import { useState } from 'react'
import { Link } from 'react-router-dom'

function Login() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    // TODO: API call
  }

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="glass-card p-8 w-full max-w-md">
        <h1 className="text-3xl font-bold mb-6 text-center text-avesta-gold">Login</h1>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-gray-400 mb-2">Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-4 py-3 bg-black/50 rounded-lg border border-white/10 focus:border-avesta-purple outline-none"
            />
          </div>
          
          <div>
            <label className="block text-gray-400 mb-2">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 bg-black/50 rounded-lg border border-white/10 focus:border-avesta-purple outline-none"
            />
          </div>
          
          <button
            type="submit"
            className="w-full py-3 bg-avesta-purple rounded-lg hover:bg-avesta-purple/80 transition font-bold"
          >
            Login
          </button>
        </form>
        
        <p className="mt-4 text-center text-gray-400">
          Don't have an account?{' '}
          <Link to="/register" className="text-avesta-gold">Register</Link>
        </p>
      </div>
    </div>
  )
}

export default Login
