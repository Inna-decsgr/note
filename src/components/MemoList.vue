<template>
  <div class="memo-list">
    <ul v-if="memos.length">
      <li v-for="memo in memos" :key="memo.id" class="d-flex justify-content-between align-items-center">
        <div class="flex-grow-1 me-3">
          <span class="memo-title">{{ memo.title }}</span>
          <p class="memo-content">{{ memo.content }}</p>
          <span class="memo-date">{{ formatDate(memo.created_at) }}</span>
        </div>
        <button @click="editmemo(memo)" class="btn btn-secondary custom-btn">메모 수정</button>
        <button @click="deletememo(memo.id)" class="btn btn-secondary custom-btn">삭제</button>
        <button class="starbutton btn btn-secondary custom-btn" @click="toggleBookmark(memo)">
          <font-awesome-icon :icon="memo.is_bookmark ? 'fas fa-star' : 'far fa-star'" />
        </button>
      </li>
    </ul>
    <p v-else>작성된 메모가 없습니다.</p>
  </div>
</template>


<script>
import axios from 'axios';
import { formatDate } from '@/utils/format';

export default {
  props: {
    memos: {
      type: Array,
      required: true
    }
  },
  methods: {
    formatDate(createdAt) {
      return formatDate(createdAt);
    },
    editmemo(memo) {
      // 수정 버튼을 클릭하면 memo 데이터를 가지고 /create 경로로 이동
      this.$router.push({
        path: '/create',
        query: { memoId: memo.id }
      });
      console.log('수정할 메모', memo);
    },
    async deletememo(memoId) {
      // 삭제 요청을 부모 컴포넌트에 전달, 부모 컴포넌트의 삭제 로직 실행시키도록
      this.$emit('delete-memo', memoId);
    },
    async toggleBookmark(memo) {
      try {
        const response = await axios.post(`http://localhost:8000/api/memos/${memo.id}/toggle_bookmark/`);
        memo.is_bookmark = response.data.is_bookmark;  // API 응답에 따라 즐겨찾기 상태 업데이트
      } catch (error) {
        console.error('즐겨찾기 토글 중 오류 발생:', error);
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

.memo-list .btn {
  margin-top: 0px;
  font-size: 12px;
}

.starbutton {
  outline: none;
  width: 40px !important;  
  margin-right: 0;
}

.memo-date {
  font-size: 12px;
  font-weight: bold;
  color:#9b9898
}


.custom-btn {
  width: 100px !important;
  line-height: 1 !important;
  margin-right: 5px !important;
}

</style>