""" Client allows us to make Test Requests to our app's unit tests """
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
""" reverse helps us generate URLS for our Django admin page """


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='jason@digital-knowledge.co.jp',
            password='password1!'
        )
        """ Use helper function to login the superuser,
            so we don't need to login manually to do our tests. """
        self.client.force_login(self.admin_user)
        """ setup a spare user we can use for testing listings, etc. """
        self.user = get_user_model().objects.create_user(
            email='kd@user1.co.jp',
            password='password1!',
            name="Tester Man"
        )

    def test_users_listed(self):
        """ Test that users are listed on user page """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        """ Make sure the response is HTTP 200, and check the content """
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Test that the user edit page works """
        url = reverse('admin:core_user_change', args=[self.user.id])
        # -> ex: / admin/core/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test that the create user page works """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
