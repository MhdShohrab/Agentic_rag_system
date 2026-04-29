import { Bot } from 'lucide-react'

export function TypingIndicator() {
  return (
    <div className="flex gap-4 animate-in fade-in slide-in-from-bottom-2 duration-500">
      <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-primary/10">
        <Bot className="h-5 w-5 text-primary" />
      </div>

      <div className="flex items-center gap-2 rounded-2xl border border-border/50 bg-card/50 px-4 py-3 backdrop-blur-sm">
        <div className="flex gap-1">
          <span
            className="h-2 w-2 animate-bounce rounded-full bg-primary"
            style={{ animationDelay: '0ms' }}
          />
          <span
            className="h-2 w-2 animate-bounce rounded-full bg-primary"
            style={{ animationDelay: '150ms' }}
          />
          <span
            className="h-2 w-2 animate-bounce rounded-full bg-primary"
            style={{ animationDelay: '300ms' }}
          />
        </div>
      </div>
    </div>
  )
}
