import { Link } from 'react-router-dom'

function Sidebar() {
  const menuItems = [
    { path: '/', label: 'Dashboard', icon: '📊' },
    { path: '/users', label: 'Users', icon: '👥' },
    { path: '/wallets', label: 'Wallets', icon: '💰' },
    { path: '/transactions', label: 'Transactions', icon: '📈' },
    { path: '/mining', label: 'Mining', icon: '⛏️' },
    { path: '/settings', label: 'Settings', icon: '⚙️' }
  ]

  return (
    <div className="w-64 bg-black/50 border-r border-white/10 h-screen">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-yellow-400">AVN Admin</h1>
      </div>
      
      <nav className="mt-6">
        {menuItems.map(item => (
          <Link
            key={item.path}
            to={item.path}
            className="flex items-center px-6 py-3 hover:bg-white/5 transition"
          >
            <span className="mr-3">{item.icon}</span>
            {item.label}
          </Link>
        ))}
      </nav>
    </div>
  )
}

export default Sidebar
