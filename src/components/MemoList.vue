<template>
  <div class="memo-list">
    <ul v-if="memos.length">
      <li v-for="memo in memos" :key="memo.id">
        <span class="memo-title">{{ memo.title }}</span>
        <p class="memo-content">{{ memo.content }}</p>
      </li>
    </ul>
    <p v-else>작성된 메모가 없습니다.</p>
  </div>
</template>

<script>
export default {
  props: {
    memos: {
      type: Array,
      required: true
    }
  }
}
</script>


<style>
ul {
  padding: 0;
  margin: 0;
}

li {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.memo-list {
  margin-top: 20px;
}

.memo-title {
  font-weight: bold;
  font-size: 17px;
}

.memo-content {
  font-size: 13px;
  margin-top: 5px;
  height: 20px;
}
</style>