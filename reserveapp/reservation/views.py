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
    def get_object(self, pk, password):
        try:
            return User.objects.get(pk=pk,password=password)
        except User.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        self.get_object(request.data['user_id'],request.data['password'])

        return Response("Ok", status=status.HTTP_200_OK)