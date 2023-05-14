from rest_framework import generics
from rest_framework.response import Response
from .serializers import *

# region Profile

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        query = request.query_params.get('email')
        if query:
            queryset = queryset.filter(email__icontains=query)

        serializer = ProfileDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    lookup_url_kwarg = 'profile_id'

    def get(self, request, *args, **kwargs):
        profile_id = self.kwargs.get('profile_id')
        queryset = self.get_queryset().filter(id=profile_id)
        serializer = ProfileDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

# endregion

# region Product

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    lookup_url_kwarg = 'product_id'

    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        queryset = self.get_queryset().filter(id=product_id)
        serializer = ProductDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

# endregion

# region Order

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    lookup_url_kwarg = 'order_id'

    def get(self, request, *args, **kwargs):
        order_id = self.kwargs.get('order_id')
        queryset = self.get_queryset().filter(id=order_id)
        serializer = OrderDetailsSerializer(queryset, many=True)
        return Response(serializer.data)

# endregion
