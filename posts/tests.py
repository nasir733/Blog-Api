from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):
    @classmethod
    # create a user
