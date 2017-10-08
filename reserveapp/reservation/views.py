# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from permissions import IsOwnerOrReadOnly
from django.http import Http404

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
    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)
        except Reservation.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        reservation = Reservation.objects.all()
        serializer = ReservationSerializer(reservation,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ok",status=status.HTTP_200_OK)
        return Response('No',status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        reservation = self.get_object(request.data['reservation_id'])
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ok",status=status.HTTP_200_OK)
        return Response("No",status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        reservation = self.get_object(request.query_params['reservation_id'])
        reservation.delete()
        return Response("Ok")

class InquireList(APIView):
    def get_object(self,pk):
        try:
            return Inquire.objects.get(pk=pk)
        except Inquire.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        inquire = Inquire.objects.all()
        serializer = InquireSerializer(inquire,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InquireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ok",status=status.HTTP_200_OK)
        return Response("No",status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        inquire = self.get_object(request.data['inquire_id'])
        serializer = InquireSerializer(inquire, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ok",status=status.HTTP_200_OK)
        return Response("No",status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        inquire = self.get_object(request.query_params['inquire_id'])
        inquire.delete()
        return Response("Ok")

class InquireDetailList(APIView):
    def get(self, request, pk, format=None):
        inquire = Inquire.objects.get(pk=pk)
        serializer = InquireDetailSerializer(inquire)
        return Response(serializer.data)

class CommentList(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def post(self, request, pk, fomrat=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("OK",status=status.HTTP_200_OK)
        return Response("No",status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        comment = self.get_object(request.data['comment_id'])
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Ok",status=status.HTTP_200_OK)
        return Response("No",status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(request.data['comment_id'])
        comment.delete()
        return Response("Ok")

class CheckList(APIView):
    def get_object(self, user_id):
        try:
            return Reservation.objects.get(user_id=user_id)
        except Reservation.DoesNotExist:
            return -1

    def get(self, request):
        reservation = self.get_object(request.GET['user_id'])
        if reservation == -1:
            return Response("Ok",status=status.HTTP_200_OK)
        else:
            serializer = ReservationSerializer(reservation,many=True)
            if serializer.is_valid():
                print serializer.data
                return Response(serializer.data)
            return Response(serializer.errors)