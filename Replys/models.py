from django.db import models
import datetime

# Create your models here.


class Reply(models.Model):
    content = models.CharField(max_length=20000)
    author = models.ForeignKey('Users.User', on_delete='Cascade')
    fatherId = models.ForeignKey('Reply', on_delete='Cascade', null=True)
    time = models.DateTimeField(default=datetime.datetime.now())
    postId = models.ForeignKey('Posts.Post', on_delete='Cascade')

    class Meta:
        db_table = "replys"
