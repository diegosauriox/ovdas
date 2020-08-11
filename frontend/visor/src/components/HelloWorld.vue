<template>
  <div class="hello">
    <md-button class="md-primary">Primary</md-button>
    <md-button class="md-raised md-accent">Accent</md-button>
    <h1>{{ msg }}</h1>
    <md-button class="md-raised md-accent">Accent</md-button>
     <md-button
                slot="buttons"
                href="javascript:void(0)"
                class="md-just-icon md-simple md-white"
              >
                <i class="fab fa-google-plus-g"></i>
              </md-button>
    <md-button class="md-raised md-primary">Primary</md-button>
    <md-content class="md-accent">Accent</md-content>
    <div class="">
      <md-dialog :md-active.sync="showDialogCreate" style="width: 70% !important;" >
        <md-dialog-title>Nuevo</md-dialog-title>
        <div class="">
        <form>
          <md-field class="md-form-group">
            <md-icon>title</md-icon>
            <label>Nombre...</label>
            <md-input v-model="element.nombre" type="text" aria-required="required" />
          </md-field>
          <md-field class="md-form-group">
            <md-icon>text_format</md-icon>
            <label>Descripción...</label>
            <md-input v-model="element.rut" type="text" aria-required="required" />
          </md-field>
        </form>
        </div>
        <md-dialog-actions>
          <md-button class="button-danger" @click="showDialogCreate = false">cancelar</md-button>
          <md-button class="md-success" @click="newElement(element)">Crear</md-button>
        </md-dialog-actions>
      </md-dialog>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'prueba inicial de datos',
      trazas: [],
      imagen: ''
    }
  },
  methods: {
    loadtrazas () {
      let vm = this
      console.log(vm.msg)
    }
  },
  mounted () {
    let vm = this
    vm.loadtrazas()
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
