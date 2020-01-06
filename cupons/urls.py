from django.conf.urls import url
from .views import CuponApply

app_name = 'cupons'

urlpatterns = [
    url(r'^apply', CuponApply, name='apply')
]