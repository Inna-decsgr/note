from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import serializers, viewsets 
from .models import Memo

# MemoSerializer 정의
class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'

# MemoViewSet 정의
class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

# DefaultRouter를 사용하여 RESTful API의 URL을 자동으로 생성
router = DefaultRouter()
router.register(r'memos', MemoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
