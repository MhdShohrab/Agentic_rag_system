import { useCallback } from 'react'

let toastCallback = null

export function setToastCallback(callback) {
  toastCallback = callback
}

export function useToast() {
  const toast = useCallback((message, type = 'default') => {
    if (toastCallback) {
      toastCallback(message, type)
    } else {
      console.log(`[${type}] ${message}`)
    }
  }, [])

  return { toast }
}

export const toast = {
  success: (message) => {
    if (toastCallback) {
      toastCallback(message, 'success')
    } else {
      console.log(`[success] ${message}`)
    }
  },
  error: (message) => {
    if (toastCallback) {
      toastCallback(message, 'error')
    } else {
      console.log(`[error] ${message}`)
    }
  },
  info: (message) => {
    if (toastCallback) {
      toastCallback(message, 'info')
    } else {
      console.log(`[info] ${message}`)
    }
  },
}
