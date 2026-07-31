import { useState } from 'react'

function Users() {
  const [users, setUsers] = useState([])

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-8 text-yellow-400">User Management</h1>
      
      <div className="bg-white/5 rounded-xl border border-white/10 overflow-hidden">
        <table className="w-full">
          <thead className="bg-white/10">
            <tr>
              <th className="p-4 text-left">ID</th>
              <th className="p-4 text-left">Username</th>
              <th className="p-4 text-left">Email</th>
              <th className="p-4 text-left">Level</th>
              <th className="p-4 text-left">Status</th>
              <th className="p-4 text-left">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-t border-white/10">
              <td className="p-4">1</td>
              <td className="p-4">testuser</td>
              <td className="p-4">test@example.com</td>
              <td className="p-4">1</td>
              <td className="p-4"><span className="text-green-400">Active</span></td>
              <td className="p-4">
                <button className="text-red-400 hover:text-red-300">Ban</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default Users
