from django.db import models

class Объявление(models.Model):
    заголовок = models.CharField(max_length=100)
    описание = models.TextField()
    дата_создания = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.заголовок