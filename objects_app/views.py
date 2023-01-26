from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

# Create your views here.
 class ItemListView(APIView):
    def get(self, request):
        lst = Item.objects.all()
        return Response({'lst': lst})

    # def post(self, request):

    