from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .forms import SignupForm
from .models import FriendshipRequest, User
from .serializers import FriendshipRequestSerializer, UserRegisterSerializer, UserSerializer
from rest_framework import generics


@extend_schema(tags=["Auth"], summary="Получение информации о пользователе")
@api_view(["GET"])
def me(request):
    return Response(
        {"id": request.user.id, "name": request.user.name, "email": request.user.email}
    )


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    @extend_schema(summary="Регистрация пользователя")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



@extend_schema(tags=["Auth"], summary="Получение списка друзей пользователя")
@api_view(["GET"])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(
            created_for=request.user, status=FriendshipRequest.SENT
        )
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return Response(
        {
            "user": UserSerializer(user).data,
            "friends": UserSerializer(friends, many=True).data,
            "requests": requests,
        }
    )


@api_view(['POST'])
def logout_user(request):
    request.user.auth_token.delete()
    return Response({"message": "Успешный выход"}, status=200)


@extend_schema(tags=["Auth"], summary="Отправка запроса в друзья")
@api_view(["POST"])
def send_friendship_request(request, id):
    user = User.objects.get(pk=id)
    return Response({"message": "friendship request created"})

    # check1 = FriendshipRequest.objects.filter(
    #     created_for=request.user).filter(created_by=user)
    # check2 = FriendshipRequest.objects.filter(
    #     created_for=user).filter(created_by=request.user)

    # if not check1 or not check2:
    #     friendrequest = FriendshipRequest.objects.create(
    #         created_for=user, created_by=request.user)

    #     # notification = create_notification(
    #     #     request, 'new_friendrequest', friendrequest_id=friendrequest.id)

    #     return JsonResponse({'message': 'friendship request created'})
    # else:
    #     return JsonResponse({'message': 'request already sent'})


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
