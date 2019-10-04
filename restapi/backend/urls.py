from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('manufacturer', views.ManufacturerView)
router.register('shoetype', views.ShoeTypeView)
router.register('shoecolor', views.ShoeColorView)
router.register('shoe', views.ShoeView)

urlpatterns = [url('', include(router.urls))]
