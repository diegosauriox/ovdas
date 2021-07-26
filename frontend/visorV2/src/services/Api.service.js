import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

class ApiConnect {
  constructor (route) {
    this.resource = Vue.resource(process.env.address.api + route)
  }
  getResource () {
    return this.resource
  }
  getVueInstance () {
    return Vue
  }
  query () {
    return this.resource.query()
  }
  getById (id) {
    return this.resource.get({id})
  }
  shipMail (email) {
    return this.resource.get({email})
  }
  save (model) {
    return this.resource.save(model)
  }
  getByIdEvaluacion (idEvaluacion, idUser) {
    return this.resource.get({idEvaluacion, idUser})
  }
  update (id, model) {
    return this.resource.update({id}, model)
  }
  destroy (id) {
    return this.resource.delete({id})
  }
}

export default ApiConnect
