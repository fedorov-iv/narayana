# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class NewsHook(CMSApp):
    name = u"Новости"
    urls = ["news.urls"]

apphook_pool.register(NewsHook)
