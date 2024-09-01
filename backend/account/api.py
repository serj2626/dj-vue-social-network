from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.decorators import (
    api_view,
)
from rest_framework.response import Response

from .models import FriendshipRequest, User
from .serializers import (
    FriendshipRequestSerializer,
    UserRegisterSerializer,
    UserSerializer,
)


@extend_schema(tags=["Auth"], summary="Получение информации о пользователе")
@api_view(["GET"])
def me(request):
    return Response(
        {"id": request.user.id, "name": request.user.name, "email": request.user.email}
    )


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    @extend_schema(tags=["Auth"], summary="Регистрация пользователя")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(tags=["Auth"], summary="Получение списка друзей пользователя")
@api_view(["GET"])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    friends = user.friends.all()

    return Response(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
        }
    )


@extend_schema(tags=["Auth"], summary="Получение списка подписчиков пользователя")
@api_view(["GET"])
def subscribers(request, pk):
    user = User.objects.get(pk=pk)
    subscribers = FriendshipRequest.objects.filter(
        created_for=user, status=FriendshipRequest.SENT
    )
    subscribers = FriendshipRequestSerializer(subscribers, many=True).data
    return Response(
        {
            "user": UserSerializer(user).data,
            "subscribers": subscribers
        }
    )


@extend_schema(tags=["Auth"], summary="Получение списка подписок пользователя")
@api_view(["GET"])
def subscriptions(request, pk):
    user = User.objects.get(pk=pk)
    subscriptions = FriendshipRequest.objects.filter(
        created_by=user, status=FriendshipRequest.SENT
    )
    subscriptions = FriendshipRequestSerializer(subscriptions, many=True)
    subscriptions = subscriptions.data
    return Response(
        {
            "user": UserSerializer(user).data,
            "subscriptions": subscriptions
        }
    )


@api_view(["POST"])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({"message": "Успешный выход"}, status=200)


@extend_schema(tags=["Auth"], summary="Отправка запроса в друзья")
@api_view(["POST"])
def send_friendship_request(request, id):
    user = User.objects.get(pk=id)
    check1 = FriendshipRequest.objects.filter(
        created_for=request.user, created_by=user)
    check2 = FriendshipRequest.objects.filter(
        created_for=user, created_by=request.user)
    if check1 or check2:
        return Response({"message": "Вы уже отправляли запрос на дружбу"}, status=400)

    FriendshipRequest.objects.create(created_for=user, created_by=request.user)
    return Response({"message": "Ваш запрос отправлен"}, status=200)


# class SendFriendshipRequestView(CreateAPIView):
#     queryset = FriendshipRequest.objects.all()
#     serializer_class = FriendshipRequestSerializer

#     def create(self, request, *args, **kwargs):
#         pk = self.kwargs['pk']
#         user = User.objects.get(pk=pk)

#         check1 = FriendshipRequest.objects.filter(
#             created_for=request.user).filter(created_by=user)
#         check2 = FriendshipRequest.objects.filter(
#             created_for=user).filter(created_by=request.user)

#         if not check1 or not check2:
