import ApiService from '../Api.service.js'

class CreateVolcanService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const createVolcanService = new CreateVolcanService('createVolcanes')
