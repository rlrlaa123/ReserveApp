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
            'reservation_id',
            'date',
            'period',
            'classroom',
            'user_id',
            'day',
            'name',
            'purpose',
            'state',
            'reject',
        )

# class LookupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reservation
#         fields = (
#             'reservation_id',
#             'date',
#             'period',
#             'classroom',
#             'user_id',
#             'day',
#             'name',
#             'purpose',
#             'state',
#         )

class InquireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquire
        fields = (
            'inquire_id',
            'date',
            'user_id',
            'title',
            'content',
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'inquire',
            'user_id',
            'date',
            'comment',
            'comment_id',
        )

class InquireDetailSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True,read_only=True)

    class Meta:
        model = Inquire
        fields = (
            'inquire_id',
            'date',
            'user_id',
            'title',
            'content',
            'comment',
        )