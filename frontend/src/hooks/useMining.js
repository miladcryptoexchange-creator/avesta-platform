import { useState, useEffect } from 'react'
import { getMiningStatus } from '../services/mining'

export function useMining() {
  const [status, setStatus] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await getMiningStatus()
        setStatus(response.data)
      } catch (error) {
        console.error('Failed to fetch mining status:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchStatus()
    const interval = setInterval(fetchStatus, 30000) // Update every 30s

    return () => clearInterval(interval)
  }, [])

  return { status, loading }
}
