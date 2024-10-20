from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet

router_posts = DefaultRouter()

router_posts.register(r'posts', PostModelViewSet, basename='posts')