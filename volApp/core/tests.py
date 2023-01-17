import unittest
from django.test import tag
from django.urls import reverse
from django.test import Client
from .models import User


@tag("unit_test")
class LogoutTest(unittest.TestCase):
    """LogoutTest """
    client = Client()

    def test_logout(self):
        """testLogout """
        # User.objects.create(username='israa1', password='123')
        self.client.login(username='username', password='password')

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)

    @tag('unit-test')
    def test_logout_url(self):
        """test_logout_url """
        response = self.client.get('logout', )
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_home_url(self):
        """test_home_url """
        response = self.client.get('home', )
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_login_url(self):
        """test_home_url """
        response = self.client.get('login', )
        self.assertNotEqual(response.status_code, 300)

class AddFoodTest(unittest.TestCase):
    """add-secretary """
    client = Client()

    @tag('integration-test')
    def test_addsecretary(self):
        """test_add_to_food_list """
        # accss view
        response = self.client.get(('login'))
        self.assertTrue(User.is_authenticated)

        response = self.client.get(('add-secretary'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

        @tag('integration-test')
        def test_profile(self):
            """test_nurse_dashboard """
            # accss view
            response = self.client.get(('login'))
            self.assertTrue(User.is_authenticated)

            response = self.client.get(('profile'))
            self.assertNotEqual(response.status_code, 300)

            response = self.client.get(reverse('logout'), follow=True)

            self.assertEqual(response.status_code, 200)

            def test_profile2(self):
                """test_nurse_dashboard """
                # accss view
                response = self.client.get(('login'))
                self.assertTrue(User.is_authenticated)

                response = self.client.get(('schedule'))
                self.assertNotEqual(response.status_code, 300)

                response = self.client.get(reverse('logout'), follow=True)

                self.assertEqual(response.status_code, 200)

                @tag('integration-test')
                def testallstudents(self):
                    """test_nurse_dashboard """
                    # accss view
                    response = self.client.get(('login'))
                    self.assertTrue(User.is_authenticated)

                    response = self.client.get(('allstudents'))
                    self.assertNotEqual(response.status_code, 300)

                    response = self.client.get(reverse('logout'), follow=True)

                    self.assertEqual(response.status_code, 200)

                    @tag('unit-test')
                    def test__template(self):
                        """test_update_ecg_access_template """
                        response = self.client.get('add-secretary')
                        self.assertNotEqual(response.status_code, 300)
                        value = 'add-secretary.html'
                        self.assertTrue(value)

                        @tag('unit-test')
                        def test__template(self):
                            """test_update_ecg_access_template """
                            response = self.client.get('allstudents')
                            self.assertNotEqual(response.status_code, 300)
                            value = 'allstudents.html'
                            self.assertTrue(value)

                        def test__template(self):
                            """test_update_ecg_access_template """
                            response = self.client.get('base')
                            self.assertNotEqual(response.status_code, 300)
                            value = 'base.html'
                            self.assertTrue(value)

                        def test__template(self):
                            """test_update_ecg_access_template """
                            response = self.client.get('home')
                            self.assertNotEqual(response.status_code, 300)
                            value = 'home.html'
                            self.assertTrue(value)

                        def test__template(self):
                            """test_update_ecg_access_template """
                            response = self.client.get('login')
                            self.assertNotEqual(response.status_code, 300)
                            value = 'login.html'
                            self.assertTrue(value)

                            























