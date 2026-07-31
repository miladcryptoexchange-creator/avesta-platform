import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import WalletCard from '../components/WalletCard'
import MiningCard from '../components/MiningCard'
import ReferralCard from '../components/ReferralCard'
import RewardCard from '../components/RewardCard'

function Dashboard() {
  const [user, setUser] = useState(null)

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      <motion.h1 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-3xl font-bold mb-8"
      >
        Dashboard
      </motion.h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <WalletCard />
        <MiningCard />
        <ReferralCard />
        <RewardCard />
      </div>
    </div>
  )
}

export default Dashboard
