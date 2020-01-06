from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'shop'

urlpatterns = [
    path("UpCategoryList/<slug:upcategory_slug>/", views.UpCategoryList, name="UpCategoryList"),
    path("ProductListByCategory/<slug:category_slug>/", views.ProductList, name="ProductListByCategory"),

    path("<int:id>/<slug:slug>/", views.ProductDetail, name="ProductDetail"),
    path("", views.UpCategoryList, name="UpCategoryList"),
    path("", views.ProductList, name="ProductListByCategory"),

]
