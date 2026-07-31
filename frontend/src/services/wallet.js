import api from './api'

export const getWallet = () => api.get('/api/wallet/')
export const transfer = (data) => api.post('/api/wallet/transfer', data)
export const getHistory = () => api.get('/api/wallet/history')
