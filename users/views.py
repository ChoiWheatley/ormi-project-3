from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, views
from rest_framework.response import Response
from users.models import Member
from users.serializers import MemberSerializer


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


class MemberLoginView(views.APIView):
    def post(self, request):
        serializer = MemberSerializer(data=request.data)

