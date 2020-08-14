import ApiService from '../Api.service.js'

class UpdateEstacionService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const updateEstacionService = new UpdateEstacionService('updateEstacion/{id}')
