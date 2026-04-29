import { Badge } from '@/components/ui/badge'
import { cn } from '@/lib/utils'
import { Bot, User } from 'lucide-react'

const toolColors = {
  rag: 'badge-rag',
  web: 'badge-web',
  calculator: 'badge-calculator',
  default: 'badge-default',
  llm: 'badge-llm',
}

export function MessageBubble({ message }) {
  const isUser = message.role === 'user'

  return (
    <div
      className={cn(
        'flex gap-4 animate-in fade-in slide-in-from-bottom-2 duration-500',
        isUser ? 'justify-end' : 'justify-start'
      )}
    >
      {!isUser && (
        <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-primary/10">
          <Bot className="h-5 w-5 text-primary" />
        </div>
      )}

      <div
        className={cn(
          'max-w-[80%] space-y-2 rounded-2xl px-4 py-3 backdrop-blur-sm transition-all',
          isUser
            ? 'bg-primary text-primary-foreground'
            : 'bg-card/50 border border-border/50'
        )}
      >
        <p className="whitespace-pre-wrap break-words leading-relaxed">
          {message.content}
        </p>

        {!isUser && (message.toolUsed || message.type) && (
          <div className="flex flex-wrap gap-2 pt-1">
            {message.toolUsed && (
              <Badge
                variant="outline"
                className={cn(
                  'rounded-lg',
                  toolColors[message.toolUsed] || toolColors.default
                )}
              >
                {message.toolUsed}
              </Badge>
            )}
            {message.type && (
              <Badge variant="outline" className="rounded-lg">
                {message.type.replace('_', ' ')}
              </Badge>
            )}
          </div>
        )}
      </div>

      {isUser && (
        <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-xl bg-primary/10">
          <User className="h-5 w-5 text-primary" />
        </div>
      )}
    </div>
  )
}
