import api from './api'

export const startMining = () => api.post('/api/mining/start')
export const getMiningStatus = () => api.get('/api/mining/status')
export const claimReward = () => api.post('/api/mining/claim')
export const watchAdBoost = () => api.post('/api/mining/boost')
export const luckySpin = (useAd = false) => api.post(`/api/mining/spin?use_ad=${useAd}`)
