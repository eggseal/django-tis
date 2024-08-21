from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django import forms
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Me",
        })
        return context

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 150},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 1000},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 225},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 30}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        if int(id) - 1 not in range(len(Product.products)):
            return HttpResponseRedirect(reverse('home'))

        viewData = {}
        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)
    
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('The price must be greater than zero (0)')
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            Product.products.append({
                "id": len(Product.products) + 1,
                "name": name,
                "price": price,
                "description": "One of the products of all time"
            })
            return HttpResponseRedirect(reverse('success'))
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        
class ProductSuccessView(TemplateView):
    template_name = 'products/success.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Created Product"
        return render(request, self.template_name, viewData)
        
class ContactPageView(TemplateView):
    template_name = 'pages/contacts.html'

    def get_context_data(self, **kwargs: Any):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            "title": "Contact Us - Online Store",
            "subtitle": "Our contact information",
            "email": "service@onlinestore.com",
            "address": "Cra 1A #1-1",
            "phone": "+573000000000"
        })
        return ctx