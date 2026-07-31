import { motion } from 'framer-motion'

function RewardCard() {
  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="glass-card p-6"
    >
      <h3 className="text-gray-400 mb-2">Total Earned</h3>
      <p className="text-3xl font-bold text-avesta-purple">0 AVN</p>
      <p className="text-sm text-gray-500 mt-2">From mining & referrals</p>
    </motion.div>
  )
}

export default RewardCard
