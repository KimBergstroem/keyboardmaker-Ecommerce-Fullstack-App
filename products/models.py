from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model representing product categories
    """
    class Meta:
        verbose_name_plural = 'Categories' # Add correct name in the admin dashboard

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model representing products in the e-commerce system
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def image_size_save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            try:
                img = Image.open(self.image.path)
                max_size = (380, 380)

                # Resize the image if it exceeds the maximum size
                if img.height > max_size[1] or img.width > max_size[0]:
                    img.thumbnail(max_size, Image.LANCZOS)
                    img.save(self.image.path)
            except Exception as e:
                print(f"Error processing image for product {self.name}: {e}")

    def average_rating(self):
        reviews = self.review_set.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0  # or another default value if there are no reviews

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Model representing product reviews by users
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Sets the order of comments by date ascending
        """
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment {self.text} by {self.user.username}"
