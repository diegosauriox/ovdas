import ApiService from '../Api.service.js'

class LoadVolcanService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const loadVolcanService = new LoadVolcanService('loadVolcanesCSV')
