<template>
  <div id="app">
    <AdminHeader />
    <AdminContent />
    <AdminFooter />
  </div>
</template>

<script>
import AdminHeader from './components/AdminHeader.vue'
import AdminContent from './components/AdminContent.vue'
import AdminFooter from './components/AdminFooter.vue';

export default {
  name: 'App',
  components: {
    AdminHeader,
    AdminContent,
    AdminFooter
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
}


</style>
