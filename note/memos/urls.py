from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import serializers, viewsets 
from .models import Memo
from . import views

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
    path('', include(router.urls)),  # API 경로를 router.urls로 연결
    path('memos/', views.memo_list, name='memo-list'),
    path('memos/<int:memo_id>/toggle_bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
]
