import { motion } from 'framer-motion'

function MiningCard() {
  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="glass-card p-6"
    >
      <h3 className="text-gray-400 mb-2">Mining Status</h3>
      <p className="text-2xl font-bold text-green-400">Active</p>
      <p className="text-sm text-gray-500 mt-2">Rate: 0.25 AVN/hour</p>
    </motion.div>
  )
}

export default MiningCard
