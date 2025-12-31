from django.db import models

# Create your models here.
class BookModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('name', 'author', 'year')
    
    def __str__(self):
        return self.name

    