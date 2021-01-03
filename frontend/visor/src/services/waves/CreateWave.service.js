import ApiService from '../Api.service.js'

class CreateWaveService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const createWaveService = new CreateWaveService('createWave/')
