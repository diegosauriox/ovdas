import ApiService from '../Api.service.js'

class DeleteVolcanService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const deleteVolcanService = new DeleteVolcanService('deleteVolcan/{id}')
