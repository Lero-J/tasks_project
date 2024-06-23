from django.db import models

# Create your models here.



class Task(models.Model):
    name = models.CharField(max_length=100, null=True)

    slug = models.SlugField(unique=True, null=True)

    is_done = models.BooleanField(default=False, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



class User(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(unique=True, null=True)
    task = models.ManyToManyField(Task, related_name='users')
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


