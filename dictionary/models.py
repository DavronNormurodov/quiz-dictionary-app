from django.db import models
from accounts.models import User


class DictionaryModel(models.Model):
    word = models.CharField(max_length=255, verbose_name="English word")
    defination = models.TextField(max_length=1000, verbose_name="Defination or translation")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='word_by_user', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return f"{self.word}:{self.defination}"