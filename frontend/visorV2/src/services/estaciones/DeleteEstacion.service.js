import ApiService from '../Api.service.js'

class DeleteEstacionService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const deleteEstacionService = new DeleteEstacionService('deleteEstacion/{id}')
