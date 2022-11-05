from django.shortcuts import render, redirect
from django.views import View
from burgery.models import Product
from burgery.forms import AddNewProductForm


class ShowAllProducts(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'ShowAllBurgers.html', {product: 'product'})

class AddProduct(View):
    def get(self,request):
        form = AddNewProductForm()
        return render(request, 'form.html', {'form':form})
    def post(self, request):
        form = AddNewProductForm()
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {'form':form})