# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    inquire = models.ForeignKey('Inquire', models.DO_NOTHING, related_name='comment', verbose_name='문의내용')
    user_id = models.CharField(max_length=45, default='관리자', verbose_name='글쓴이')
    date = models.DateTimeField(default=datetime.now, verbose_name='날짜')
    comment = models.TextField(max_length=500, verbose_name='리뷰')

    class Meta:
        managed = False
        db_table = 'comment'
        verbose_name = '문의사항 댓글 관리'
        verbose_name_plural = '문의 사항 댓글'
    # def __unicode__(self):
    #     return [self.user_id,self.comment,self.date]
    #
        #  '[%s,%s,%s]' % (self.user_id, self.comment, self.date)


class Inquire(models.Model):
    inquire_id = models.AutoField(primary_key=True, verbose_name='문의내용')
    date = models.DateTimeField(default=datetime.now, verbose_name='날짜')
    user_id = models.CharField(max_length=45, verbose_name='글쓴이')
    title = models.CharField(max_length=45, verbose_name='제목')
    content = models.CharField(max_length=45, verbose_name='내용')

    class Meta:
        managed = False
        db_table = 'inquire'
        verbose_name = '문의사항'
        verbose_name_plural = '문의사항'


class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(verbose_name='날짜')
    user_id = models.CharField(max_length=45, default='관리자', verbose_name='글쓴이')
    title = models.CharField(max_length=45, verbose_name='제목')
    content = models.TextField(max_length=45, verbose_name='내용')

    class Meta:
        managed = False
        db_table = 'notice'
        verbose_name = '공지'
        verbose_name_plural = '공지'


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=45, verbose_name='아이디')
    name = models.CharField(max_length=45, verbose_name='예약이름')
    date = models.DateField(verbose_name='날짜')
    period = models.CharField(max_length=45, verbose_name='교시')
    classroom = models.CharField(max_length=45, verbose_name='강의실')
    state = models.IntegerField(default=2,choices=((1,'미신청'),(2,'보류'),(3,'허가'),(4,'거부')), verbose_name='예약상태')
    day = models.CharField(max_length=45, verbose_name='요일')
    purpose = models.TextField(max_length=100, blank=True, null=True, verbose_name='사용목적')
    reject = models.TextField(max_length=100, blank=True, null=True, verbose_name='거부이유')

    class Meta:
        managed = False
        db_table = 'reservation'
        verbose_name = '강의실 대여'
        verbose_name_plural = '강의실 대여'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=45, verbose_name='아이디')
    password = models.CharField(max_length=45, verbose_name='비밀번호')
    name = models.CharField(max_length=45, verbose_name='이름')
    phone = models.CharField(max_length=45, verbose_name='휴대폰')
    email = models.CharField(max_length=45 ,verbose_name='이메일')
    major = models.CharField(max_length=45, verbose_name='전공')
    student_id = models.CharField(unique=True, max_length=45, verbose_name='학번')

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = '유저 관리'
        verbose_name_plural = '유저 관리'
