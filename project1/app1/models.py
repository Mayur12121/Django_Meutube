from django.db import models
from django.contrib.auth.models import User # Import User model for user-related fields

# Create your models here.

class ABC(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User model
    text=models.TextField(max_length=100)
    photo=models.ImageField(upload_to='photos/', null=True, blank=True)  # Image field for photo uploads
    updated_at=models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is saved
    created_at=models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    
    def __str__(self): #makes the object more readable in the admin interface
        # Return a string representation of the model instance
        return f"{self.user.username} - {self.text[:10]}"