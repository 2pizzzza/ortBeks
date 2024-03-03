from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from rest_framework import permissions, generics, status, views
from . import models as m, serializers as s


class RegisterAPIView(generics.CreateAPIView):
    queryset = m.User.objects.all()
    serializer_class = s.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                'message': 'Пользователь успешно зарегистрировался',
                'access_token': str(AccessToken.for_user(user)),
                'refresh_token': str(RefreshToken.for_user(user)),
            }, status=status.HTTP_201_CREATED
        )


class LoginAPIView(generics.CreateAPIView):
    queryset = m.User.objects.all()

    def post(self, request, *args, **kwargs):
        user = m.User.objects.filter(email=request.data.get('email')).first()

        if not user:
            return Response(
                {'message': 'Пользователь не существует'},
                status=status.HTTP_404_NOT_FOUND
            )

        if not user.check_password(request.data.get('password')):
            return Response(
                {'message': 'Неверный пароль'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                'message': 'Пользователь успешно вошел в систему',
                'access_token': str(AccessToken.for_user(user)),
                'refresh_token': str(RefreshToken.for_user(user)),
            }, status=status.HTTP_200_OK
        )


class LogoutAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(cls, request):
        refresh = request.data.get('refresh')
        access = request.data.get('access')

        if not refresh and not access:
            return Response(
                {'Сообщение': 'Отсутствует токен'},
                status=status.HTTP_400_BAD_REQUEST
            )

        RefreshToken(refresh).blacklist()
        RefreshToken(access).blacklist()

        return Response(
            {'Сообщение': 'Пользователь успешно вышел из системы.'},
            status=status.HTTP_200_OK
        )


class ProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = s.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {**serializer.validated_data},
            status=status.HTTP_201_CREATED
        )


class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = m.Profile.objects.all()
    serializer_class = s.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return self.queryset.get(user=self.request.user)
        except m.Profile.DoesNotExist:
            return None

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({})

    def put(self, request, *args, **kwargs):
        self.patch(request, *args, **kwargs)
