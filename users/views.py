from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from users.models import Member
from users.serializers import MemberSerializer, SignInSerializer


class MemberViewSet(viewsets.ViewSet):
    """test view set example from https://www.django-rest-framework.org/api-guide/viewsets/#example"""

    def list(self, request):
        queryset = Member.objects.all()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Member.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = MemberSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        """signup"""
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors)

    @action(methods=["post"], detail=True)
    @permission_classes([AllowAny])
    def signin(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            pw = serializer.validated_data["password"]
            user = authenticate(request, email=email, password=pw)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return Response({"message": "login failed"}, status.HTTP_400_BAD_REQUEST)
