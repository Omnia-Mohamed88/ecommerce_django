from rest_framework import serializers
from .models import Product, Category




class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):
    productcategory = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'







# from rest_framework import serializers
# from .models import Product, Category

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'categoryname'] 

# class ProductSerializer(serializers.ModelSerializer):
#     productcategory = CategorySerializer()  

#     class Meta:
#         model = Product
#         fields = '__all__'  


# from rest_framework import serializers
# from .models import Product, Category

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'categoryname']

# class ProductSerializer(serializers.ModelSerializer):
#     productcategory = CategorySerializer()  

#     class Meta:
#         model = Product
#         fields = '__all__'
