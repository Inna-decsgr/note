<template>
  <div>
    <h2>새 메모 작성</h2>
    <form @submit.prevent="submitMemo">
      <label for="title">제목</label>
      <input type="text" v-model="memo.title" id="title" required />

      <label for="content">메모 내용</label>
      <textarea v-model="memo.content" id="content" required></textarea>

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      memo: {
        title: '',
        content: ''
      }
    };
  },
  methods: {
    async submitMemo() {
      try {
        const response = await axios.post('http://localhost:8000/api/memos/', this.memo);
        console.log(response);
        alert('성공적으로 메모가 작성되었습니다.')
        this.$router.push('/');
      } catch (error) {
        console.error('새로운 메모를 작성하던 중 에러가 발생했습니다', error);
      }
    }
  }
}
</script>


<style>

</style>
