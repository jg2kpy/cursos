from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet
# from .views import ArticleList

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<slug:slug>', article_details),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>', ArticlesDetails.as_view()),
    path('', include(router.urls))
]
