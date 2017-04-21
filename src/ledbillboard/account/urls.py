# -*- coding: utf-8 -*-
from django.conf.urls import url
from ledbillboard.account.views import AjaxLoginView

urlpatterns = [
    url(r'^ajax_login$', AjaxLoginView.as_view(), name='ajax_login_view'),
]
