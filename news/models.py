from django.db import models
import time

# Create your models here.

class WebSiteArticle_cn(models.Model):
    id = models.BigAutoField(verbose_name = '序号', primary_key = True)
    url = models.URLField(verbose_name='链接', max_length=255, null=True)
    site_name = models.CharField(verbose_name='网站名', max_length=255, null=True)
    title = models.CharField(verbose_name='标题', max_length=100000, null=True)
    content = models.CharField(verbose_name='内容', max_length=100000, null=True)
    publish_time = models.CharField(verbose_name='出版时间', max_length=255, null=True)
    author = models.CharField(verbose_name='作者', max_length=255, null=True)
    created_at = models.CharField(max_length=10, default=time.strftime('%Y%m%d', time.localtime(time.time())))
    updated_at = models.DateTimeField(null=True)
    summarize = models.CharField(verbose_name='摘要', max_length=1000, null=True)
    class_name = models.CharField(verbose_name='文章分类', max_length=255, null=True)
    title_en = models.CharField(verbose_name='原文标题', max_length=100000, null=True)
    content_en = models.CharField(verbose_name='原文内容', max_length=100000, null=True)

class WebsiteArticle(models.Model):
    id = models.BigAutoField(verbose_name='序号', primary_key=True)
    url = models.URLField(verbose_name='链接', max_length=255, null=True)
    site_name = models.CharField(verbose_name='网站名', max_length=255, null=True)
    title = models.CharField(verbose_name='标题', max_length=100000, null=True)
    content = models.CharField(verbose_name='内容', max_length=100000, null=True)
    publish_time = models.CharField(verbose_name='出版时间', max_length=255, null=True)
    author = models.CharField(verbose_name='作者', max_length=255, null=True)
    created_at = models.CharField(max_length=10, default=time.strftime('%Y%m%d', time.localtime(time.time())))
    updated_at = models.DateTimeField(null=True)

class Summarize_week(models.Model):
    id = models.BigAutoField(verbose_name = '序号', primary_key = True)
    content = models.CharField(verbose_name='内容', max_length=100000, null=True)
    created_at = models.CharField(max_length=100, default=time.strftime('%Y%m%d', time.localtime(time.time())))
    updated_at = models.DateTimeField(null=True)

class Click_statistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=10000, null=True)
    click_id = models.CharField(max_length=10000, null=True)
    created_at = models.CharField(max_length=10, default=time.strftime('%Y%m%d', time.localtime(time.time())))
    updated_at = models.DateTimeField(null=True)

class User_analyse(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=10000, null=True)
    shijian = models.BigIntegerField(default=0)
    jishu = models.BigIntegerField(default=0)
    zhengce = models.BigIntegerField(default=0)
    yanjiu = models.BigIntegerField(default=0)
    yuce = models.BigIntegerField(default=0)