from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ProductDetailsView, ProductListView, contacts, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, UnpublishProductView, ProductCategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailsView.as_view()), name='product'),
    path("new/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("unpublish/<int:pk>/", UnpublishProductView.as_view(), name="unpublish_product"),
    path("category_products/<int:pk>/", ProductCategoryListView.as_view(), name="category_products"),
]
