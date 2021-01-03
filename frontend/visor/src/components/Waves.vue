<template>
  <div class="">
    <h1>Formulario</h1>
    <label>Fecha predeterminada: 2020-02-18 </label>
    <form>
      <md-field class="md-form-group">
        <md-icon class="bh-text-primary">list_alt</md-icon>
        <label>Nombre Estacion</label>
        <md-select v-model="datos.nombre" name="traza" place>
          <md-option v-for="traza in trazas" v-bind:key="traza.nombre" :value="traza.nombre" aria-required="required">{{ traza.nombre }}</md-option>
        </md-select>
      </md-field>
      <md-field class="md-form-group">
        <md-icon class="bh-text-primary">list_alt</md-icon>
        <label>Hora inicio</label>
        <md-input v-model="datos.hora_inicio" type="text" aria-required="required"/>
      </md-field  >
      <md-button class="bh-success" @click="cargarTraza(datos)">Pedir traza</md-button>
    </form>
    <div class="" style="justify-content: center; height:40% ;width:40% ;">
    <line-chart :chart-data="datos.datacollection"></line-chart>
    </div>
    <div id="container" style="height: 400px; min-width: 310px">
    </div>
    <!-- <div class="" style="justify-content: center; height:40% ;width:40% ;">
    <line-chart :chart-data="datos.datacollectionE"></line-chart>
    </div>
    <div class="" style="justify-content: center; height:40% ;width:40% ;">
    <line-chart :chart-data="datos.datacollectionN"></line-chart>
    </div> -->
  </div>
</template>

<script>

import { createWaveService } from '@/services/waves/CreateWave.service'
// import { Line } from 'vue-chartjs'
import LineChart from './linechart.js'

export default {
  name: 'Form',
  components: {
    LineChart
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
        // fecha_inicio: '',
        // fecha_fin: '',
        hora_inicio: '',
        // hora_fin: '',
        datacollection: {}
        // datacollectionE: {},
        // datacollectionN: {}
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
            label: 'grafico z',
            backgroundColor: '#ffffff',
            data: coordenadasY,
            radius: 0
          }
        ],
        options: {
          elements: {
            point: {
              radius: 0
            }
          }
        }
      }
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
