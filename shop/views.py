from django.shortcuts import render, get_object_or_404
from .models import Category, Product, UpCategory
from cart.forms import CartAddProductForm


#Страница с надкагориями
def UpCategoryList(request, upcategory_slug=None):
    upcategory = None
    upcategorys = UpCategory.objects.all()
    categories = Category.objects.filter()
    if upcategory_slug:
        upcategory = get_object_or_404(UpCategory, slug=upcategory_slug)
        categories = categories.filter(upcategory=upcategory)
    return render(request, 'shop/product/list.html', {
        'upcategory': upcategory,
        'upcategorys': upcategorys,
        'categories': categories
    })


# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

