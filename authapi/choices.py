from django.db import models


class UserTypeChoices(models.TextChoices):
    USER = 'USER', 'USER'
    RESTAURANT_OWNER = 'RESTAURANT_OWNER', 'Restaurant Owner'
    DELIVERY_PARTNER = 'DELIVERY_PARTNER', 'Delivery Partner'