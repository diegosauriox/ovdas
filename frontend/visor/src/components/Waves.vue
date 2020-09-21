<template>
  <div class="">
    <h1>Formulario</h1>
    <form>
      <md-field class="md-form-group">
            <label>Nombre Estacion</label>
            <md-input model="datos.nombre" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <label>Fecha inicio</label>
            <md-input model="datos.fecha_inicio" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <label>Fecha fin</label>
            <md-input model="datos.fecha_fin" type="text" aria-required="required" />
          </md-field>
          <md-button class="bh-success" @click="cargarTraza(datos)">Pedir traza</md-button>
    </form>
    <p>{{datos.nombre}}</p>
  </div>
</template>
<script>
import { createWaveService } from '@/services/waves/CreateWave.service'
export default {
  name: 'Form',
  data () {
    return {
      datos: {
        nombre: 'ejemplo',
        fecha_inicio: '',
        fecha_fin: ''
      },
      traza: {
      }
    }
  },
  methods: {
    cargarTraza (datos) {
      let vm = this
      console.log(datos)
      createWaveService.save(datos).then(data => {
        console.log("enviado")
      },
       vm.traza = data.body
      // vm.element.rut = '',
      )
    }
  }
}

</script>
