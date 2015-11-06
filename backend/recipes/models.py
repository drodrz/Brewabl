from django.db import models
from django.conf import settings

RECIPE_TYPES = (
    ('ALL GRAIN', 'All Grain'),
    ('EXTRACT', 'Extract'),
    ('PARTIAL', 'Partial Mash'),
)

FERMENTABLE_TYPES = (
    ('GRAIN', 'Grain'),
    ('SUGAR', 'Sugar'),
    ('DRY EXTRACT', 'Dry Extract'),
    ('WET EXTRACT', 'Wet Extract'),
    ('ADJUNCT', 'Adjunct'),
)

YEAST_TYPES = (
    ('LAGER', 'Lager'),
    ('ALE', 'Ale'),
    ('HYBRID', 'Hybrid'),
    ('SOUR', 'Sour'),
)

HOP_TYPES = (
    ('MASH', 'Mash'),
    ('FWH', 'First Wort Hop'),
    ('BOIL', 'Boil'),
    ('WHIRLPOOL', 'Whirlpool'),
    ('SECONDARY', 'Secondary'),
)

MISC_TYPES = (
    ('FLAVOR', 'Flavor'),
    ('SPICE', 'Spice'),
    ('FINING', 'Fining'),
    ('FERMENTATION', 'Fermentation'),
    ('OTHER', 'Other'),
)


class Fermentable(models.Model):
    name = models.CharField(max_length=64)
    mfg = models.CharField(max_length=64)
    type = models.CharField(max_length=20, choices=FERMENTABLE_TYPES)
    ppg = models.IntegerField()
    srm = models.IntegerField()

    def __str__(self):
        return self.name


class Hop(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=20, choices=YEAST_TYPES)
    weight = models.IntegerField()
    duration = models.IntegerField()
    aa = models.FloatField()

    def __str__(self):
        return self.name


class Yeast(models.Model):
    name = models.CharField(max_length=64)
    mfg = models.CharField(max_length=64)
    type = models.CharField(max_length=20, choices=YEAST_TYPES)
    att_min = models.PositiveSmallIntegerField()
    att_max = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Misc(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=20, choices=MISC_TYPES)

    def __str__(self):
        return self.name


class WaterProfile(models.Model):
    name = models.CharField(max_length=64)
    calcium = models.IntegerField()
    magnesium = models.IntegerField()
    sodium = models.IntegerField()
    chlorine = models.IntegerField()
    alkalinity = models.IntegerField()
    pH = models.FloatField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=64)
    style = models.CharField(max_length=64)
    type = models.CharField(max_length=32)
    notes = models.TextField(max_length=1024, null=True)

    # Ingredients
    fermentables = models.ManyToManyField(Fermentable)
    hops = models.ManyToManyField(Hop)
    yeast = models.ManyToManyField(Yeast)
    misc = models.ManyToManyField(Misc)

    # TODO: Water profiles, additions

    # metadata
    created = models.DateField('Date Created', null=True)
    modified = models.DateField('Last modified', null=True)
    original = models.ForeignKey('Recipe', null=True)

    def __str__(self):
        return self.name
