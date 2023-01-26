from rest_framework import serializers


from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    model = Item
    fields = (
        'id',
        'name',
        'description',
        'price'
    )