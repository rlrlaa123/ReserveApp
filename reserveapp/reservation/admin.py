# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# 출력할 ResourceAdmin 클래스를 만든다
class UserAdmin(admin.ModelAdmin):
  list_display = ('user_id', 'password','name','phone','email','major','student_id')

class NoticeAdmin(admin.ModelAdmin):
  list_display = ('date','title','content')

class ReservationAdmin(admin.ModelAdmin):
  list_display = ('reservation_id','user_id','name','date','period','classroom','state','day','purpose')

class InquireAdmin(admin.ModelAdmin):
    list_display = ('inquire_id','date','user_id','title','content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id','date','comment')

# 클래스를 어드민 사이트에 등록한다.
admin.site.register(User, UserAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Inquire, InquireAdmin)
admin.site.register(Comment, CommentAdmin)