function Navbar() {
  return (
    <div className="h-16 bg-black/50 border-b border-white/10 flex items-center justify-between px-8">
      <h2 className="text-lg font-semibold">Avesta Platform</h2>
      <div className="flex items-center space-x-4">
        <span className="text-gray-400">Admin</span>
        <button className="px-4 py-2 bg-red-500/20 text-red-400 rounded-lg">
          Logout
        </button>
      </div>
    </div>
  )
}

export default Navbar
