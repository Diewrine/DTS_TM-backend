from rest_framework.routers import DefaultRouter
from .viewset import MemberViewSet

router = DefaultRouter()
router.register(r'member', MemberViewSet, basename='member')
#router.register(r'user', UserViewSet, basename='user')
urlpatterns = router.urls