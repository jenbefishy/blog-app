from django.db import models
from django.utils.crypto import get_random_string
from users.models import CustomUser


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    slug = models.SlugField(max_length=25, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = get_random_string(length=25)
        while Post.objects.filter(slug=slug).exists():
            slug = get_random_string(length=25)
        return slug

    def __str__(self):
        return self.title
