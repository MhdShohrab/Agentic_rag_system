import { useState, useRef } from 'react'
import { Upload, X, FileText, Loader2 } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { cn } from '@/lib/utils'

export function UploadBox({ onUpload, uploadedFiles, isUploading }) {
  const fileInputRef = useRef(null)

  const handleFileSelect = async (e) => {
    const files = e.target.files
    if (!files) return

    const pdfFiles = Array.from(files).filter(
      (file) => file.type === 'application/pdf'
    )

    if (pdfFiles.length > 0) {
      await onUpload(pdfFiles.slice(0, 3 - uploadedFiles.length))
    }
    
    // Reset input so the same file can be selected again if needed
    e.target.value = ''
  }

  return (
    <div className="w-full">
      <input
        ref={fileInputRef}
        type="file"
        accept=".pdf"
        multiple
        onChange={handleFileSelect}
        className="hidden"
        disabled={uploadedFiles.length >= 3 || isUploading}
      />

      <Button
        onClick={() => fileInputRef.current?.click()}
        disabled={uploadedFiles.length >= 3 || isUploading}
        className="w-full h-12 rounded-xl bg-primary text-primary-foreground hover:bg-primary/90 flex items-center justify-center gap-2 shadow-lg shadow-primary/20 transition-all active:scale-95"
      >
        {isUploading ? (
          <Loader2 className="h-5 w-5 animate-spin" />
        ) : (
          <Upload className="h-5 w-5" />
        )}
        <span className="font-semibold">
          {isUploading ? 'Uploading...' : 'Upload PDFs'}
        </span>
      </Button>
    </div>
  )
}
