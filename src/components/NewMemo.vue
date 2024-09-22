<template>
  <div class="new-memo">
    <form @submit.prevent="submitMemo">
      <label for="title" class="form-label">제목</label><br/>
      <input 
        type="text" 
        v-model="memo.title" 
        id="title" 
        class="form-control" 
        required
      /><br/>

      <label for="content" class="form-label">메모 내용</label><br/>
      <input 
        v-model="memo.content" 
        id="content" 
        class="form-control content" 
        required 
        placeholder="메모 내용을 입력하세요."
      />

      <button type="submit" class="btn btn-primary">
        {{ isEdit ? '수정하기' : '저장하기' }}
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    // props로 memo 데이터를 받고, 수정 모드인지 여부도 받기
    existMemo: {
      type: Object,
      default: () => ({ title: '', content: '' })
    },
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      memo: { ...this.existMemo }  // memo를 props로 받은 axiosMemo로 초기화
    };
  },
  watch: {
    // existMemo가 변경되면 memo 값도 업데이트
    existMemo(newMemo) {
      this.memo = {...newMemo}
    }
  },
  methods: {
    async submitMemo() {
      try {
        if (this.isEdit) {
          // 메모 수정하는 PUT 요청
          const response = await axios.put(`http://localhost:8000/api/memos/${this.memo.id}/`, this.memo);
          console.log('메모 수정 성공:', response);
          alert('성공적으로 메모가 수정되었습니다.')
          this.$router.push('/');
        } else {
          // 새 메모 작성하는 POST 요청
        const response = await axios.post('http://localhost:8000/api/memos/', this.memo);
        console.log('새 메모 작성 성공:', response);
        alert('성공적으로 메모가 작성되었습니다.')
        }
        this.$router.push('/');
      } catch (error) {
        console.error('메모 처리 중 오류 발생:', error);
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