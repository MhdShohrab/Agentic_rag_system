import { useState, useEffect } from 'react'
import { FileText, Menu, Moon, Sun, X } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { UploadBox } from '@/components/upload-box'
import { ChatBox } from '@/components/chat-box'
import { ToastContainer } from '@/components/Toast'
import { toast } from '@/hooks/useToast'
import { uploadFiles, askQuestion } from '@/lib/api'
import { useTheme } from '@/hooks/useTheme'

function App() {
  const [uploadedFiles, setUploadedFiles] = useState([])
  const [messages, setMessages] = useState([])
  const [isUploading, setIsUploading] = useState(false)
  const [isAsking, setIsAsking] = useState(false)
  const [showUpload, setShowUpload] = useState(true)
  const { theme, setTheme } = useTheme()

  useEffect(() => {
    // Set initial theme
    const html = document.documentElement
    if (theme === 'dark') {
      html.classList.add('dark')
    } else {
      html.classList.remove('dark')
    }
  }, [theme])

  const handleUpload = async (newFiles) => {
    const updatedFiles = [...uploadedFiles, ...newFiles]
    setIsUploading(true)
    try {
      await uploadFiles(updatedFiles)
      setUploadedFiles(updatedFiles)
      toast.success(`Successfully uploaded documents`)
    } catch (error) {
      toast.error('Failed to upload files. Please try again.')
      console.error('Upload error:', error)
    } finally {
      setIsUploading(false)
    }
  }

  const handleRemoveFile = async (index) => {
    const updatedFiles = uploadedFiles.filter((_, i) => i !== index)
    setUploadedFiles(updatedFiles)
    
    // Always sync with backend, even if empty
    setIsUploading(true)
    try {
      await uploadFiles(updatedFiles)
      if (updatedFiles.length === 0) {
        setMessages([])
      }
      toast.success('Document index updated')
    } catch (error) {
      toast.error('Failed to update document index')
      console.error('Remove error:', error)
    } finally {
      setIsUploading(false)
    }
  }

  const handleSendMessage = async (message) => {
    // Add user message
    const userMessage = { role: 'user', content: message }
    setMessages((prev) => [...prev, userMessage])

    setIsAsking(true)
    try {
      const response = await askQuestion(message)
      const assistantMessage = {
        role: 'assistant',
        content: response.answer,
        toolUsed: response.tool_used,
        type: response.type,
      }
      setMessages((prev) => [...prev, assistantMessage])
    } catch (error) {
      toast.error('Failed to get response. Please try again.')
      console.error('Ask error:', error)
      // Remove user message on error
      setMessages((prev) => prev.slice(0, -1))
    } finally {
      setIsAsking(false)
    }
  }

  return (
    <div className="flex h-screen flex-col bg-background">
      <ToastContainer />
      
      {/* Header */}
      <header className="border-b border-border/50 bg-background/80 backdrop-blur-xl sticky top-0 z-50">
        <div className="flex h-16 items-center justify-between px-6">
          <div className="flex items-center gap-4">
            <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-primary/10 border border-primary/20">
              <FileText className="h-5 w-5 text-primary" />
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight">AI IntelliDocs</h1>
              <p className="text-xs text-muted-foreground font-medium">
                Your Intelligent Document Assistant
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3">
            <Button
              variant="outline"
              size="sm"
              onClick={() => setShowUpload(!showUpload)}
              className="hidden lg:flex gap-2 rounded-xl border-border/50 bg-secondary/40 hover:bg-secondary/60 transition-all active:scale-95"
            >
              <Menu className="h-4 w-4" />
              <span>{showUpload ? 'Hide' : 'Show'} Sidebar</span>
            </Button>
            
            <div className="flex h-10 w-px bg-border/50 mx-1 hidden lg:block" />
            
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
              className="h-10 w-10 rounded-xl hover:bg-primary/5 transition-colors"
            >
              <Sun className="h-5 w-5 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0 text-primary" />
              <Moon className="absolute h-5 w-5 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100 text-primary" />
            </Button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex flex-1 overflow-hidden">
        {/* Upload Sidebar */}
        {showUpload && (
          <aside className="relative border-r border-border/50 bg-card/30 backdrop-blur-xl w-sidebar overflow-hidden">
            {/* Grid Pattern Background */}
            <div className="absolute inset-0 bg-grid opacity-20 pointer-events-none" />
            
            <div className="relative z-10 flex flex-col h-full p-6">
              <div className="space-y-6">
                <div className="space-y-1">
                  <h2 className="text-2xl font-bold tracking-tight">AI IntelliDocs</h2>
                  <p className="text-sm text-muted-foreground font-medium">
                    Upload upto 3 pdf
                  </p>
                </div>

                <UploadBox
                  onUpload={handleUpload}
                  uploadedFiles={uploadedFiles}
                  isUploading={isUploading}
                />

                {/* File List section in sidebar */}
                {uploadedFiles.length > 0 && (
                  <div className="space-y-3 pt-4">
                    <div className="h-px bg-border/50" />
                    {uploadedFiles.map((file, index) => (
                      <div
                        key={index}
                        className="group flex items-center gap-3 rounded-xl bg-card/50 p-3 border border-border/50 hover:border-primary/50 transition-all"
                      >
                        <div className="rounded-lg bg-primary/10 p-2">
                          <FileText className="h-4 w-4 text-primary" />
                        </div>
                        <div className="flex-1 min-w-0">
                          <p className="truncate text-sm font-medium">{file.name}</p>
                        </div>
                        <Button
                          onClick={() => handleRemoveFile(index)}
                          variant="ghost"
                          size="sm"
                          className="h-8 w-8 rounded-lg p-0 hover:bg-destructive/10 hover:text-destructive"
                        >
                          <X className="h-4 w-4 text-muted-foreground" />
                        </Button>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </aside>
        )}

        {/* Chat Area */}
        <main className="flex flex-col w-chat overflow-hidden h-full">
          <ChatBox
            onSendMessage={handleSendMessage}
            messages={messages}
            isLoading={isAsking}
            disabled={uploadedFiles.length === 0}
          />
        </main>
      </div>
    </div>
  )
}

export default App
