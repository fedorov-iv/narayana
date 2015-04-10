# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class FeedbackHook(CMSApp):
    name = u"Форма обратной связи"
    urls = ["feedback.urls"]

apphook_pool.register(FeedbackHook)
