from django.db import models

# Create your models here.
class Title(models.Model):
    title = models.CharField(max_length=200)
    #i = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.ForeignKey(Title, on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=200)
    def __str__(self):
        return self.tag_text
