from django.db import models
from django.conf import settings


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="image/", blank=True)
    
    author = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product")
    
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    ) 
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.content