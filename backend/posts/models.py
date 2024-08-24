import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timesince import timesince

from .service import get_path_for_post_image

User = get_user_model()


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(
        User, related_name="likes", on_delete=models.CASCADE, verbose_name="автор")
    created_at = models.DateTimeField(
        verbose_name="дата создания", auto_now_add=True)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(verbose_name="текст поста", blank=True, null=True)

    attachments = models.ManyToManyField(
        PostAttachment, blank=True, verbose_name="прикрепленные файлы"
    )

    likes = models.ManyToManyField(Like, blank=True, verbose_name="лайки")
    likes_count = models.IntegerField(
        verbose_name="количество лайков", default=0)

    created_at = models.DateTimeField(
        verbose_name="дата создания", auto_now_add=True)
    author = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("-created_at",)

    def created_at_formatted(self):
        return timesince(self.created_at)

    def __str__(self):
        return f"Post {self.body[:10]}... by {self.author}"
