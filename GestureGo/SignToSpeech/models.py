from django.db import models

# Create your models here.

# class User(models.Model):
#     name = models.TextField(max_length=30)
#     username= models.TextField(max_length=15)
#     email = models.EmailField(unique=True, null=False, default = None)
#     password1 =models.TextField(max_length=10)
#     password2 =models.TextField(max_length=10)
#     date_joined= models.DateTimeField(auto_now_add=True, null=True)
#     def __str__(self):
#         return self.email