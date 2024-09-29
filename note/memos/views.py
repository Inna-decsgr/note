from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Memo
from .serializers import MemoSerializer
from django.shortcuts import get_object_or_404

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