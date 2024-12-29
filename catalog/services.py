from catalog.models import Product


def get_products_list_by_category(category_id):
    """Возвращает список всех продуктов в указанной категории"""
    products_by_category = Product.objects.filter(category_id=category_id)

    if not products_by_category:
        products_by_category = None

    return products_by_category
