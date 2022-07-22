from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerCreate, AnswerList, AnswerUpdateDelete
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('question', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('question/<slug:slug>/answercreate/', AnswerCreate.as_view()),
    path('question/<slug:slug>/answers/', AnswerList.as_view()),
    path('answers/<int:pk>/', AnswerUpdateDelete.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
