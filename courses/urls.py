from django.conf.urls import url, include

from courses import views
from courses import admin_views
import courses.api.urls

urlpatterns = [
    url(r'^$', views.course_list, name='home'),
    url(r'^list/$', views.course_list, name='list'),
    url(r'^preview/$', views.course_list_preview, name='list_preview'),
    url(r'^detail/(?P<course_id>\d+)/$', views.subscription, name='subscription'),
    url(r'^detail/(?P<course_id>\d+)/second/$', views.subscription2, name='subscription2'),
    url(r'^detail/(?P<course_id>\d+)/subscription/$', views.subscription_do, name='subscription_do'),
    url(r'^detail/(?P<course_id>\d+)/subscription_message/$', views.subscription_message,
        name='subscription_message'),
    url(r'^auth/$', views.subscription_overview,
        name='subscription_overview'),
    url(r'^auth/export/$',
        views.export_summary,
        name='export_summary'),
    url(r'^auth/export/(?P<offering_id>\d+)/$',
        views.export_offering_summary,
        name='export_offering_summary'),
    url(r'^auth/export/teacher/(?P<offering_id>\d+)/$',
        views.export_offering_teacher_payment_information,
        name='export_offering_salary'),
    url(r'^auth/courses/(?P<course_id>\d+)/$', views.course_overview,
        name='course_overview'),
    url(r'^auth/offering/(?P<offering_id>\d+)/$', views.offering_overview,
        name='offering_overview'),
    url(r'^admin/voucher_generate/$', admin_views.voucher_generation_view,
        name='voucher_generation'),
    url(r'^api/', include(courses.api.urls, namespace='api')),  # nested namespace 'api'
]
