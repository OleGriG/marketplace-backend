from rest_framework import serializers

from .models import Product, Category, ProductPhoto, Slider, Cart
from user_service.serializers import SellerSerializer


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['photo']


class DetaileProductSerializer(serializers.ModelSerializer):
    photos = ProductPhotoSerializer(
        many=True, read_only=True, source='productphoto_set'
    )

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('rate', 'display_on_main_page', 'owner', 'main_photo' 'photos')


class ProductSerializer(serializers.ModelSerializer):
    owner = SellerSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('rate', 'display_on_main_page', 'owner', 'main_photo')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products']