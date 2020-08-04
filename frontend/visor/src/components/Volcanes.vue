<template>
  <div class="">
    <md-table v-model="volcanes" md-sort="nombre" md-sort-order="asc" md-card md-fixed-header>
      <md-table-toolbar>
        <div class="md-toolbar-section-start">
          <h1 class="md-title">Volcanes</h1>
        </div>

        <md-field md-clearable class="md-toolbar-section-end">
          <md-input placeholder="Buscar por nombre..." v-model="search" @input="searchOnTable" />
        </md-field>
      </md-table-toolbar>

      <md-table-empty-state
        md-label="No users found"
        :md-description="`No user found for this '${search}' query. Try a different search term or create a new user.`">
        <md-button class="md-primary md-raised" @click="newUser">Create New User</md-button>
      </md-table-empty-state>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID" md-sort-by="id" md-numeric>{{ item.id_volcan }}</md-table-cell>
        <md-table-cell md-label="Nombre" md-sort-by="name">{{ item.nombre }}</md-table-cell>
        <md-table-cell md-label="altura" md-sort-by="email">{{ item.altura }}</md-table-cell>
        <md-table-cell md-label="latitu" md-sort-by="gender">{{ item.latitud }}</md-table-cell>
        <md-table-cell md-label="longitud" md-sort-by="title">{{ item.longitud }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<script>
import { allVolcanesService } from '@/services/volcanes/GetAllVolcanes.service'

export default {
  name: 'Volcanes',
  data () {
    return {
      msg: 'prueba inicial de datos',
      volcanes: [],
      imagen: ''
    }
  },
  methods: {
    loadVolacanes () {
      let vm = this
      allVolcanesService.query().then(data => {
        vm.volcanes = data.body
        console.log(vm.volcanes)
      })
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
