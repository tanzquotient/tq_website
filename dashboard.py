"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'tq_website.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)   
        
        # helper variable
        meta_models=('courses.models.CourseType','courses.models.Style','courses.models.Period','courses.models.Room',)
        
        self.children.append(modules.ModelList(
            title='Course Administration',
            column=1,
            models=('courses.models.*'),
            exclude=('django.contrib.*',)+meta_models
        ))
        
        self.children.append(modules.ModelList(
            title='Course Administration - Meta Infos',
            column=1,
            models=meta_models
        ))

        # append an app list module for "Administration"
        self.children.append(modules.ModelList(
            _('User Administration'),
            column=1,
            collapsible=True,
            models=('django.contrib.*',),
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=6,
            column=3,
        ))

        # append another link list module for "Website".
        self.children.append(modules.LinkList(
            _('Website'),
            column=3,
            children=[
                {
                    'title': _('Go to Website'),
                    'url': '/home/',
                    'external': False,
                },
            ]
        ))
        
        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=3,
            children=[
                {
                    'title': _('Django Documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Documentation'),
                    'url': 'http://packages.python.org/django-grappelli/',
                    'external': True,
                },
                {
                    'title': _('Grappelli Google-Code'),
                    'url': 'http://code.google.com/p/django-grappelli/',
                    'external': True,
                },
            ]
        ))
