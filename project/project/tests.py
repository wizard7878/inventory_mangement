from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
import os

class InventoryConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get('SECRET_KEY')
        try:
            validate_password(SECRET_KEY)
        except Exception as err:
            msg = f"Weak Secert Key {err.messages}"
            self.fail(msg)
        