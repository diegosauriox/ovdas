<template>
  <div class="">
    <md-table v-model="estaciones" md-sort="nombre" md-sort-order="asc" md-card md-fixed-header>
      <md-table-toolbar>
        <div class="md-toolbar-section-start">
          <h1 class="md-title">Estaciones</h1>
          <div class="md-layout-item">
              <md-button class="md-raised bh-primary" @click="showDialogCreate = true">
                Nueva Estacion
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
        <md-button class="bh-primary md-raised"  @click="showDialogCreate = true">Crear nueva Estacion</md-button>
      </md-table-empty-state>
      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID" md-sort-by="id_estacion" md-numeric>{{ item.id_estacion }}</md-table-cell>
        <md-table-cell md-label="Nombre" md-sort-by="nombre">{{ item.nombre }}</md-table-cell>
        <md-table-cell md-label="altura" md-sort-by="altura">{{ item.altura }}</md-table-cell>
        <md-table-cell md-label="Latitu" md-sort-by="latitud">{{ item.latitud }}</md-table-cell>
        <md-table-cell md-label="Longitud" md-sort-by="longitud">{{ item.longitud }}</md-table-cell>
        <md-table-cell md-label="Acciones">
          <md-button class="md-icon-button bh-info md-primary md-raised" @click="showInfo(item)">
            <md-icon>visibility</md-icon>
          </md-button>
          <md-button class="md-icon-button bh-warning md-primary md-raised" @click="elementAuxEdit(item)">
            <md-icon>edit</md-icon>
          </md-button>
          <md-button class="bh-danger md-icon-button" @click="elementAuxDelet(item.id_estacion)">
            <md-icon>cancel</md-icon>
          </md-button>
        </md-table-cell>
      </md-table-row>
    </md-table>
    <div class="">
      <md-dialog class="bh-scroll-y" :md-active.sync="showDialogCreate">
        <md-dialog-title>Nuevo</md-dialog-title>
        <md-dialog-content class="">
        <form>
          <md-field class="md-form-group">
            <md-icon>list_alt</md-icon>
            <label>Id Estacion...</label>
            <md-input v-model="element.id_estacion" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>title</md-icon>
            <label>Nombre...</label>
            <md-input v-model="element.nombre" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <label>Sensor...</label>
            <md-textarea class="bh-pd2" v-model="element.sensor" aria-required="required"></md-textarea>
          </md-field>
          <md-field class="md-form-group">
            <md-icon>height</md-icon>
            <label>Periodo...</label>
            <md-input v-model="element.periodo" type="number" aria-required="required" />
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
          <md-field class="md-form-group">
            <md-icon>add_location</md-icon>
            <label>Altura...</label>
            <md-input v-model="element.altura" type="number" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>add_location</md-icon>
            <label>Volcan...</label>
            <md-select v-model="element.volcan" name="volcan"  placeholder="Volcán">
              <md-option v-for="volcan in volcanes" v-bind:key="volcan.id_volcan" :value="volcan.id_volcan">{{ volcan.nombre }}</md-option>
            </md-select>
          </md-field>
          <md-field class="md-form-group">
            <md-icon>add_location</md-icon>
            <label>Distancia al cráter...</label>
            <md-input v-model="element.distancia_crater" type="number" aria-required="required" />
          </md-field>
        </form>
        </md-dialog-content>
        <md-dialog-actions>
          <md-button class="bh-danger" @click="showDialogCreate = false">cancelar</md-button>
          <md-button class="bh-success" @click="newElement(element)">Crear</md-button>
        </md-dialog-actions>
      </md-dialog>
      <md-snackbar
      md-position="center"
      :style="colorSnackbar"
      :md-duration="timeout"
      :md-active.sync="showSnackbar"
      md-persistent
    >
      <span>{{textSnackbar}}</span>
      <md-button class="md-danger bh-text-white" @click="showSnackbar = false">x</md-button>
    </md-snackbar>
    </div>
    <div>
      <md-dialog class="bh-scroll-y" :md-active.sync="showDialogEdit">
        <md-dialog-title>Actualizar</md-dialog-title>
        <md-dialog-content class="">
        <form>
          <md-field class="md-form-group">
            <md-icon>list_alt</md-icon>
            <label>Id Estación...</label>
            <md-input v-model="elementAux.id_estacion" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>title</md-icon>
            <label>Nombre...</label>
            <md-input v-model="elementAux.nombre" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <label>Descripción...</label>
            <md-textarea class="bh-pd2" v-model="elementAux.descripcion" aria-required="required"></md-textarea>
          </md-field>
          <md-field class="md-form-group">
            <md-icon>height</md-icon>
            <label>Altura...</label>
            <md-input v-model="elementAux.altura" type="number" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>add_location</md-icon>
            <label>Latitud...</label>
            <md-input v-model="elementAux.latitud" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>add_location</md-icon>
            <label>Latitud...</label>
            <md-input v-model="elementAux.longitud" type="text" aria-required="required" />
          </md-field>
        </form>
        </md-dialog-content>
        <md-dialog-actions>
          <md-button class="bh-danger" @click="showDialogCreate = false">Cancelar</md-button>
          <md-button class="bh-success" @click="editSaveElement(elementAux)">Actualizar</md-button>
        </md-dialog-actions>
      </md-dialog>
    </div>
    <div>
      <div class="">
      <md-dialog class="" :md-active.sync="showDialogDelete">
        <md-dialog-title>¿Estas seguro de relizar esta acción?</md-dialog-title>
        <md-dialog-content class="">
          <p>Se eliminara una <strong>Estación</strong> para siempre</p>
        </md-dialog-content>
        <md-dialog-actions>
          <md-button class="bh-danger" @click="showDialogDelete = false">Cancelar</md-button>
          <md-button class="bh-default" @click="deleteElement()">Eliminar</md-button>
        </md-dialog-actions>
      </md-dialog>
      <div class="">
        <md-dialog class="" :md-active.sync="ShowDialogInfo">
          <md-dialog-title>Detalles de <strong>{{elementAux.nombre}}</strong></md-dialog-title>
          <md-dialog-content>
            <p>{{elementAux.descripcion}}</p>
          </md-dialog-content>
          <md-dialog-actions>
            <md-button class="bh-success" @click="ShowDialogInfo = false">Ok</md-button>
          </md-dialog-actions>
        </md-dialog>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import { allVolcanesIDService } from '@/services/volcanes/GetAllVolcanesID.service'
