from account.models import FriendshipRequest


def get_path_for_post_image(instance, filename):
    return f"post_attachments/{instance.author}/{filename}"


def get_status(self, user):
    status = ""

    if user in self.request.user.friends.all():
        status = "Ваш друг"
    elif self.request.user in user.friends.all():
        status = "Ваш друг"
    elif FriendshipRequest.objects.filter(
        created_by=self.request.user, created_for=user
    ):
        status = "Вы подписаны"
    elif FriendshipRequest.objects.filter(
        created_by=user, created_for=self.request.user
    ):
        status = "Ваш подписчик"
    else:
        status = "Отправить заявку"

    return status