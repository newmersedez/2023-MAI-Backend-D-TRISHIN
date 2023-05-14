import json
import random
from datetime import datetime
from uuid import uuid4

import bcrypt
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_http_methods

from .models import Profile, Product, Order


def main_view(request):
    return render(request, 'main_template.html', {})


# region Profile

@require_http_methods(["GET"])
def get_profiles(request):
    query = request.GET.get('email', '')
    profiles = Profile.objects.all().filter(email__icontains=query).values('id', 'email', 'registration_date')
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
    query = request.GET.get('name', '')
    products = Product.objects.all().filter(name__icontains=query).values('id', 'name', 'description', 'price', 'created_by', 'created_date')
    return JsonResponse(list(products), safe=False)

@require_http_methods(["GET"])
def get_product(request, product_id):
    product = Profile.objects.get(id=product_id)

    if product is None:
        return HttpResponseNotFound('Товар не найден')

    response = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'created_by': product.created_by,
        'created_date': product.created_date
    }

    return JsonResponse(response, safe=False)

@require_http_methods(["POST"])
def create_product(request):
    data = json.loads(request.body)

    name = data.get('name'),
    description = data.get('description')
    price = data.get('price')
    created_by = data.get('created_by')

    product = Product.objects.create(
        name=name, description=description, price=price, created_by=created_by, created_date=datetime.utcnow()
    )

    return JsonResponse(product.id, safe=False)

# endregion

# region Order

@require_http_methods(["GET"])
def get_orders(request):
    query = request.GET.get('name', '')
    orders = Order.objects.all().filter(name__icontains=query).values('id', 'profile_id', 'product_id', 'destination', 'created_date')
    return JsonResponse(list(orders), safe=False)

@require_http_methods(["POST"])
def create_order(request):
    user_id = uuid4()
    return JsonResponse(user_id)

# endregion
