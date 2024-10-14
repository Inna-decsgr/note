<template>
  <div class="memo-detail">
    <div class="title-container">
      <div class="memotitle">
        <span class="detailtitle">{{ memoData.title }}</span>
        <span class="detaildate">{{ formatDate(memoData.created_at) }}</span>
      </div>
      <div class="button-group">
        <button @click="editmemo(memoData)" class="btn btn-secondary custom-btn">수정</button>
        <button @click="deletememo(memoData.id)" class="btn btn-secondary custom-btn">삭제</button>
      </div>
    </div>
    <p class="detailcontent">{{ memoData.content }}</p>
    <div class="homebutton">
      <button @click="gotoDetail(memo)" class="btn btn-secondary custom-btn">홈으로</button>
    </div>
  </div>
</template>



<script>
import { formatDate } from '@/utils/format';

export default {
  data() {
    return {
      memoData: {} // props에서 받은 memo를 저장할 새로운 변수
    }
  },
  created() {
    // 쿼리에서 memo를 가져와서 JSON 파싱
    const memoString = this.$route.query.memo;
    if (memoString) {
      try {
        this.memoData = JSON.parse(memoString);   // JSON 문자열을 객체로 변환
      } catch (error) {
        console.error('Memo 파싱 오류:', error);
        this.memoData = {};  // 오류 발생 시 기본값 설정
      }
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
    gotoDetail(memo) {
      this.$router.push({
        path: '/',
        query: {
          memo: JSON.stringify(memo)  // memo 객체를 JSON 문자열로 변환하여 전송
        }
      })
    },
  }
}
</script>

<style>
.memo-detail {
  display: flex;
  flex-direction: column;
}

.title-container {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.memotitle {
  display: flex;
  align-items: baseline;
}
.detailtitle {
  font-size: 30px;
  font-weight: bold;
  margin-right: 10px;
}

.button-group {
  display: flex;
}

.button-group button {
  margin-top: 0;
}

.detailcontent {
  font-size: 17px;
  padding: 35px 0 60px 0;
}

.detaildate{ 
  font-size: 13px;
  color: gray;
}

.homebutton {
  margin-top: auto;
  display: flex;
  justify-content: flex-end;
}
</style>