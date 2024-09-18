<template>
  <div class="memo-wrapper">
    <span class="title">새 메모 작성</span>
    <NewMemo />
  </div>
</template>

<script>
import NewMemo from '@/components/NewMemo.vue'

export default {
  components: {
    NewMemo
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
