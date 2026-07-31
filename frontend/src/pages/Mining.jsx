import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'

function Mining() {
  const [mining, setMining] = useState(false)
  const [timeLeft, setTimeLeft] = useState(86400)
  const [boost, setBoost] = useState(0)

  const formatTime = (seconds) => {
    const h = Math.floor(seconds / 3600)
    const m = Math.floor((seconds % 3600) / 60)
    const s = seconds % 60
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`
  }

  const startMining = () => {
    setMining(true)
  }

  const watchAd = () => {
    if (boost < 10) {
      setBoost(prev => prev + 2)
    }
  }

  return (
    <div className="max-w-4xl mx-auto px-6 py-8">
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="text-center"
      >
        <h1 className="text-4xl font-bold mb-8 text-avesta-gold">Mining</h1>
        
        <div className="glass-card p-12 mb-8">
          {!mining ? (
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={startMining}
              className="w-48 h-48 rounded-full bg-gradient-to-br from-avesta-purple to-avesta-blue text-2xl font-bold neon-glow"
            >
              START
              <br />MINING
            </motion.button>
          ) : (
            <div>
              <p className="text-6xl font-mono mb-4">{formatTime(timeLeft)}</p>
              <p className="text-avesta-gold mb-2">Mining Active</p>
              <p className="text-gray-400">Rate: {0.25 * (1 + boost/100)} AVN/hour</p>
              {boost > 0 && <p className="text-green-400">Boost: +{boost}%</p>}
            </div>
          )}
        </div>
        
        {mining && (
          <div className="glass-card p-6">
            <h3 className="text-xl mb-4">Ads Boost</h3>
            <p className="text-gray-400 mb-4">Watch ads to boost mining rate (+2% per ad, max 5)</p>
            <button 
              onClick={watchAd}
              disabled={boost >= 10}
              className="px-6 py-3 bg-avesta-gold text-black rounded-lg disabled:opacity-50"
            >
              Watch Ad (+2%)
            </button>
            <p className="mt-2 text-sm text-gray-500">{boost/2}/5 ads watched</p>
          </div>
        )}
      </motion.div>
    </div>
  )
}

export default Mining
