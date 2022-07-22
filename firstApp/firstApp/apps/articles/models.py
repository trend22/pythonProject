# datetime импортируется из питона
import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    article_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    # делаем метод - создана ли статья в течении 7 дней
    def was_published_recently(self):
        return self.article_date >= (timezone.now() - datetime.timedelta(days=7))

    # для переименований в админке строк в Блоге
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    # это привязка комментария к статье
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name

    # для переименований в админке строк в Блоге
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
