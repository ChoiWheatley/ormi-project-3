from rest_framework.routers import DefaultRouter

from users.views import MemberViewSet

router = DefaultRouter()
router.register(r"users", MemberViewSet, basename="user")
urlpatterns = router.urls
