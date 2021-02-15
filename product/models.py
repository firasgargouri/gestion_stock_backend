from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'profiles/{filename}'.format(filename=filename)


class Category(models.Model):
    category = models.CharField(max_length=20)
    objects = models.Manager()

    def __str__(self):
        return str(self.category)


class SubCategory(models.Model):
    subCategory = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.subCategory)


class Product(models.Model):
    # reference = models.IntegerField()
    titre = models.CharField(max_length=50)
    description = models.TextField(max_length=250, null=True)
    prix = models.DecimalField(
        max_digits=20, decimal_places=3, default=0.000)
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='products/default.png', blank=True)
    quantite = models.IntegerField(default=0)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta():
        ordering = ('-quantite',)

    def __str__(self):
        return str(self.titre)
