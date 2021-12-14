from django.conf import settings
from django.db import models
from django.utils import timezone
# 他のファイルから引用

class Post(models.Model):
# Postはモデルの名前、(models.Model):はポストがDjangoModelという意味

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #authorは著者
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title