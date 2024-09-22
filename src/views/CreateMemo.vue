<template>
  <div class="memo-wrapper">
    <span class="title">{{  isEdit ? '메모 수정하기' : '새 메모 작성' }}</span>
    <NewMemo :existMemo="memo" :isEdit="isEdit"/>
  </div>
</template>

<script>
import NewMemo from '@/components/NewMemo.vue';
import axios from 'axios';

export default {
  components: {
    NewMemo
  },
  data() {
    return {
      memo: { title: '', content: '' },
      isEdit: false
    }
  },
  async created() {
    const memoId = this.$route.query.memoId;
    if (memoId) {
      this.isEdit = true;
      try {
        const response = await axios.get(`http://localhost:8000/api/memos/${memoId}/`);
        this.memo = response.data;
      } catch (error) {
        console.error('메모를 불러오는 중 오류 발생:', error);
      }
    }
  }
}
</script>

<style>
.memo-wrapper {
  margin-top: 15px;
}

.title {
  font-weight: bold;
  font-size: 25px;
}
</style>
