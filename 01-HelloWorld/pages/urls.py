from django.urls import path
from .views import HomePageView, AboutPageView, ProductIndexView, ProductShowView, ProductCreateView, ContactPageView, ProductSuccessView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/success', ProductSuccessView.as_view(), name='success'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
]