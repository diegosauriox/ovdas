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
