from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
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


class MemberCreateView(views.APIView):
    """separated from MemberViewSet"""

    permission_classes = [AllowAny]

    def post(self, request):
        """signup"""
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors)


class ExampleView(views.APIView):
    """
    sample code from drf documentation
    ref: https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme
    """

    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
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
