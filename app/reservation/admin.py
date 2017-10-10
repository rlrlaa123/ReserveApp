# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class SeminarInline(admin.StackedInline):
    model = Reservation
    extra = 0
    ordering = ('state',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','name','phone','email','major','student_id')

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title','user_id','date','content')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name','user_id','date','period','classroom','state','day','purpose','reject')
    list_editable = ('state',)

class InquireAdmin(admin.ModelAdmin):
    list_display = ('title','user_id','date','content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('inquire_title','user_id','date','comment')

    def inquire_title(self, obj):
        return obj.inquire.title
    inquire_title.short_description = '문의내용'

    raw_id_fields = ('inquire',)



# 클래스를 어드민 사이트에 등록한다.
admin.site.register(User, UserAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Inquire, InquireAdmin)
admin.site.register(Comment, CommentAdmin)