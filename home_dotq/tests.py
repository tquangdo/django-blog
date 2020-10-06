from django.test import TestCase, SimpleTestCase


# python manage.py test home_dotq
class SimpleTest(SimpleTestCase):
    def test_home_dotq_status(self):
        res = self.client.get('/')  #phải có "/" đầu đuôi
        self.assertEquals(res.status_code, 201)