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
    // 페이지가 생성되자마자 할 일들
    // route의 쿼리로부터 memoId를 받아와서 변수에 저장
    const memoId = this.$route.query.memoId;
    if (memoId) {  // memoId가 존재한다는것은 이미 id를 부여받은 메모가 있다는 뜻 즉, 수정하고 싶은 메모가 있다는 뜻이므로 수정 모드를 true로 변경해준다
      this.isEdit = true;
      try {
        // 그리고 데이터를 가져오는 GET 요청을 보내는데 이때 어떤 메모를 가져올 지에 대한 메모의 memoId 정보를 함께 전송한다. 기존 메모 정보를 input 필드에 보여줄 때 필요하기 때문. 성공적으로 GET 요청이 완료되면 응답의 데이터를 this.memo에 다시 저장하고 NewMemo 컴포넌트에 existMemo로 전달한다. 수정 모드 여부와 함께!!
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
