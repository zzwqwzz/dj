import json
import requests
from django.http import JsonResponse
from django.shortcuts import render
import time
from news.models import WebSiteArticle_cn, Summarize_week, User_analyse, Click_statistics
from news.utils.pagination import Pagination

data = time.strftime('%Y%m%d', time.localtime(time.time()))
# Create your views here.

def sum_week(request):
    all_data = Summarize_week.objects.all().order_by('-created_at')
    pagination = Pagination(request, 'page', all_data, time_data='', search_data='', page_size=5)
    values = pagination.page_queryset.values()
    for i in range(len(values)):
        content = values[i]['content']
        content = content.split('\n')
        values[i]['content'] = content
    return render(request, 'sum_week.html', {'all_data': values, 'count': pagination.total, 'page_html_string': pagination.html(), 'date': data})

def agdaily(request):
    all_data = WebSiteArticle_cn.objects.filter(site_name='agdaily')
    #标题搜索
    search_filter = {}
    search_data = request.GET.get('search')
    if search_data:
        search_filter['title__contains'] = search_data
        search_filter['title_en__contains'] = search_data
    else:
        search_data = ''
    #时间筛选
    time_filter = {}
    time_data = request.GET.get('time')
    temp_list = []
    if time_data == '0':
        for i in range(1):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '1':
        for i in range(3):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '2':
        for i in range(7):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '3':
        for i in range(30):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '4':
        for i in range(365):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '5':
        pass
    else:
        time_data = '5'
    time_select_data = all_data.filter(**time_filter)
    search_select_data = time_select_data.filter(**search_filter).order_by('-created_at', 'title')
    t = list(search_select_data.values())
    #分页显示
    pagination = Pagination(request, 'page', search_select_data, search_data=search_data, time_data=time_data)
    return render(request, 'article_list.html', {'all_data': pagination.page_queryset, 'count': pagination.total, 'search_data': search_data, 'time_data': time_data, 'page_html_string': pagination.html()})

def agriculture(request):
    all_data = WebSiteArticle_cn.objects.filter(site_name='agriculture')
    #标题搜索
    search_filter = {}
    search_data = request.GET.get('search')
    if search_data:
        search_filter['title__contains'] = search_data
        search_filter['title_en__contains'] = search_data
    else:
        search_data = ''
    #时间筛选
    time_filter = {}
    time_data = request.GET.get('time')
    temp_list = []
    if time_data == '0':
        for i in range(1):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '1':
        for i in range(3):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '2':
        for i in range(7):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '3':
        for i in range(30):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '4':
        for i in range(365):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '5':
        pass
    else:
        time_data = '5'
    time_select_data = all_data.filter(**time_filter)
    search_select_data = time_select_data.filter(**search_filter).order_by('-created_at', 'title')
    t = list(search_select_data.values())
    #分页显示
    pagination = Pagination(request, 'page', search_select_data, search_data=search_data, time_data=time_data)
    return render(request, 'article_list.html', {'all_data': pagination.page_queryset, 'count': pagination.total, 'search_data': search_data, 'time_data': time_data, 'page_html_string': pagination.html()})

def agropages(request):
    all_data = WebSiteArticle_cn.objects.filter(site_name='agropages')
    #标题搜索
    search_filter = {}
    search_data = request.GET.get('search')
    if search_data:
        search_filter['title__contains'] = search_data
        search_filter['title_en__contains'] = search_data
    else:
        search_data = ''
    #时间筛选
    time_filter = {}
    time_data = request.GET.get('time')
    temp_list = []
    if time_data == '0':
        for i in range(1):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '1':
        for i in range(3):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '2':
        for i in range(7):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '3':
        for i in range(30):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '4':
        for i in range(365):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '5':
        pass
    else:
        time_data = '5'
    time_select_data = all_data.filter(**time_filter)
    search_select_data = time_select_data.filter(**search_filter).order_by('-created_at', 'title')
    t = list(search_select_data.values())
    #分页显示
    pagination = Pagination(request, 'page', search_select_data, search_data=search_data, time_data=time_data)
    return render(request, 'article_list.html', {'all_data': pagination.page_queryset, 'count': pagination.total, 'search_data': search_data, 'time_data': time_data, 'page_html_string': pagination.html()})

