from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User
from .serializers import UserSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(email="", password="", first_name="", last_name=""):
        if email != "" and password != "" and first_name != "" and last_name != "":
            User.objects.create(email=email, password=password, first_name=first_name, last_name=last_name)

    def setUp(self):
        # add test data
        self.create_song("example@test.com", "test123", "Example", "Test")
        self.create_song("example1@test.com", "test1231", "Example1", "Test1")
        self.create_song("example2@test.com", "test1232", "Example2", "Test2")
        self.create_song("example3@test.com", "test1233", "Example3", "Test3")


class GetAllUsersTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all users added in the setUp method
        exist when we make a GET request to the users/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("users-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = User.objects.all()
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
