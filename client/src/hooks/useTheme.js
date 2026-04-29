import { useState, useEffect } from 'react'

export function useTheme() {
  const [theme, setThemeState] = useState('dark')
  const [isMounted, setIsMounted] = useState(false)

  useEffect(() => {
    setIsMounted(true)
    const storedTheme = localStorage.getItem('theme') || 'dark'
    setThemeState(storedTheme)
    applyTheme(storedTheme)
  }, [])

  const setTheme = (newTheme) => {
    setThemeState(newTheme)
    localStorage.setItem('theme', newTheme)
    applyTheme(newTheme)
  }

  const applyTheme = (theme) => {
    const html = document.documentElement
    if (theme === 'dark') {
      html.classList.add('dark')
    } else {
      html.classList.remove('dark')
    }
  }

  return { theme, setTheme, isMounted }
}
