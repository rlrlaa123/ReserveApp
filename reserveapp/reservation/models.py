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
    inquire = models.ForeignKey('Inquire', models.DO_NOTHING, related_name='comment')
    user_id = models.CharField(max_length=45,default='관리자')
    date = models.DateTimeField(default=datetime.now)
    comment = models.CharField(max_length=100)

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
    inquire_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.now)
    user_id = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'inquire'
        verbose_name = '문의사항'
        verbose_name_plural = '문의사항'


class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    user_id = models.CharField(max_length=45,default='관리자')
    title = models.CharField(max_length=45)
    content = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'notice'
        verbose_name = '공지'
        verbose_name_plural = '공지'


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    date = models.DateField()
    period = models.CharField(max_length=45)
    classroom = models.CharField(max_length=45)
    state = models.IntegerField(default=2,choices=((1,'미신청'),(2,'보류'),(3,'허가'),(4,'거부')))
    day = models.CharField(max_length=45)
    purpose = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservation'
        verbose_name = '강의실 대여'
        verbose_name_plural = '강의실 대여'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    major = models.CharField(max_length=45)
    student_id = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = '유저 관리'
        verbose_name_plural = '유저 관리'
