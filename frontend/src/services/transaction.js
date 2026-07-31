import api from './api'

export const getTransactions = () => api.get('/api/transaction/')
export const getTransaction = (txHash) => api.get(`/api/transaction/${txHash}`)
