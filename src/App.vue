<template>
  <div id="id" class="app-container">
    <div class="content-wrapper">
      <nav class="nav">
        <router-link to="/">Home</router-link>
        <router-link to="/create">메모 작성</router-link>
      </nav>
    <router-view/>
    </div>
  </div>
</template>

<style>
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.content-wrapper {
    position: relative; /* 상대적 위치 */
    width: 100%; 
    max-width: 700px;
    height: 700px;
    padding: 35px; 
    border: 1px solid #dee2e6; 
    border-radius: 8px;
    background-color: white; 
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    box-sizing: border-box;
    overflow: auto;
}

.nav {
  margin-bottom: 20px;
  text-align: left;
}

.nav a {
  color: black;
  font-weight: bold;
  text-decoration: none;
  margin: 0 20px 20px 0;
}

ol, ul {
  list-style: none;
  padding: 0 !important;  
  margin: 0;       
}
</style>
