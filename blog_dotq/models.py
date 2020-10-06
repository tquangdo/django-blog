from django.db import models
from django.conf import settings
# from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='commentsFromModel')
    # TH có related_name thì shell dùng Post.commentsFromModel.all()
    # TH KO có related_name thì shell dùng Post.comment_set.all()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               default='',
                               on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Choice(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}'.format(self.question, self.choice_text)


# class CustomUser(AbstractUser):
#     age = models.IntegerField(default=0)
#     gender_type = ((0, "Nữ"), (1, "Nam"), (2, "Unknown"))
#     gender = models.IntegerField(choices=gender_type, default=0)
#     address = models.CharField(default='', max_length=255)