def agupdate(request):
    all_data = WebSiteArticle_cn.objects.filter(site_name='agupdate')
    #标题搜索
    search_filter = {}
    search_data = request.GET.get('search')
    if search_data:
        search_filter['title__contains'] = search_data
        search_filter['title_en__contains'] = search_data
    else:
        search_data = ''
    #时间筛选
    time_filter = {}
    time_data = request.GET.get('time')
    temp_list = []
    if time_data == '0':
        for i in range(1):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '1':
        for i in range(3):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '2':
        for i in range(7):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '3':
        for i in range(30):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '4':
        for i in range(365):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '5':
        pass
    else:
        time_data = '5'
    time_select_data = all_data.filter(**time_filter)
    search_select_data = time_select_data.filter(**search_filter).order_by('-created_at', 'title')
    t = list(search_select_data.values())
    #分页显示
    pagination = Pagination(request, 'page', search_select_data, search_data=search_data, time_data=time_data)
    return render(request, 'article_list.html', {'all_data': pagination.page_queryset, 'count': pagination.total, 'search_data': search_data, 'time_data': time_data, 'page_html_string': pagination.html()})

def asiapathways(request):
    all_data = WebSiteArticle_cn.objects.filter(site_name='asiapathways')
    #标题搜索
    search_filter = {}
    search_data = request.GET.get('search')
    if search_data:
        search_filter['title__contains'] = search_data
        search_filter['title_en__contains'] = search_data
    else:
        search_data = ''
    #时间筛选
    time_filter = {}
    time_data = request.GET.get('time')
    temp_list = []
    if time_data == '0':
        for i in range(1):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '1':
        for i in range(3):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '2':
        for i in range(7):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '3':
        for i in range(30):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '4':
        for i in range(365):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '5':
        pass
    else:
        time_data = '5'
    time_select_data = all_data.filter(**time_filter)
    search_select_data = time_select_data.filter(**search_filter).order_by('-created_at', 'title')
    t = list(search_select_data.values())
    #分页显示
    pagination = Pagination(request, 'page', search_select_data, search_data=search_data, time_data=time_data)
    return render(request, 'article_list.html', {'all_data': pagination.page_queryset, 'count': pagination.total, 'search_data': search_data, 'time_data': time_data, 'page_html_string': pagination.html()})

def bbc(request):
    print(request)
    all_data = WebSiteArticle_cn.objects.filter(site_name='bbc')
    #标题搜索
    search_filter = {}
    search_data = request.GET.get('search')
    if search_data:
        search_filter['title__contains'] = search_data
        search_filter['title_en__contains'] = search_data
    else:
        search_data = ''
    #时间筛选
    time_filter = {}
    time_data = request.GET.get('time')
    temp_list = []
    if time_data == '0':
        for i in range(1):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '1':
        for i in range(3):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '2':
        for i in range(7):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '3':
        for i in range(30):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '4':
        for i in range(365):
            temp_list.append(int(data) - i)
        time_filter['created_at__in'] = temp_list
    elif time_data == '5':
        pass
    else:
        time_data = '5'
    time_select_data = all_data.filter(**time_filter)
    search_select_data = time_select_data.filter(**search_filter).order_by('-created_at', 'title')
    t = list(search_select_data.values())
    #分页显示
    pagination = Pagination(request, 'page', search_select_data, search_data=search_data, time_data=time_data)
    return render(request, 'article_list.html', {'all_data': pagination.page_queryset, 'count': pagination.total, 'search_data': search_data, 'time_data': time_data, 'page_html_string': pagination.html()})

def detail(request):
    print(request)
    user = User_analyse.objects.filter(username=request.user)
    id = request.GET.get('id')
    data = WebSiteArticle_cn.objects.filter(id = id)[0]
    Click_statistics.objects.create(username=request.user, click_id=id)
    if data.class_name == '政策':
        if user:
            User_analyse.objects.filter(username=request.user).update(zhengce=user[0].zhengce + 1)
        else:
            User_analyse.objects.create(username=request.user)
            User_analyse.objects.filter(username=request.user).update(zhengce=1)
    elif data.class_name == '事件':
        if user:
            User_analyse.objects.filter(username=request.user).update(shijian=user[0].shijian + 1)
        else:
            User_analyse.objects.create(username=request.user)
            User_analyse.objects.filter(username=request.user).update(shijian=1)
    elif data.class_name == '研究':
        if user:
            User_analyse.objects.filter(username=request.user).update(yanjiu=user[0].yanjiu + 1)
        else:
            User_analyse.objects.create(username=request.user)
            User_analyse.objects.filter(username=request.user).update(yanjiu=1)
    elif data.class_name == '预测':
        if user:
            User_analyse.objects.filter(username=request.user).update(yuce=user[0].yuce + 1)
        else:
            User_analyse.objects.create(username=request.user)
            User_analyse.objects.filter(username=request.user).update(yuce=1)
    elif data.class_name == '技术':
        if user:
            User_analyse.objects.filter(username=request.user).update(jishu=user[0].jishu + 1)
        else:
            User_analyse.objects.create(username=request.user)
            User_analyse.objects.filter(username=request.user).update(jishu=1)
    content = data.content.split('\n')

    return render(request, 'article_detail.html', {'data': data, 'content': content})