from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from customer_and_brand.serializers import MyUserViewSet, PlanViewSet, BrandPromotionViewSet, CustomerGoalsViewSet

router = routers.DefaultRouter()

router.register(r'users', MyUserViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'brand-promotions', BrandPromotionViewSet)
router.register(r'customer-goals', CustomerGoalsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
