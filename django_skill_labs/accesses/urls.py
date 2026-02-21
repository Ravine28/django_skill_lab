from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, SystemViewSet, AccessViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'systems', SystemViewSet)
router.register(r'accesses', AccessViewSet)

urlpatterns = router.urls