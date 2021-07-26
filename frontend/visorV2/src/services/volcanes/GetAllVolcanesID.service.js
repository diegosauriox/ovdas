import ApiService from '../Api.service.js'

class AllVolcanesIDService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const allVolcanesIDService = new AllVolcanesIDService('volcanesIdName')
