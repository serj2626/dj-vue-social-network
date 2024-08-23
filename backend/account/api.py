from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response

from .forms import SignupForm


@api_view(['GET'])
def me(request):
    return Response({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    print("form", form.errors)

    if form.is_valid():
        form.save()
        # Send verification email later!
    else:
        message = 'error'

    return Response({'message': message})
