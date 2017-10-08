# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from serializers import *
from models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from rest_framework import permissions
from permissions import IsOwnerOrReadOnly

# Create your views here.
class SignupList(APIView):
    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ok", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginList(APIView):
    def get_object(self, user_id, password):
        try:
            return User.objects.get(user_id=user_id,password=password)
        except User.DoesNotExist:
            return

    def get(self, request, format=None):
        self.get_object(request.GET['user_id'],request.GET['password'])

        return Response("Ok", status=status.HTTP_200_OK)

class ValidationList(APIView):
    def get_object(self, user_id):
        try:
            User.objects.get(user_id=user_id)
            return Response("Invalid", status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response("Valid", status=status.HTTP_200_OK)

    def get(self,request,format=None):
        return self.get_object(request.GET['user_id'])

class NoticeList(APIView):

    def get(self,request,format=None):
        user = Notice.objects.all()
        serializer = NoticeSerializer(user,many=True)
        return Response(serializer.data)
# class LoginList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = LoginSerializer
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('=username', '=password')