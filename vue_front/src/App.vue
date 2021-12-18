<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <TablePage :defaultUrl="defaultUrl"></TablePage>
  </div>
</template>

<script>
import TablePage from "@/components/TablePage";

export default {
  name: 'App',
  components: {
    TablePage
  },
  data () {
    return {
      defaultUrl: 'http://127.0.0.1:8003/'
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
