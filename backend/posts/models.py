from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timesince import timesince

from .service import get_path_for_post_image

User = get_user_model()


class PostAttachment(models.Model):
    """
    Модель Прикрепленного файла
    """

    image = models.ImageField(
        verbose_name="картинка", upload_to=get_path_for_post_image
    )
    author = models.ForeignKey(
        User,
        related_name="post_attachments",
        on_delete=models.CASCADE,
        verbose_name="автор",
    )

    class Meta:
        verbose_name = "Прикрепленный файл"
        verbose_name_plural = "Прикрепленные файлы"




class Post(models.Model):
    """
    Модель Поста
    """

    body = models.TextField(verbose_name="текст поста", blank=True, null=True)

    attachments = models.ManyToManyField(
        PostAttachment, blank=True, verbose_name="прикрепленные файлы"
    )

    likes = models.ManyToManyField(User, blank=True, verbose_name="лайки")

    created_at = models.DateTimeField(
        verbose_name="дата создания", auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE, verbose_name="автор"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return f"Post {self.body[:10]}... by {self.author}"


class Comment(models.Model):
    """
    Модель Комментария
    """

    body = models.TextField(blank=True, null=True,
                            verbose_name="текст комментария")
    author = models.ForeignKey(
        User, related_name="user_comments", on_delete=models.CASCADE, verbose_name="автор"
    )
    post = models.ForeignKey(
        Post, related_name="post_comments", on_delete=models.CASCADE, verbose_name="пост"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return f"Комментарий от {self.author}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def created_at_formatted(self):
        return timesince(self.created_at)
