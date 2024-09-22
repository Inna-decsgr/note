<template>
  <div class="memo-list">
    <ul v-if="memos.length">
      <li v-for="memo in memos" :key="memo.id">
        <span class="memo-title">{{ memo.title }}</span>
        <p class="memo-content">{{ memo.content }}</p>
        <button @click="editmemo(memo)">메모 수정</button>
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
  },
  methods: {
    editmemo(memo) {
      // memo 데이터를 가지고 /create 경로로 이동
      this.$router.push({
        path: '/create',
        query: { memoId: memo.id }
      });
      console.log('수정할 메모', memo);
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