<template>
  <div class="">
    <md-table v-model="volcanes" md-sort="nombre" md-sort-order="asc" md-card md-fixed-header>
      <md-table-toolbar>
        <div class="md-toolbar-section-start">
          <h1 class="md-title">Volcanes</h1>
          <div class="md-layout-item">
              <md-button class="md-raised bh-primary" @click="showDialogCreate = true">
                Nuevo Volcan
                <md-icon>add</md-icon>
              </md-button>
            </div>
        </div>

        <md-field md-clearable class="md-toolbar-section-end">
          <md-input placeholder="Buscar por nombre..."  />
        </md-field>
      </md-table-toolbar>

      <md-table-empty-state
        md-label="No existen registros"
        :md-description="`No se han podido cargar los datos correctamente o estan vacios los registros, pruebe creando nuevos datos`">
        <md-button class="bh-primary md-raised"  @click="showDialogCreate = true">Crear nuevo VOlcan</md-button>
      </md-table-empty-state>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID" md-sort-by="id_volcan" md-numeric>{{ item.id_volcan }}</md-table-cell>
        <md-table-cell md-label="Nombre" md-sort-by="nombre">{{ item.nombre }}</md-table-cell>
        <md-table-cell md-label="altura" md-sort-by="altura">{{ item.altura }}</md-table-cell>
        <md-table-cell md-label="Latitu" md-sort-by="latitud">{{ item.latitud }}</md-table-cell>
        <md-table-cell md-label="Longitud" md-sort-by="longitud">{{ item.longitud }}</md-table-cell>
        <md-table-cell md-label="Acciones">
          <md-button class="md-icon-button bh-warning md-primary md-raised">
            <md-icon>edit</md-icon>
          </md-button>
          <md-button class="bh-danger md-icon-button ">
            <md-icon>cancel</md-icon>
          </md-button>
        </md-table-cell>
      </md-table-row>
    </md-table>
    <div class="">
      <md-dialog class="md-size-30" :md-active.sync="showDialogCreate"  style="width:auto;">
        <md-dialog-title>Nuevo</md-dialog-title>
        <div class="">
        <form>
          <md-field class="md-form-group">
            <md-icon>list_alt</md-icon>
            <label>Id volcán...</label>
            <md-input v-model="element.id_volcan" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>title</md-icon>
            <label>Nombre...</label>
            <md-input v-model="element.nombre" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>text_format</md-icon>
            <label>Descripción...</label>
            <md-textarea v-model="element.descripcion" aria-required="required"></md-textarea>
          </md-field>
          <md-field class="md-form-group">
            <md-icon>height</md-icon>
            <label>Altura...</label>
            <md-input v-model="element.altura" type="number" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>add_location</md-icon>
            <label>Latitud...</label>
            <md-input v-model="element.latitud" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>add_location</md-icon>
            <label>Latitud...</label>
            <md-input v-model="element.longitud" type="text" aria-required="required" />
          </md-field>
        </form>
        </div>
        <md-dialog-actions>
          <md-button class="bh-danger" @click="showDialogCreate = false">cancelar</md-button>
          <md-button class="bh-success" @click="newElement(element)">Crear</md-button>
        </md-dialog-actions>
      </md-dialog>
    </div>
  </div>
</template>

<script>
import { allVolcanesService } from '@/services/volcanes/GetAllVolcanes.service'
import { createVolcanService } from '@/services/volcanes/CreateVolcan.service'

export default {
  name: 'Volcanes',
  data () {
    return {
      msg: 'prueba inicial de datos',
      volcanes: [],
      imagen: '',
      showDialogCreate: false,
      showSnackbar: false,
      textSnackbar: '',
      colorSnackbar: '',
      timeout: 4000,
      bancos: [],
      showDialogUpdate: false,
      search: '',
      element: {}
    }
  },
  methods: {
    loadVolacanes () {
      let vm = this
      allVolcanesService.query().then(data => {
        vm.volcanes = data.body
        console.log(vm.volcanes)
      })
    },
    newElement (model) {
      let vm = this
      console.log(model)
      createVolcanService.save(model).then(data => {
        vm.volcanes = data.body
        vm.textSnackbar = 'El campo fue creado con éxito'
        vm.showSnackbar = true
        vm.colorSnackbar = 'background-color: green'
      },
      response => {
        vm.textSnackbar = 'Hubo un error al crear los datos'
        vm.showSnackbar = true
        vm.colorSnackbar = 'background-color: darkred'
      },
      // vm.element.nombre = '',
      // vm.element.rut = '',
      vm.showDialogCreate = false
      )
    }
  },
  mounted () {
    let vm = this
    vm.loadVolacanes()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
