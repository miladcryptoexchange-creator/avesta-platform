        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/wallet" element={<Wallet />} />
          <Route path="/mining" element={<Mining />} />
          <Route path="/transactions" element={<Transactions />} />
          <Route path="/referral" element={<Referral />} />
          <Route path="/staking" element={<Staking />} />
          <Route path="/governance" element={<Governance />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/nft" element={<NFTMarketplace />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
