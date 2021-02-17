from django.db import models


class Plate(models.Model):
    COURSES = (
        ('A', 'Antipasto'),
        ('P', 'Primo'),
        ('S', 'Secondo'),
        ('Z', 'Pizza'),
        ('D', 'Dessert'),
        ('B', 'Beverage')
    )

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    course_type = models.CharField(max_length=1, choices=COURSES)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
