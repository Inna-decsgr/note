// 날짜만 포맷하는 함수
export function formatDate(createdAt) {
  const date = new Date(createdAt);
  return date.toLocaleDateString('ko-KR', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
}
