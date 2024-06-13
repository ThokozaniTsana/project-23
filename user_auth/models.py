from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """param: An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Class to create a custom user objects.
    """

    username = models.CharField(
        max_length=150, 
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits, and spaces only.',
        validators=[],
        error_messages={
            'unique': "A user with that username already exists. Please try another name.",
        },
    )  
