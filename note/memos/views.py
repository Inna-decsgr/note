from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Memo
from .serializers import MemoSerializer
from django.shortcuts import get_object_or_404
import json

@api_view(['GET'])
def memo_list(request):
    memos = Memo.objects.all()
    serializer = MemoSerializer(memos, many=True)
    return Response(serializer.data)


# 즐겨찾기 토글 기능
@api_view(['POST'])
def toggle_bookmark(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)  # 메모가 없으면 404 응답
    memo.is_bookmark = not memo.is_bookmark  # 즐겨찾기 상태 반전
    memo.save()
    return JsonResponse({'is_bookmark': memo.is_bookmark})  # 새로운 상태 반환

# 새 메모 작성
def create_memo(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # JSON 데이터 로드
        title = data.get('title')
        content = data.get('content')
        is_locked = data.get('is_locked', False)  # 기본값 False
        is_bookmark = data.get('is_bookmark', False) 
        password = data.get('password')

        # 메모 생성
        memo = Memo.objects.create(title=title, content=content, is_locked=is_locked, is_bookmark=is_bookmark, password=password)

        return JsonResponse({
            'id': memo.id, 
            'title': memo.title, 
            'content': memo.content, 
            'is_locked': memo.is_locked,
            'is_bookmark': memo.is_bookmark,
            'created_at': memo.created_at
        }, status=201)

    return JsonResponse({'error': 'Invalid method'}, status=405)


# 메모 조회
def view_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if memo.is_locked:
        entered_password = request.POST.get('password')
        if entered_password != memo.password:
            return JsonResponse({"error": "비밀번호가 틀렸습니다."}, status=403)
    return JsonResponse({"title": memo.title, "content": memo.content})