from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

User = get_user_model()


class TestRegisterView(APITestCase):
    def setUp(self):
        self.url = reverse("accounts:signup")
        self.payload = {
            "username": "abc",
            "email": "abc@example.com",
            "password": "abcpass*",
            "first_name": "Abc",
            "last_name": "Xyz",
        }

    def test_registration(self):
        """
       This method is to check if
       RegisterView is creating user
       object properly
       """
        resp = self.client.post(self.url, data=self.payload, format="json")
        user_object = User.objects.first()
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(user_object.email, self.payload["email"])

    def test_not_saving_raw_password(self):
        """
       to test that RegisterView is not
       saving password as raw text without
       hashing
       """
        resp = self.client.post(self.url, data=self.payload)
        user_object = User.objects.get(username=self.payload['username'])
        self.assertNotEqual(user_object.password, self.payload["password"])

    def test_password_not_in_response(self):
        """
       making sure that password is not
       present in response
       """
        resp = self.client.post(self.url, data=self.payload, format="json")
        self.assertNotIn("password", resp.data)


class TestObtainJWTTokenView(APITestCase):
    """
   This class is for testing
   obtain_token_view
   """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="abc", email='abc@example.com', password="abcpassword")

    def test_token_generation(self):
        """
       Token generation test with proper
       payload
       """
        url = reverse("accounts:login")
        data = {"username": "abc", "password": "abcpassword"}
        resp = self.client.post(path=url, data=data, format="json")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("token", resp.data)


class TestVerifyToken(APITestCase):
    """
   This class is to test
   token_verify_jwt_token view
   """

    def setUp(self):
        self.client = APIClient()
        self.url = reverse("accounts:verify_token")
        self.login_url = reverse("accounts:login")

        self.user = User.objects.create_user(
            username="abc", email='abc@example.com', password="abcpassword")

        self.payload = {
            "username": "abc",
            "password": "abcpassword",
        }

    def test_token_verification(self):
        """
       method to test token verify
       is working as expected
       """

        # to add JWT at start
        token = self.client.post(self.login_url, data=self.payload, format="json").data["token"]
        resp = self.client.post(self.url, data={"token": token}, format="json")
        error_resp = self.client.post(self.url, data={"token": token + "x"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(error_resp.status_code, 400)


class TestRefreshJWTToken(APITestCase):
    """
   This class is to test refresh_jwt_token view
   """

    def setUp(self):
        self.client = APIClient()
        self.url = reverse("accounts:refresh_token")
        self.login_url = reverse("accounts:login")

        self.user = User.objects.create_user(
            username="abc", email='abc@example.com', password="abcpassword")

        self.payload = {
            "username": "abc",
            "password": "abcpassword",
        }

    def test_refresh_jwt_token_view(self):
        """
       test method to make sure refresh_jwt_token
       view working properly
       """
        token = self.client.post(self.login_url, data=self.payload, format="json").data["token"]
        resp = self.client.post(self.url, data={"token": token})
        self.assertEqual(resp.status_code, 200)
        self.assertIn("token", resp.data)