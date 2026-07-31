import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <nav className="bg-avesta-dark/80 backdrop-blur-md border-b border-white/10 px-6 py-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <Link to="/" className="text-2xl font-bold text-avesta-gold">
          AVN
        </Link>
        
        <div className="hidden md:flex space-x-6">
          <Link to="/" className="hover:text-avesta-purple transition">Dashboard</Link>
          <Link to="/wallet" className="hover:text-avesta-purple transition">Wallet</Link>
          <Link to="/mining" className="hover:text-avesta-purple transition">Mining</Link>
          <Link to="/nft" className="hover:text-avesta-purple transition">NFT</Link>
          <Link to="/staking" className="hover:text-avesta-purple transition">Staking</Link>
          <Link to="/governance" className="hover:text-avesta-purple transition">DAO</Link>
        </div>
        
        <div className="flex items-center space-x-4">
          <Link to="/login" className="px-4 py-2 rounded-lg bg-avesta-purple hover:bg-avesta-purple/80 transition">
            Login
          </Link>
        </div>
      </div>
    </nav>
  )
}

export default Navbar
