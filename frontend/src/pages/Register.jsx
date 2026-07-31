import { useState } from 'react'
import { Link } from 'react-router-dom'

function Register() {
  const [form, setForm] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  })

  const handleSubmit = (e) => {
    e.preventDefault()
    // TODO: API call
  }

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="glass-card p-8 w-full max-w-md">
        <h1 className="text-3xl font-bold mb-6 text-center text-avesta-gold">Register</h1>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-gray-400 mb-2">Username</label>
            <input
              type="text"
              value={form.username}
              onChange={(e) => setForm({...form, username: e.target.value})}
              className="w-full px-4 py-3 bg-black/50 rounded-lg border border-white/10 focus:border-avesta-purple outline-none"
            />
          </div>
          
          <div>
            <label className="block text-gray-400 mb-2">Email</label>
            <input
              type="email"
              value={form.email}
              onChange={(e) => setForm({...form, email: e.target.value})}
              className="w-full px-4 py-3 bg-black/50 rounded-lg border border-white/10 focus:border-avesta-purple outline-none"
            />
          </div>
          
          <div>
            <label className="block text-gray-400 mb-2">Password</label>
            <input
              type="password"
              value={form.password}
              onChange={(e) => setForm({...form, password: e.target.value})}
              className="w-full px-4 py-3 bg-black/50 rounded-lg border border-white/10 focus:border-avesta-purple outline-none"
            />
          </div>
          
          <button
            type="submit"
            className="w-full py-3 bg-avesta-purple rounded-lg hover:bg-avesta-purple/80 transition font-bold"
          >
            Create Account
          </button>
        </form>
        
        <p className="mt-4 text-center text-gray-400">
          Already have an account?{' '}
          <Link to="/login" className="text-avesta-gold">Login</Link>
        </p>
      </div>
    </div>
  )
}

export default Register
