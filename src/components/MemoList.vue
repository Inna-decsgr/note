<template>
  <div class="memo-list">
    <ul v-if="memos.length">
      <li v-for="memo in memos" :key="memo.id" @click="handleClick(memo)" class="d-flex justify-content-between align-items-center">
        <div class="flex-grow-1 me-3">
          <span class="memo-title">
            {{ memo.title }} <span v-if="memo.is_locked">🔒</span>
          </span>

          <!--비밀번호 입력 폼 표시 여부-->
          <div v-if="memo.is_locked && isPasswordFormVisible[memo.id]">
            <p>이 메모는 잠금된 메모입니다. 비밀번호를 입력해주세요.</p>
            <input 
              type="password" 
              v-model="passwords[memo.id]" 
              placeholder="비밀번호를 입력해주세요"
            >
            <button @click="unlockMemo(memo)">확인</button>
            <p v-if="error">{{ error }}</p>
          </div>

          <!-- 비밀전호를 입력하지 않으면 내용 숨김-->
          <p v-else class="memo-content">
            {{ memo.content }}
          </p>
          <span class="memo-date">{{ formatDate(memo.created_at) }}</span>
        </div>
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
  data() {
    return {
      passwords: {},
      error: '',
      // 메모별로 비밀번호 입력 폼 표시 여부를 관리하는 객체
      isPasswordFormVisible: {},
    }
  },
  methods: {
    getCsrfToken() {
      const csrfCookie = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='));
      
      if (csrfCookie) {
        return csrfCookie.split('=')[1];  // 'csrftoken=' 이후의 값을 반환
      } else {
        return null;  // CSRF 토큰을 찾지 못하면 null 반환
      }
    },
    mounted() {
      // CSRF 토큰을 초기 설정에 추가
      axios.defaults.headers.common['X-CSRFToken'] = this.getCsrfToken();
    },
    handleClick(memo) {
      if (memo.is_locked) {
        this.showPasswordForm(memo);
      } else {
        this.gotoDetail(memo);
      }
    },
    // 잠금된 메모를 클릭하면 비밀번호 입력 폼을 표시
    showPasswordForm(memo) {
      this.isPasswordFormVisible[memo.id] = true;
      this.error = '';
      this.password = '';
    },
    // 서버에 비밀번호를 전송해서 잠금 해제 요청
    async unlockMemo(memo) {
      const csrfToken = this.getCsrfToken();
      console.log('CSRF Token:', csrfToken);
      console.log('Password:', this.passwords[memo.id]);

      try {
        console.log('CSRF Token:', this.csrfToken);
        console.log('Password:', this.passwords[memo.id]);

        const response = await axios.post(`http://localhost:8000/api/memos/${memo.id}/view/`, {
          password: this.passwords[memo.id],  // 메모ID에 해당하는 비밀번호 사용
        }, {
          headers: {
            'X-CSRFToken': csrfToken,
          },
          withCredentials: true
        });

        // 서버 응답 처리
        const data = response.data;
        memo.content = data.content;
        this.isPasswordFormVisible[memo.id] = false;  // 잠금 해제 시 촘 숨김
        this.passwords[memo.id] = '';  // 비밀번호 입력 필드 초기화
        this.error = '';  // 오류 메시지 초기화

        // 비밀번호가 올바르면 상세 페이지로 이동
        this.gotoDetail(memo);  // 상세 페이지로 이동
      } catch (error) {
        if (error.response && error.response.status === 403) {
          this.error = error.response.data.error;  // 비밀번호 틀림
        } else {
          console.error('잠금 해제 오류:', error);
          this.error = '서버 오류가 발생했습니다.'; // 서버 오류 처리
        }
      }
    },
    formatDate(createdAt) {
      return formatDate(createdAt);
    },
    gotoDetail(memo) {
      this.$router.push({
        path: '/detail',
        query: {
          memo: JSON.stringify(memo)  // memo 객체를 JSON 문자열로 변환하여 전송
        }
      })
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