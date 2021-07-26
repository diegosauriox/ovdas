<template>
  <div class="hello">
    <md-content class="" style="height:7rem;">
      <h1 class="">Carga de datos masivos por CSV</h1>
    </md-content>
    <div class="md-card drag bh-yellow" v-cloak @drop.prevent="addFile" @dragover.prevent md-with-hover>
      <h2>Identificacion de Señal</h2>
      <ul>
        <li v-for="file in identificacionSenal" v-bind:key="file.name">
          {{ file.name }}  <button class="remove-button" @click="removeFile(file)" title="Remove">X</button>
        </li>
      </ul>
      <md-button class="md-raised bh-text-black"  :disabled="uploadDisabled" @click="upload">Cargar</md-button>
    </div>
    <div class="md-card drag bh-rose" v-cloak @drop.prevent="addLocacaliCSV" @dragover.prevent md-with-hover>
      <h2>Localizaciones</h2>
      <ul>
        <li v-for="file in localizaciones" v-bind:key="file.name">
          {{ file.name }} ({{ file.size | kb }} kb) <button class="remove-button" @click="removeFile(file)" title="Remove">X</button>
        </li>
      </ul>
      <md-button class="md-raised bh-text-black"  :disabled="uploadLocaliDisabled" @click="uploadLocalizacion">Cargar</md-button>
    </div>
    <div class="md-card drag bh-teal" v-cloak @drop.prevent="addFile" @dragover.prevent md-with-hover>
      <h2>Registro Avistamineto</h2>
      <ul>
        <li v-for="file in registroAvistamiento" v-bind:key="file.name">
          {{ file.name }} <button class="remove-button" @click="removeFile(file)" title="Remove">X</button>
        </li>
      </ul>
      <md-button class="md-raised bh-text-black"  :disabled="uploadDisabled" @click="upload">Cargar</md-button>
    </div>
    <md-toolbar v-bind:class="[isActive ? activeClass: inactiveClass]" style="bottom:20%; position:absolute; background-color:darkred;">
      <h3 class="md-subheder bh-text-white" style="flex: 1">{{error + ' Asegurate de que el archivo este con el formato recomendado, puedes ver detalle del error en la consola'}}</h3>
      <md-button class="md-danger bh-text-white" @click="isActive = false">x</md-button>
    </md-toolbar>
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
</template>

<script>
import { loadVolcanService } from '@/services/dataset/LoadVolcanes.service'
import { loadLocalizacionService } from '@/services/dataset/LoadLocalizaciones.service'

export default {
  name: 'HelloWorld',
  data () {
    return {
      isActive: false,
      activeClass: 'activeClass',
      inactiveClass: 'inactiveClass',
      msg: 'prueba inicial de datos',
      trazas: [],
      imagen: '',
      files: [],
      localizaciones: [],
      registroAvistamiento: [],
      identificacionSenal: [],
      showDialogCreate: false,
      showSnackbar: false,
      textSnackbar: '',
      colorSnackbar: '',
      timeout: 4000,
      error: '',
      showError: false
    }
  },
  filters: {
    kb (val) {
      return Math.floor(val / 1024)
    }
  },
  computed: {
    uploadDisabled () {
      return this.files.length === 0
    },
    uploadLocaliDisabled () {
      return this.localizaciones.length === 0
    }
  },
  methods: {
    addFile (e) {
      e.preventDefault()
      console.log(e.dataTransfer.files)
      let droppedFiles = e.dataTransfer.files
      if (!droppedFiles) return
      ([...droppedFiles]).forEach(f => {
        this.files.push(f)
      })
    },
    addLocacaliCSV (e) {
      e.preventDefault()
      console.log(e.dataTransfer.files)
      let droppedFiles = e.dataTransfer.files
      if (!droppedFiles) return
      ([...droppedFiles]).forEach(f => {
        this.localizaciones.push(f)
      })
    },
    removeFile (file) {
      this.files = this.files.filter(f => {
        return f !== file
      })
    },
    upload () {
      let vm = this
      let formData = new FormData()
      this.files.forEach((f, x) => {
        console.log('ascacs', f)
        formData.append('file' + (x + 1), f)
      })
      fetch('https://httpbin.org/post', {
        method: 'POST',
        body: formData
      })
        .then(res => res.json())
        .then(res => {
          loadVolcanService.save(res.files).then(data => {
            vm.textSnackbar = 'El campo fue creado con éxito'
            vm.showSnackbar = true
            vm.colorSnackbar = 'background-color: green'
          },
          response => {
            let info = response
            console.log('respuesta' + info)
            vm.textSnackbar = response.statusText
            vm.showSnackbar = true
            vm.colorSnackbar = 'background-color: darkred'
          })
        })
        .catch(e => {
          console.error(JSON.stringify(e.message))
        })
    },
    uploadLocalizacion () {
      let vm = this
      let formData = new FormData()
      this.localizaciones.forEach((f, x) => {
        formData.append('file' + (x + 1), f)
      })
      fetch('https://httpbin.org/post', {
        method: 'POST',
        body: formData
      })
        .then(res => res.json())
        .then(res => {
          loadLocalizacionService.save(res.files).then(data => {
            vm.textSnackbar = 'Correctamente cargado los datos'
            vm.showSnackbar = true
            vm.colorSnackbar = 'background-color: green'
          },
          response => {
            console.log(response)
            vm.textSnackbar = 'Error al cargar los datos'
            vm.showSnackbar = true
            vm.colorSnackbar = 'background-color: darkred'
            vm.error = response.statusText
            vm.isActive = true
          })
        })
        .catch(e => {
          console.error(JSON.stringify(e.message))
        })
    },
    uploadIdentificacion () {
      let formData = new FormData()
      this.localizaciones.forEach((f, x) => {
        formData.append('file' + (x + 1), f)
      })
      fetch('https://httpbin.org/post', {
        method: 'POST',
        body: formData
      })
        .then(res => res.json())
        .then(res => {
          loadLocalizacionService.save(res.files).then(data => {
          },
          response => {
            console.log('error otra ves')
          })
        })
        .catch(e => {
          console.error(JSON.stringify(e.message))
        })
    },
    uploadRegistro () {
      let formData = new FormData()
      this.localizaciones.forEach((f, x) => {
        formData.append('file' + (x + 1), f)
      })
      fetch('https://httpbin.org/post', {
        method: 'POST',
        body: formData
      })
        .then(res => res.json())
        .then(res => {
          loadLocalizacionService.save(res.files).then(data => {
          },
          response => {
            console.log('error otra ves')
          })
        })
        .catch(e => {
          console.error(JSON.stringify(e.message))
        })
    }
  },
  mounted () {
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
.drag:hover {
    z-index: 2;
    box-shadow: 0 5px 5px -3px rgba(0,0,0,.2), 0 8px 10px 1px rgba(0,0,0,.14), 0 3px 14px 2px rgba(0,0,0,.12);
}
.remove-button {
    background: #fff;
    color: #37474F;
    border: none;
    cursor: pointer;
}
.remove-button:hover {
  box-shadow: 0 5px 5px -3px rgba(0,0,0,.2), 0 8px 10px 1px rgba(0,0,0,.14), 0 3px 14px 2px rgba(0,0,0,.12);
}
.md-card {
    width: 30%;
    height: 10%;
    margin: 4px;
    display: inline-block;
    vertical-align: top;
  }
  .activeClass {
    display: show;
  }
  .inactiveClass {
    display: none;
  }
</style>
