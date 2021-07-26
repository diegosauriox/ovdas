import ApiService from '../Api.service.js'

class UpdateVolcanService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const updateVolcanService = new UpdateVolcanService('updateVolcan/{id}')
