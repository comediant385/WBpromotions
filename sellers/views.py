from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from sellers.models import Seller
from sellers.serializers import SellerSerializer


class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer