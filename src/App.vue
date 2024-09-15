<template>
  <nav>
    <router-link to="/">Home</router-link> | 
    <router-link to="/create">메모 작성</router-link>
  </nav>
  <router-view/>
</template>

<style>
  nav {
    margin-bottom: 20px;
  }
</style>
