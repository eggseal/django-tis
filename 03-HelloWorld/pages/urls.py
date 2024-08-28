from django.urls import path
from .views import *
from .utils import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/success', ProductSuccessView.as_view(), name='success'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('cart/', CartView.as_view(), name='cart_index'), 
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'), 
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'), 
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'), 
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'), 
]