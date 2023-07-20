from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


tk = 'Танки'
hl = 'Хилы'
dd = 'ДД'
gm = 'Гилдмастеры'
qg = 'Квестгиверы'
kz = 'Кузнецы'
kj = 'Кожевникм'
zv = 'Зельевары'
mz = 'Мастера заклинаний'

CATEGORIES = [
    (tk, 'Танк'),
    (hl, 'Хил'),
    (dd, 'ДД'),
    (gm, 'Гилдмастер'),
    (qg, 'Квестгивер'),
    (kz, 'Кузнец'),
    (kj, 'Кожевник'),
    (zv, 'Зельевар'),
    (mz, 'Мастер заклинаний'),
]


class Categories(models.Model):
    name = models.CharField(max_length=19, choices=CATEGORIES, default=tk)

    def __str__(self):
        return self.name.title()


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Название")
    text = RichTextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Reply(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)


class News(models.Model):
    title = models.CharField(max_length=100, default="Default value")
    text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)