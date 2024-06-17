from django.db import models

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='drf', max_length=3)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
