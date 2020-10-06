from django.test import TestCase
from .models import Post


# Create your tests here.
#tablename="Post" l/q DB nên phải dùng "TestCase", KO được "SimpleTestCase"
class BlogTests(TestCase):
    def setUp(self):
        Post.objects.create(
            title='My title',
            body='just a test',
        )

    def test_string_representation(self):
        post = Post(title='My entry title')
        self.assertEqual(str(post), post.title)

    def test_post_list_view(self):
        res = self.client.get('/blog_dotq/')  #phải có "/" đầu đuôi
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'My title')
        self.assertTemplateUsed(res, 'pages/blog_dotq.html')

    def test_post_detail_view(self):
        res = self.client.get('/blog_dotq/1/')  #phải có "/" đầu đuôi
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'just a test')
        self.assertTemplateUsed(res, 'pages/post_dotq.html')
