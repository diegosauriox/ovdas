import ApiService from '../Api.service.js'

class LoadLocalizacionService extends ApiService {
  constructor (endpoint) {
    super(endpoint)
    this.name = endpoint
  }
}

export const loadLocalizacionService = new LoadLocalizacionService('loadLocalizacionesCSV')
