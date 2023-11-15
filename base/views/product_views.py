from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Product
from base.serializers import ProductSerializer


from rest_framework import status
from drf_spectacular.utils import extend_schema

@extend_schema(responses=ProductSerializer)
@api_view(['GET'])
def getProducts(request):
    products= Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@extend_schema(responses=ProductSerializer)
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False )
    return Response(serializer.data)

@extend_schema(responses=ProductSerializer)
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product deleted')


@extend_schema(responses=ProductSerializer)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user

    product = Product.objects.create(
        user= user,
        name='Apple',
        price= 0.99,
        category="FRUIT",

    )

    serializer = ProductSerializer(product, many=False )
    return Response(serializer.data)


@extend_schema(responses=ProductSerializer)
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)


    product.name = data['name']
    product.category = data['category']
    # product.image = data['name']
    product.description = data['description']
    product.price = data['price']
    product.discount = data['discount']
    product.percentage = data['percentage']
    product.startDate = data['startDate']
    product.endDate = data['endDate']
    product.discounted_price = data['discounted_price']

    product.save()

    serializer = ProductSerializer(product, many=False )
    return Response(serializer.data)


@extend_schema(responses=ProductSerializer)
@api_view(['POST'])
def uploadImage(request):  
    data = request.data

    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)

    product.image = request.FILES.get('image')
    product.save()  
    return Response('Image was uploaded')
