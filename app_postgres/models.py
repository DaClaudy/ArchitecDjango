from django.contrib.gis.db import models as gis_models
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.geos import Point


class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    longitude = models.FloatField()
    latitude = models.FloatField()
    localisation = gis_models.PointField(geography=True, srid=4326)

    vector_search = ArrayField(models.FloatField(), blank=True, null=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        # Sync la position (Point) avec lat/lon
        if self.latitude is not None and self.longitude is not None:
            self.localisation = Point(self.longitude, self.latitude)
        super().save(*args, **kwargs)
