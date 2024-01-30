from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer, CartSerializer
from .models import Product, Cart
# Create your views here.


class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all()
        print(products)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class CartView(APIView):

    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        cart = Cart.objects.filter(
            product_id=request.data['product_id']).first()
        cart.delete()
        return Response("Deleted")
