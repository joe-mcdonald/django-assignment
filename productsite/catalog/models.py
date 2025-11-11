from django.db import models

# Create your models here.
class Category(models.Model):
    # Category name field. Unique to avoid duplicates.
    name = models.CharField(max_length=100, unique=True)

    # Meta class to define ordering
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    # Tag name field. Unique to avoid duplicates.
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    # name field for the product
    name = models.CharField(max_length=150)

    # description field can be blank
    description = models.TextField(blank=True)

    # category foreign key relationship to Category model and cascade on delete
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    # many-to-many relationship with Tag model
    tags = models.ManyToManyField(Tag, related_name='products', blank=True)

    # price field with decimal type
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # ordering by name
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name