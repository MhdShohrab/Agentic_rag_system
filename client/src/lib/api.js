const API_BASE_URL = 'https://agentic-rag-system-c7nw.onrender.com'

export async function uploadFiles(files) {
  const formData = new FormData()
  files.forEach((file) => {
    formData.append('files', file)
  })
  

  const response = await fetch(`${API_BASE_URL}/upload`, {
    method: 'POST',
    body: formData,
  })

  if (!response.ok) {
    throw new Error('Failed to upload files')
  }

  return response.json()
}

export async function askQuestion(query, userId = 'default_user') {
  const response = await fetch(`${API_BASE_URL}/ask`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query, user_id: userId }),
  })

  if (!response.ok) {
    throw new Error('Failed to get response')
  }

  return response.json()
}
