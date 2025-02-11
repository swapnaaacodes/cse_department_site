from django.db import models
from django.utils.text import slugify

class Notice(models.Model):
    """
    Model representing a notice.
    """
    topic = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the notice.
        """
        return self.topic

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to generate a slug based on the topic field.
        """
        if not self.slug:
            self.slug = slugify(self.topic)
        
        super().save(*args, **kwargs)


class Events(models.Model):
    """
    Model representing an event.
    """
    topic = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the event.
        """
        return self.topic

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to generate a slug based on the topic field.
        """
        if not self.slug:
            self.slug = slugify(self.topic)
        
        super().save(*args, **kwargs)

class Blog(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)  # Change from ForeignKey to CharField
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    def __str__(self):
        """
        Returns a string representation of the blog post.
        """
        return self.title