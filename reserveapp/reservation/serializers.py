from models import *
from rest_framework import serializers

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
            'name',
            'phone',
            'email',
            'major',
            'student_id',
        )

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
        )

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = (
            'date',
            'title',
            'content',
        )

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'date',
            'period',
            'classroom',
            'user_id',
            'day',
            'name',
            'purpose',
        )

class LookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'date',
            'period',
            'classroom',
            'user_id',
            'day',
            'name',
            'purpose',
            'state',
        )

class InquireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquire
        fields = (
            'idinquire',
            # 'date',
            'user_id',
            'title',
            'content',
        )