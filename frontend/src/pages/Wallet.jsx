import { useState } from 'react'
import { motion } from 'framer-motion'

function Wallet() {
  const [address, setAddress] = useState('AVN-XXXXXXXX')
  const [balance, setBalance] = useState('0.00000000')

  return (
    <div className="max-w-4xl mx-auto px-6 py-8">
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="glass-card p-8"
      >
        <h1 className="text-3xl font-bold mb-6 text-avesta-gold">AVN Wallet</h1>
        
        <div className="mb-6">
          <p className="text-gray-400 mb-2">Address</p>
          <div className="flex items-center space-x-4">
            <code className="bg-black/50 px-4 py-2 rounded-lg">{address}</code>
            <button className="text-avesta-purple hover:text-avesta-gold">
              Copy
            </button>
          </div>
        </div>
        
        <div className="mb-8">
          <p className="text-gray-400 mb-2">Balance</p>
          <p className="text-4xl font-bold">{balance} <span className="text-avesta-gold">AVN</span></p>
        </div>
        
        <div className="flex space-x-4">
          <button className="flex-1 py-3 bg-avesta-purple rounded-lg hover:bg-avesta-purple/80 transition">
            Send
          </button>
          <button className="flex-1 py-3 bg-avesta-blue rounded-lg hover:bg-avesta-blue/80 transition">
            Receive
          </button>
        </div>
      </motion.div>
    </div>
  )
}

export default Wallet
