from django.db import models
import datetime

# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey('Users.Users', on_delete='Cascade')
    createTime = models.DateTimeField(default=datetime.datetime.now())
    modifyTime = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "posts"
