# from django.db import models
# class Category(models.Model):
#     categoryname = models.CharField(max_length=30)
#     image = models.ImageField(null=True , blank=True)
#     description = models.TextField(null=True, blank=True)
#     def __str__(self):
#         return self.categoryname
# class Product(models.Model):
#     productname = models.CharField(max_length=150)
#     image = models.ImageField(null=True, blank=True)
#     productbrand = models.CharField(max_length=100, null=True, blank=True)
#     # productcategory = models.CharField(max_length=100, null=True, blank=True)
#     # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
#     productcategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', default=1)  
#     productinfo = models.TextField(null=True, blank=True)
#     rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     stock = models.IntegerField(null=True, blank=True, default=0)
#     createdAt = models.DateTimeField(auto_now_add=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return self.productname

from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class Category(models.Model):
    categoryname = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.categoryname

class Product(models.Model):
    productname = models.CharField(max_length=150)
    # image = models.ImageField(null=True, blank=True)
    # image = models.URLField(null=True, blank=True)  # Change ImageField to URLField
    image = models.ImageField(null=True, blank=True, upload_to='products/', storage=RawMediaCloudinaryStorage())
    productbrand = models.CharField(max_length=100, null=True, blank=True)
    productcategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  
    productinfo = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.productname

