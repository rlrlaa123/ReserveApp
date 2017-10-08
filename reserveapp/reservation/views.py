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
        return Response("No", status=status.HTTP_400_BAD_REQUEST)

class LoginList(APIView):
    def get_object(self, user_id, password):
        try:
            User.objects.get(user_id=user_id,password=password)
            return Response("Ok", status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response("No", status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        return self.get_object(request.GET['user_id'],request.GET['password'])

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

class ReservationList(APIView):
    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ok",status=status.HTTP_200_OK)
        return Response('No',status=status.HTTP_400_BAD_REQUEST)

class LookupList(APIView):
    def get(self, request, format=None):
        reservation = Reservation.objects.all()
        serializer = LookupSerializer(reservation,many=True)
        return Response(serializer.data)

class InquireList(APIView):
    def post(self, request, format=None):
        serializer = InquireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ok",status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class InquireLookupList(APIView):
    def get(self, request, format=None):
        inquire = Inquire.objects.all()
        serializer = InquireSerializer(inquire,many=True)
        return Response(serializer.data)