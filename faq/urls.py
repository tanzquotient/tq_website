from django.conf.urls import patterns, url

from faq import views

urlpatterns = patterns('',
    url(r'^$', views.faq, name='faq'),
)