import { useState, useRef, useEffect } from "react";
import { Send } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { MessageBubble } from "@/components/message-bubble";
import { TypingIndicator } from "@/components/typing-indicator";
import { cn } from "@/lib/utils";

export function ChatBox({ onSendMessage, messages, isLoading, disabled }) {
  const [input, setInput] = useState("");
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || isLoading || disabled) return;

    const message = input.trim();
    setInput("");

    // Reset textarea height
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
    }

    await onSendMessage(message);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  const handleTextareaChange = (e) => {
    setInput(e.target.value);
    // Auto-resize textarea
    e.target.style.height = "auto";
    e.target.style.height = `${Math.min(e.target.scrollHeight, 200)}px`;
  };

  return (
    <div className="chat-container">
      {/* Messages Area */}
      <div className="messages">
        <div className="mx-auto max-w-3xl space-y-8">
          {messages.length === 0 ? (
            <div className="flex h-full min-h-[400px] flex-col items-center justify-center text-center animate-fadeIn">
              <div className="space-y-6">
                <div className="mx-auto flex h-24 w-24 items-center justify-center rounded-3xl bg-primary/5 transition-transform hover:scale-110">
                  <Send className="h-12 w-12 text-primary rotate-[320deg]" />
                </div>
                <div className="space-y-2">
                  <h3 className="text-3xl font-bold tracking-tight">
                    Start a Conversation
                  </h3>
                  <p className="text-muted-foreground max-w-[280px] mx-auto text-lg leading-relaxed">
                    {disabled
                      ? "Upload at least one PDF to begin"
                      : "Ask me anything about your documents"}
                  </p>
                </div>
              </div>
            </div>
          ) : (
            <>
              {messages.map((message, index) => (
                <MessageBubble key={index} message={message} />
              ))}
              {isLoading && <TypingIndicator />}
              <div ref={messagesEndRef} />
            </>
          )}
        </div>
      </div>

      {/* Input Area */}
      <div className="border-t border-border/50 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="mx-auto max-w-3xl p-4">
          <form onSubmit={handleSubmit}>
            <div className="flex items-end gap-2">
              <Textarea
                ref={textareaRef}
                value={input}
                onChange={handleTextareaChange}
                onKeyDown={handleKeyDown}
                placeholder={
                  disabled
                    ? "Upload PDF files first..."
                    : "Ask a question about your documents..."
                }
                disabled={disabled || isLoading}
                className={cn(
                  "min-h-[52px] max-h-[200px] flex-1 resize-none rounded-2xl bg-card/50 backdrop-blur-sm transition-all",
                  "focus:bg-card/80",
                  disabled && "cursor-not-allowed opacity-50",
                )}
                rows={1}
              />
              <Button
                type="submit"
                size="sm"
                disabled={!input.trim() || isLoading || disabled}
                className="h-[52px] w-[52px] shrink-0 rounded-2xl shadow-lg shadow-primary/20 transition-all active:scale-95"
              >
                <Send className="h-5 w-5" />
                <span className="sr-only">Send message</span>
              </Button>
            </div>
          </form>
          <p className="mt-2 text-center text-xs text-muted-foreground">
            Press Enter to send, Shift+Enter for new line
          </p>
        </div>
      </div>
    </div>
  );
}
