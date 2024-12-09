from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, ListView

from .models import Product


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо за обращение, {name}!")

    return render(request, template_name='catalog/contacts.html')


class ProductListView(ListView):
    model = Product


class ProductDetailsView(DetailView):
    model = Product

