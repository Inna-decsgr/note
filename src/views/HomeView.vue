<template>
  <div class="home">
    <span class="title">메모 목록</span>
    <MemoList :memos="memos" />
  </div>
</template>

<script>
import axios from 'axios';
import MemoList from '@/components/MemoList.vue'

export default {
  components: {
    MemoList
  },
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

.title {
  font-weight: bold;
  font-size: 25px;
}
</style>