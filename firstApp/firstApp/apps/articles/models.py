from django.db import models


class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    article_date = models.DateTimeField('дата публикации')


class Comment(models.Model):
    # это привязка комментария к статье
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)
