import datetime
import random
from uuid import uuid4

from django.http import JsonResponse
from django.shortcuts import render

from django.views.decorators.http import require_http_methods

def main_view(request):
    return render(request, 'main_template.html', {})

# region Profile

@require_http_methods(["GET"])
def get_current_profile_details(request):
    profile = {
        'id': uuid4(),
        'email': 'ozon671games@mail.ru',
        'registration_date': datetime.datetime.utcnow(),
        'money': '10$'
    }
    return JsonResponse(profile)

@require_http_methods(["POST"])
def create_profile(request):
    user_id = uuid4()
    return JsonResponse(user_id)

# endregion

# region Product

@require_http_methods(["GET"])
def get_products(request):
    products = [
        {
            'id': uuid4(),
            'name': f'Product{i}',
            'created_by': uuid4(),
            'description': 'very cool product',
            'price': f'{random.randint(1, 10)}'
        } for i in range(random.randint(1, 3))
    ]
    return JsonResponse(products, safe=False)

@require_http_methods(["GET"])
def get_product(request, product_id):
    product = {
        'id': uuid4(),
        'name': f'Product 1',
        'created_by': uuid4(),
        'description': 'very cool product',
        'price': f'{random.randint(1, 10)}'
    }
    return JsonResponse(product, safe=False)

@require_http_methods(["POST"])
def create_product(request):
    user_id = uuid4()
    return JsonResponse(user_id)

# endregion

# region Order

@require_http_methods(["GET"])
def get_orders(request):
    products = [
        {
            'id': uuid4(),
            'name': f'Product{i}',
            'created_by': uuid4(),
            'description': 'very cool product',
            'price': f'{random.randint(1, 10)}'
        } for i in range(random.randint(1, 3))
    ]
    return JsonResponse(products, safe=False)

@require_http_methods(["POST"])
def create_order(request):
    user_id = uuid4()
    return JsonResponse(user_id)

# endregion
