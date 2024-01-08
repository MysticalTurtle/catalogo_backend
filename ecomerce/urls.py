from rest_framework import routers
from ecomerce.api import *

router = routers.DefaultRouter()

router.register('api/product',ProductViewSet,'product'),
# router.register(r'users', UserViewSet),
router.register('api/user', UserViewSet,'user')
urlpatterns = router.urls
