from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Member
from users.serializers import MemberSerializer, SignInSerializer


class MemberViewSet(viewsets.ViewSet):
    """test view set example from https://www.django-rest-framework.org/api-guide/viewsets/#example"""

    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Member.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MemberSerializer(user)
        return Response(serializer.data)

    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def signup(self, request):
        member_ser = MemberSerializer(data=request.data)
        if member_ser.is_valid():
            member_ser.save()
            refresh = RefreshToken.for_user(member_ser.instance)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response(member_ser.errors)

    @action(methods=["get"], detail=False, permission_classes=[AllowAny],
            url_path="example", url_name="example")
    def example(self, request):
        authenticator = JWTAuthentication()
        response = authenticator.authenticate(request)
        if response:
            user, token = response
            ser_user = MemberSerializer(user)
            return Response(
                {
                    "user": ser_user.data,
                    "token": token.payload,
                }
            )
        return Response({"error": "cannot authenticate"})
