from ecommerce.models import Product
from typing import Union

class ProductManager:
    def get_products_list(self, filter_by: Union[str, None])-> list:
        if not filter_by:
            return Product.objects.all()
        filtered_list = eval(f"self.get_products_list_filtered_by_{filter_by}()")
        return filtered_list

    def get_products_list_filtered_by_price(self):
        return Product.objects.all().order_by('price')

    def get_products_list_filtered_by_price_rev(self):
        return Product.objects.all().order_by('-price')

    def get_products_list_filtered_by_score(self):
        return Product.objects.all().order_by('-score')

    def get_products_list_filtered_by_score_rev(self):
        return Product.objects.all().order_by('score')

    def get_products_list_filtered_by_name(self):
        return Product.objects.all().order_by('name')

    def get_products_list_filtered_by_name_rev(self):
        return Product.objects.all().order_by('-name')
