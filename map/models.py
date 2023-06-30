from django.db import models
from anime.models import Anime

#検索するときに使用するModel
class PlaceManager(models.Manager):
    def search_by_name(self, query):
        return self.filter(name__icontains=query)       
        
        
# 聖地の場所のモデル
class Place(models.Model):
    placeid = models.IntegerField('場所ID', primary_key=True,unique=True,auto_created=True)
    name = models.CharField('名前', max_length=50,unique=True)
    address = models.CharField('住所', max_length=50)
    descpiption = models.TextField('説明', max_length=500)
    accsess = models.CharField('アクセス', max_length=200)
    notes = models.TextField('備考', max_length=400)
    placeimage = models.ImageField('画像', upload_to='place_images/')
    lat = models.DecimalField('緯度', max_digits=9, decimal_places=7)
    lng = models.DecimalField('経度', max_digits=10, decimal_places=7)
    animeid = models.ForeignKey(Anime, on_delete=models.PROTECT,to_field='animeid',  related_name='anime')
    animetitle = models.ForeignKey(Anime, on_delete=models.PROTECT,to_field='title',  related_name='animetitle')
     
    objects = PlaceManager()

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = '場所'
        verbose_name_plural = '場所'



# Create your models here.
