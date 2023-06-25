from django.db import models
from map.models import Place
from accounts.models import User
from anime.models import Anime

class Post(models.Model):
    postid = models.IntegerField('投稿ID', primary_key=True,unique=True,auto_created=True)
    userid = models.ForeignKey(User, on_delete=models.PROTECT,to_field='userid',  related_name='users')
    placeid = models.ForeignKey(Place, on_delete=models.PROTECT,to_field='placeid',  related_name='posts')
    animeid = models.ForeignKey(Anime, on_delete=models.PROTECT,to_field='amineid', related_name='animeid')
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    postimage = models.ImageField('画像', upload_to='post_images/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
