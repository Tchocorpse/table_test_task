<template>
  <section v-if="errored_load">
    <p>Something gone wrong. Cannot reach or get backend data.</p>
  </section>

  <section v-else>
    <div v-if="loading_load">Loading...</div>

    <div v-else>
      <select name="category_id" @change="onChangeCol($event)" class="form-control">
        <option></option>
        <option value="name">Name</option>
        <option value="quantity">Quantity</option>
        <option value="distance">Distance</option>
      </select>
      <select name="category_id" @change="onChangeLog($event)" class="form-control">
        <option></option>
        <option value="equal">EQUAL</option>
        <option value="more">MORE</option>
        <option value="less">LESS</option>
        <option value="contains">CONTAINS</option>
      </select>
      <input v-model="filter_value " @change="onChangeVal($event)"/>
      <table style="width:100%">
        <tr>
          <td>
            Id
          </td>
          <td>
            Name
          </td>
          <td>
            Date
          </td>
          <td>
            Quantity
          </td>
          <td>
            Distance
          </td>
        </tr>

        <tr v-for="row in loaded_table.data.table" v-bind:key="row.id">
          <td>
            {{ row.id }}
          </td>
          <td>
            {{ row.name }}
          </td>
          <td>
            {{ row.date }}
          </td>
          <td>
            {{ row.quantity }}
          </td>
          <td>
            {{ row.distance }}
          </td>
        </tr>
      </table>

    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TablePage',
  props: {
    defaultUrl: {
      type: String
    },
  },
  data () {
    return {
      loaded_table: Object,
      delete_response: 'Nothing',
      loading_load: true,
      errored_load: false,
      filter_col: '',
      filter_logic: '',
      filter_value: '',
      limit: 20,
      offset: 0,
      total: 0,
    }
  },
  mounted () {
    this.loadTable()
  },
  methods: {
    loadTable: function () {
      axios
        .get(this.defaultUrl + 'table/', {params: {
          'col': this.filter_col,
          'logic': this.filter_logic,
          'value': this.filter_value,
          // 'limit': this.limit,
          'limit': this.total,
          'offset': this.offset,
        }})
        .then(response => (this.loaded_table = response))
        .then(this.total = this.loaded_table.total)
        .catch(error => {
          console.log(error)
          this.errored_load = true
        })
        .finally(() => (this.loading_load = false))
    },
    onChangeCol(event) {
      this.filter_col = event.target.value
      this.loadTable()
    },
    onChangeLog(event) {
      this.filter_logic = event.target.value
      this.loadTable()
    },
    onChangeVal(event) {
      event.preventDefault()
      this.loadTable()
    }
  }
}
</script>

<style scoped>
  table, th, td {
    border: 1px solid black;
  }

</style>