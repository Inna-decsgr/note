from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Memo
from .serializers import MemoSerializer

@api_view(['GET'])
def memo_list(request):
    memos = Memo.objects.all()
    serializer = MemoSerializer(memos, many=True)
    return Response(serializer.data)
