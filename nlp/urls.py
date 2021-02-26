from rest_framework import routers
from .views import Word2VecViewSet


router = routers.DefaultRouter()
router.register(r'word2vec', Word2VecViewSet)