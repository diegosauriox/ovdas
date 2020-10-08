import ApiService from '../Api.service.js'

class LoadAvistamientoService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const loadAvistamientoService = new LoadAvistamientoService('loadVolcanesCSV')
