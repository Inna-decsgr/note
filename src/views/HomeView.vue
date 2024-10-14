<template>
  <div class="home">
    <span class="title">메모 목록</span>
    <MemoList :memos="memos"  @delete-memo="deleteMemo"/>
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
    },
    async deleteMemo(memoId) {
      // 사용자에게 확인을 요청하는 confirm() 함수 사용
      const isConfirmed = confirm('메모를 정말 삭제하시겠습니까?');
      if (isConfirmed) {
        try {
          // 확인을 누르면 실행된 메모 삭제 로직 추가
          const response = await axios.delete(`http://localhost:8000/api/memos/${memoId}/`);
          console.log('메모 삭제 성공:', response.data);

          // 필터링해서 memoId와 일치하지 않는 메모들만 memos에 담기 = 삭제할 메모 외의 메모들만 담긴다
          // 이때 상태 업데이트는 부모 컴포넌트에서 수행한다.props로 전달된 데이터를 자식 컴포넌트에서는 변경시킬 수 없기 때문에 삭제 로직은 부모 컴포넌트에서 작성
          // 작성한 로직을 자식 컴포넌트에게 전달하게 되면 자식 컴포넌트에서는 해당 로직이 필요한 시점에 emit을 통해 부모 컴포넌트의 함수를 호출해서 상태를 변경시킴
          this.memos = this.memos.filter(memo => memo.id !== memoId);
        } catch (error) {
          console.error('메모 삭제 중 오류 발생:', error);
        }
      } else {
        console.log('메모 삭제 취소');
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