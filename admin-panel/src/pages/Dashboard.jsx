import { useState, useEffect } from 'react'

function Dashboard() {
  const [stats, setStats] = useState({
    totalUsers: 0,
    activeMiners: 0,
    totalSupply: 21000000000,
    circulatingSupply: 0
  })

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-8 text-yellow-400">Admin Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-white/5 p-6 rounded-xl border border-white/10">
          <p className="text-gray-400">Total Users</p>
          <p className="text-3xl font-bold">{stats.totalUsers.toLocaleString()}</p>
        </div>
        <div className="bg-white/5 p-6 rounded-xl border border-white/10">
          <p className="text-gray-400">Active Miners</p>
          <p className="text-3xl font-bold">{stats.activeMiners.toLocaleString()}</p>
        </div>
        <div className="bg-white/5 p-6 rounded-xl border border-white/10">
          <p className="text-gray-400">Total Supply</p>
          <p className="text-3xl font-bold">{(stats.totalSupply / 1e9).toFixed(0)}B AVN</p>
        </div>
        <div className="bg-white/5 p-6 rounded-xl border border-white/10">
          <p className="text-gray-400">Circulating</p>
          <p className="text-3xl font-bold">{(stats.circulatingSupply / 1e9).toFixed(0)}B AVN</p>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
