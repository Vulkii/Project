from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    kogda = models.CharField('Когда будет:', max_length=50)
    who = models.CharField('Кто приглашает',max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
