# -*- coding: utf-8 -*-
from news.models import News
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.http import Http404


def news_list(request, page=1):
    on_page = 10  # количество новостей на страницу
    items = News.objects.filter(is_active=True)  # загружаем новости из базы и фильтруем постранично
    page_object = Paginator(items, on_page)  # строим постраничную навигацию для загруженного кол-ва новостей

    try:
        curr_page_news = page_object.page(page)
    except EmptyPage:
        raise Http404()

    return render(request, 'news/news_list.html', {
        'curr_page_news': curr_page_news,
        'pages': page_object.page_range,
        'active_page': int(page),
        })


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, "news/news_detail.html", {"news": news})