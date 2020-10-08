<template>
  <div class="">
    <h1>Formulario</h1>
    <form>
      <md-field class="md-form-group">
        <md-icon class="bh-text-primary">list_alt</md-icon>
        <label>Nombre Estacion</label>
        <md-select v-model="datos.nombre" name="traza" place>
          <md-option v-for="traza in trazas" v-bind:key="traza.nombre" :value="traza.nombre">{{ traza.nombre }}</md-option>
        </md-select>
      </md-field>
      <md-datepicker v-model="datos.fecha_inicio">
        <label>Fecha inicio</label>
      </md-datepicker>
      <md-datepicker v-model="datos.fecha_fin">
        <label>Fecha Fin</label>
      </md-datepicker>
      <label>Hora inicio</label>
      <VueMaterialDateTimePicker v-model="datos.hora_inicio" :is-date-only="false" :valueFormatted="momento" />
      <md-field class="md-form-group">
        <label>Hora Fin</label>
        <md-input v-model="datos.hora_fin" type="text" aria-required="required" pattern="^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"/>
      </md-field>
      <md-button class="bh-success" @click="cargarTraza(datos)">Pedir traza</md-button>
    </form>
    <div class="small" style="justify-content: center; height:40% ;width:40% ;">
    <line-chart :chart-data="datos.datacollection"></line-chart>
    </div>
  </div>
</template>

<script>

import { createWaveService } from '@/services/waves/CreateWave.service'
// import { Line } from 'vue-chartjs'
import LineChart from './linechart.js'
import VueMaterialDateTimePicker from 'vue-material-date-time-picker'
import moment from 'moment'
export default {
  name: 'Form',
  components: {
    LineChart,
    VueMaterialDateTimePicker
  },
  computed: {
    momento () {
      return moment(String(this.datos.hora_inicio)).format('DD/MM/YYYY hh:mm')
    }
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
        fecha_fin: '',
        hora_inicio: '',
        hora_fin: '',
        datacollection: {}
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
        // vm.coordenadasX = data.body[0]
        // vm.coordenadasY = data.body[1]
        vm.fillData(data.body[0], data.body[1])
      }
      // vm.element.rut = '',
      )
    },
    fillData (coordenadasX, coordenadasY) {
      this.datos.datacollection = {
        labels: coordenadasX,
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#ffffff',
            data: coordenadasY
          }
        ]
      }
      console.log(this.datacollection)
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  }
}
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
