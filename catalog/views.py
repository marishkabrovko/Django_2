from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def home(request):
    return render(request, template_name='home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо за обращение, {name}!")

    return render(request, template_name='contacts.html')


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name='product_list.html', context=context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, template_name='product_details.html', context=context)
