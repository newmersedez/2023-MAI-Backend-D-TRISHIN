import json
import random
from datetime import datetime
from uuid import uuid4

import bcrypt
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from .models import Profile, Product, Order


def main_view(request):
    return render(request, 'main_template.html', {})


# region Profile

@require_http_methods(["GET"])
def get_profiles(request, query):
    profiles = Profile.objects.all().filter(email__icontains='query').values('id', 'email', 'registration_date')
    return JsonResponse(list(profiles), safe=False)

@require_http_methods(["GET"])
def get_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    if profile is None:
        return HttpResponseNotFound('Профиль не найден')

    response = {
        'id': profile.id,
        'email': profile.email,
        'registration_date': profile.registration_date
    }

    return JsonResponse(response, safe=False)

@require_http_methods(["POST"])
def create_profile(request):
    data = json.loads(request.body)
    email = data.get('email'),
    password = data.get('password')

    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password, salt)

    profile = Profile.objects.create(email=email, password_hash=password_hash, registration_date=datetime.utcnow())

    return JsonResponse(profile.id, safe=False)

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
