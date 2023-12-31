from django.db import models


class Anime(models.Model):
    animeid = models.IntegerField(primary_key=True, editable=False)
    animeimage = models.ImageField('アニメ写真',upload_to='anime_images/')
    title = models.CharField(max_length=50,unique=True)
    description = models.CharField('あらすじ',max_length=500)

    def __str__(self):
    	return self.title
