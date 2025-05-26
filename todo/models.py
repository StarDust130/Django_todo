from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]

