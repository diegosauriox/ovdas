import ApiService from './../Api.service.js'

class AllTrazasService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const allTrazasService = new AllTrazasService('trazas')
