import { useState, useEffect } from 'react'
import { getWallet } from '../services/wallet'

export function useWallet() {
  const [wallet, setWallet] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchWallet = async () => {
      try {
        const response = await getWallet()
        setWallet(response.data)
      } catch (error) {
        console.error('Failed to fetch wallet:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchWallet()
  }, [])

  return { wallet, loading }
}
