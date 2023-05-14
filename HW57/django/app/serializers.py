from rest_framework import serializers
from .models import Profile, Product, Order

# region Profile

class ProfileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'email', 'registration_date')


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email', 'password')

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('email',)

# endregion

# region Product

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'created_date')


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

# endregion

# region Order

class OrderDetailsSerializer(serializers.ModelSerializer):
    profile = ProfileDetailsSerializer()
    product = ProductDetailsSerializer()

    class Meta:
        model = Order
        fields = ('id', 'profile', 'product', 'shipping_address', 'created_date')


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('profile', 'product', 'shipping_address')

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('shipping_address',)

# endregion

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('id', 'name', 'description', 'price')
#
# class OrderSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()
#     product = ProductSerializer()
#
#     class Meta:
#         model = Order
#         fields = ('id', 'profile_id', 'product_id', 'created_date', 'destination')
