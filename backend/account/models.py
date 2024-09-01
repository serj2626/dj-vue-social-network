import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(name, email, password, **extra_fields)

    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True, default="")
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)
    friends = models.ManyToManyField(
        "self",
        verbose_name="друзья",
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["name"]

    def __str__(self):
        return self.email


class FriendshipRequest(models.Model):
    SENT = "отправлено"
    ACCEPTED = "принято"
    REJECTED = "отклонено"

    STATUS_CHOICES = (
        (SENT, "Sent"),
        (ACCEPTED, "Accepted"),
        (REJECTED, "Rejected"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_for = models.ForeignKey(
        User,
        related_name="received_friendshiprequests",
        on_delete=models.CASCADE,
        verbose_name="получатель",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    created_by = models.ForeignKey(
        User,
        related_name="created_friendshiprequests",
        on_delete=models.CASCADE,
        verbose_name="отправитель",
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=SENT, verbose_name="статус"
    )

    def __str__(self):
        return f"Запрос на дружбу от {self.created_by} -> {self.created_for}"

    class Meta:
        verbose_name = "Запрос в друзья"
        verbose_name_plural = "Запросы в друзья"
        ordering = ["-created_at"]


# class Community(models.Model):
#     title = models.CharField(max_length=255, verbose_name="название сообщества")
#     description = models.TextField(blank=True, null=True, verbose_name="описание")
#     avatar = models.ImageField(upload_to="communities", blank=True, null=True)
#     author = models.ForeignKey(
#         User, related_name="communities", on_delete=models.CASCADE
#     )
#     users = models.ManyToManyField(
#         User, verbose_name="участники", related_name="my_communities"
#     )
#     created_at = models.DateTimeField(
#         verbose_name="дата создания", auto_now_add=True
#     )

#     class Meta:
#         verbose_name = "Сообщество"
#         verbose_name_plural = "Сообщества"
#         ordering = ["-created_at"]

#     def created_at_formatted(self):
#         return timesince(self.created_at)

#     def __str__(self):
#         return self.title
