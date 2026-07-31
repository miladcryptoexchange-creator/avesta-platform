import { motion } from 'framer-motion'

function WalletCard() {
  return (
    <motion.div
      whileHover={{ scale: 1.02 }}
      className="glass-card p-6"
    >
      <h3 className="text-gray-400 mb-2">AVN Balance</h3>
      <p className="text-3xl font-bold text-avesta-gold">0.00000000 AVN</p>
      <p className="text-sm text-gray-500 mt-2">≈ $0.00 USD</p>
    </motion.div>
  )
}

export default WalletCard
