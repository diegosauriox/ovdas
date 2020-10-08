<template>
  <div class="">
    <h1>Formulario</h1>
    <form>
      <md-field class="md-form-group">
        <label>Nombre Estacion</label>
        <md-select v-model="datos.nombre" name="traza" place>
          <md-option v-for="traza in trazas" v-bind:key="traza.nombre" :value="traza.nombre">{{ traza.nombre }}</md-option>
        </md-select>
      </md-field>
      <md-field class="md-form-group">
        <label>Fecha inicio</label>
        <md-input v-model="datos.fecha_inicio" type="text" aria-required="required" />
      </md-field>
      <md-field class="md-form-group">
        <label>Fecha fin</label>
        <md-input v-model="datos.fecha_fin" type="text" aria-required="required" />
      </md-field>
      <md-button class="bh-success" @click="cargarTraza(datos)">Pedir traza</md-button>
    </form>
    <canvas id="myChart" width="400" height="400"></canvas>
    <div class="small">
      <graficoLiena :chartdata="datacollection"></graficoLiena>
      <button @click="sfillData()">Randomizar</button>
    </div>
  </div>
</template>

<script>

import { createWaveService } from '@/services/waves/CreateWave.service'
import { Line as graficoLiena } from 'vue-chartjs'
export default {
  name: 'Form',
  components: {
    graficoLiena
  },
  data () {
    return {
      options: {
        type: Object,
        default: null
      },
      datacollection: null,
      coordenadasX: [],
      coordenadasY: [],
      datos: {
        nombre: '',
        fecha_inicio: '',
        fecha_fin: ''
      },
      trazas: [
        {nombre: 'FRE'},
        {nombre: 'CHS'},
        {nombre: 'PLA'},
        {nombre: 'CHA'},
        {nombre: 'ROB'},
        {nombre: 'FU2'},
        {nombre: 'SHG'},
        {nombre: 'NBL'},
        {nombre: 'PTZ'},
        {nombre: 'PHI'},
        {nombre: 'LBN'},
        {nombre: 'BI0'}
      ]
    }
  },
  methods: {
    cargarTraza (datos) {
      let vm = this
      console.log(datos)
      createWaveService.save(datos).then(data => {
        console.log('enviado')
        console.log(data.body)
        vm.coordenadasX = data.body[0]
        vm.coordenadasY = data.body[1]
      }
      // vm.element.rut = '',
      )
    },
    sfillData () {
      console.log('modifica grafico')
      this.datacollection = {
        labels: [this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()]
          }, {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()]
          }
        ]
      }
      console.log(this.datacollection)
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  },
  mounted () {
  // cuando carga la pagina te monta con esa funcion
    let vm = this
    vm.sfillData()
    console.log('odio todo')
  }
}
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
