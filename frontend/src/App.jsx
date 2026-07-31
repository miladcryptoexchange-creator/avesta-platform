import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Dashboard from './pages/Dashboard'
import Wallet from './pages/Wallet'
import Mining from './pages/Mining'
import Transactions from './pages/Transactions'
import Referral from './pages/Referral'
import Staking from './pages/Staking'
import Governance from './pages/Governance'
import Profile from './pages/Profile'
import Login from './pages/Login'
import Register from './pages/Register'
import NFTMarketplace from './pages/NFTMarketplace'

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-avesta-dark text-white">
        <Navbar />
       
