<template>
  <div class="memo-detail">
    <h1>{{ memoData.title }}</h1>
    <p>{{ memoData.content }}</p>
    <span>{{ formatDate(memoData.created_at) }}</span>

    <div>
      <button @click="editmemo(memoData)" class="btn btn-secondary custom-btn">메모 수정</button>
      <button @click="deletememo(memoData.id)" class="btn btn-secondary custom-btn">삭제</button>
    </div>
  </div>
</template>



<script>
import { formatDate } from '@/utils/format';

export default {
  props: {
    memo: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      memoData: {} // props에서 받은 memo를 저장할 새로운 변수
    }
  },
  created() {
    // 쿼리에서 memo를 가져와서 JSON 파싱
    const memoString = this.$route.query.memo;
    if (memoString) {
      this.memoData = JSON.parse(memoString);  // JSON 문자열을 객체로 변환
    } else {
      this.memoData = this.memo;  /// props에서 memo가 전달된 경우
    }
  },
  methods: {
    formatDate(createdAt) {
      return formatDate(createdAt);
    },
    editmemo(memo) {
      this.$router.push({
        path: '/create',
        query: { memoId: memo.id }
      });
    },
    async deletememo(memoId) {
      // 삭제 요청을 부모 컴포넌트에 전달, 부모 컴포넌트의 삭제 로직 실행시키도록
      this.$emit('delete-memo', memoId);
    },
  }
}
</script>