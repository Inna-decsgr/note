<template>
  <div>
    <h2>메모 목록</h2>
    <ul v-if="memos.length">
      <li v-for="memo in memos" :key="memo.id">
        <h3>{{ memo.title }}</h3>
        <p>{{ memo.content }}</p>
      </li>
    </ul>
    <p v-else>작성된 메모가 없습니다.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      memos: []
    };
  },
  async created() {
    await this.fetchMemos();
  },
  methods: {
    async fetchMemos() {
      try {
        const response = await axios.get('http://localhost:8000/api/memos/');
        this.memos = response.data;
      } catch (error) {
        console.error('메모 목록을 가져오던 중 에러가 발생했습니다', error);
      }
    }
  }
}
</script>