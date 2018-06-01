from django.db import models

# Create your models here.
"""例
class Card(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    liked = models.IntegerField(default=0)
    card_date = models.DateTimeField('date published', default=timezone.now)
    card_tag = models.TextField()
    card_caregory = models.TextField()
    user = models.ForeignKey(User,related_name='cards',on_delete=models.CASCADE,default="0")
"""