from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class TestUserModel(TestCase):
    """
    This class is for testing User model
    """

    def setUp(self):
        User.objects.create_user(username='usertest', password='abc1234', email='usertest@example.com')
        self.user = User.objects.get(username='usertest')

    def test_create_user(self):
        """
        testing if user object is being
        created properly
        """
        User.objects.create_user(username='abc', password='abcpass', email='abc@example.com')
        user_obj = User.objects.get(username='abc')
        self.assertTrue(user_obj.email, "abc@example.com")
        self.assertEqual(str(user_obj), "abc")
