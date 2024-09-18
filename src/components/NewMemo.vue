<template>
  <div class="new-memo">
    <form @submit.prevent="submitMemo">
      <label for="title" class="form-label">제목</label><br/>
      <input type="text" v-model="memo.title" id="title" class="form-control" required /><br/>

      <label for="content" class="form-label">메모 내용</label><br/>
      <input 
        v-model="memo.content" 
        id="content" 
        class="form-control content" 
        required 
        placeholder="메모 내용을 입력하세요."
      />

      <button type="submit" class="btn btn-primary">Submit</button>
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
.new-memo {
  margin-top: 20px;
}

.form-label {
  font-weight: bold;
  font-size: 14px;
}

.content {
  height: 100px;
  overflow-y: auto;
}

.form-control::placeholder {
  font-size: 13px; /* Placeholder 텍스트 크기 조정 */
  color: #888; /* Placeholder 텍스트 색상 조정 */
}

.btn {
  width: 100%;
  margin-top: 40px;
}
</style>