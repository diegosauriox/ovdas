import ApiService from '../Api.service.js'

class AllVolcanesService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const allVolcanesService = new AllVolcanesService('volcanes')
