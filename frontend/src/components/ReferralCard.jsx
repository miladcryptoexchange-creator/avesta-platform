import { motion } from 'framer-motion'

function ReferralCard() {
  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="glass-card p-6"
    >
      <h3 className="text-gray-400 mb-2">Referrals</h3>
      <p className="text-3xl font-bold text-avesta-blue">0</p>
      <p className="text-sm text-gray-500 mt-2">Invite friends to earn</p>
    </motion.div>
  )
}

export default ReferralCard
