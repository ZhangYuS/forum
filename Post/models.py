from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('User.User', on_delete='Cascade')
    createTime = models.DateTimeField(default=datetime.datetime.now())
    modifyTime = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=20000, null=True)

    class Meta:
        db_table = "posts"

class Reply(models.Model):
    content = models.CharField(max_length=20000)
    author = models.ForeignKey('User.User', on_delete='Cascade')
    fatherId = models.ForeignKey('Reply', on_delete='Cascade', null=True)
    time = models.DateTimeField(default=datetime.datetime.now())
    postId = models.ForeignKey('Post.Post', on_delete='Cascade')

    class Meta:
        db_table = "replys"