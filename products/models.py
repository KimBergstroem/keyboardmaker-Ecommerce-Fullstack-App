from django.db import models
from PIL import Image

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories' # Add correct name in the admin dashboard

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
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


    def __str__(self):
        return self.name
