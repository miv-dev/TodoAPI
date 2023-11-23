from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User
from users.pagination import LargeResultsSetPagination
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.SearchFilter]

    search_fields = ['username']

    def get_queryset(self):
        queryset = User.objects.all()

        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        if first_name is not None:
            queryset = queryset.filter(Q(first_name__startswith=first_name), Q(last_name__startswith=last_name))
        return queryset
