import ApiService from '../Api.service.js'

class AllEstacionesService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const allEstacionesService = new AllEstacionesService('estaciones')