import { allEstacionesService } from '@/services/estaciones/GetAllEstaciones.service'
import { createEstacionService } from '@/services/estaciones/CreateEstacion.service'
import { deleteEstacionService } from '@/services/estaciones/DeleteEstacion.service'
import { updateEstacionService } from '@/services/estaciones/UpdateEstacion.service'

export default {
  name: 'Estaciones',
  data () {
    return {
      msg: 'prueba inicial de datos',
      estaciones: [],
      volcanes: [],
      imagen: '',
      showDialogCreate: false,
      showSnackbar: false,
      textSnackbar: '',
      colorSnackbar: '',
      timeout: 4000,
      bancos: [],
      showDialogUpdate: false,
      showDialogDelete: false,
      showDialogEdit: false,
      ShowDialogInfo: false,
      auxElementDelete: -1,
      search: '',
      element: {},
      elementAux: {}
    }
  },
  methods: {
    loadEstaciones () {
      let vm = this
      allEstacionesService.query().then(data => {
        vm.estaciones = data.body
      })
    },
    loadVolacanes () {
      let vm = this
      allVolcanesIDService.query().then(data => {
        vm.volcanes = data.body
        console.log(vm.volcanes)
      })
    },
    newElement (model) {
      let vm = this
      console.log(model)
      createEstacionService.save(model).then(data => {
        vm.estaciones = data.body
        vm.textSnackbar = 'El campo fue creado con éxito'
        vm.showSnackbar = true
        vm.colorSnackbar = 'background-color: green'
        vm.loadEstaciones()
      },
      response => {
        vm.textSnackbar = 'Hubo un error al crear los datos'
        vm.showSnackbar = true
        vm.colorSnackbar = 'background-color: darkred'
      },
      // vm.element.nombre = '',
      // vm.element.rut = '',
      vm.element = {},
      vm.showDialogCreate = false
      )
    },
    showInfo (model) {
      let vm = this
      vm.elementAux = model
      vm.ShowDialogInfo = true
    },
    elementAuxEdit (model) {
      let vm = this
      vm.elementAux = model
      vm.showDialogEdit = true
    },
    editSaveElement (model) {
      let vm = this
      console.log(model)
      updateEstacionService.update(model.id_estacion, model).then(data => {
        vm.estaciones = data.body
        vm.textSnackbar = 'El campo fue actualizado con éxito'
        vm.showSnackbar = true
        vm.colorSnackbar = 'background-color: green'
        vm.loadEstaciones()
      },
      response => {
        vm.textSnackbar = 'Hubo un error al actualizar los datos'
        vm.showSnackbar = true
        vm.colorSnackbar = 'background-color: darkred'
      },
      // vm.element.nombre = '',
      // vm.element.rut = '',
      vm.elementAux = {},
      vm.showDialogEdit = false
      )
    },
    elementAuxDelet (id) {
      let vm = this
      vm.auxElementDelete = id
      vm.showDialogDelete = true
    },
    deleteElement () {
      let vm = this
      deleteEstacionService.destroy(vm.auxElementDelete).then(data => {
        vm.textSnackbar = 'El campo fue creado con eliminado con Exito'
        vm.showSnackbar = true
        vm.colorSnackbar = 'background-color: green'
        vm.loadEstaciones()
      },
      response => {
        vm.textSnackbar = 'Hubo un error al aliminar el estacion'
        vm.showSnackbar = true
        vm.colorSnackbar = 'background-color: darkred'
      },
      vm.showDialogDelete = false,
      vm.auxElementDelete = -1
      )
    }
  },
  mounted () {
    let vm = this
    vm.loadEstaciones()
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
