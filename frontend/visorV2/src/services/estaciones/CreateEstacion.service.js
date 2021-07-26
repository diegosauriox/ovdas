import ApiService from '../Api.service.js'

class CreateEstacionService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const createEstacionService = new CreateEstacionService('createEstacion')
