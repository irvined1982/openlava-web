#!/usr/bin/env python
# Copyright 2011 David Irvine
#
# This file is part of Openlava Web
#
# Openlava Web is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# Openlava Web is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openlava Web. If not, see <http://www.gnu.org/licenses/>.
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'openlavaweb.views.system_view', name="olw_system_view"),
                       url(r'^overview/hosts$', 'openlavaweb.views.system_overview_hosts', name="olw_system_overview_hosts"),
                       url(r'^overview/jobs$', 'openlavaweb.views.system_overview_jobs', name="olw_system_overview_jobs"),
                       url(r'^overview/slots$', 'openlavaweb.views.system_overview_slots', name="olw_system_overview_slots"),
                       url(r'^hosts/$', 'openlavaweb.views.host_list', name="olw_host_list"),
                       url(r'^hosts/(?P<host_name>.+?)/open$', 'openlavaweb.views.host_open', name="olw_host_open"),
                       url(r'^hosts/(?P<host_name>.+?)/close$', 'openlavaweb.views.host_close', name="olw_host_close"),
                       url(r'^hosts/(.+?)$', 'openlavaweb.views.host_view', name="olw_host_view"),
                       url(r'^queues/$', 'openlavaweb.views.queue_list', name="olw_queue_list"),
                       url(r'^queues/(?P<queue_name>.+?)/close$', 'openlavaweb.views.queue_close',
                           name="olw_queue_close"),
                       url(r'^queues/(?P<queue_name>.+?)/open$', 'openlavaweb.views.queue_open', name="olw_queue_open"),
                       url(r'^queues/(?P<queue_name>.+?)/inactivate$', 'openlavaweb.views.queue_inactivate',
                           name="olw_queue_inactivate"),
                       url(r'^queues/(?P<queue_name>.+?)/activate$', 'openlavaweb.views.queue_activate',
                           name="olw_queue_activate"),
                       url(r'^queues/(.+?)$', 'openlavaweb.views.queue_view', name="olw_queue_view"),
                       url(r'^jobs/(?P<job_id>\d+)/$', 'openlavaweb.views.job_list', name="olw_job_list"),
                       url(r'^jobs/$', 'openlavaweb.views.job_list', name="olw_job_list"),
                       url(r'^job/submit$', 'openlavaweb.views.job_submit', name="olw_job_submit"),
                       url(r'^job/submit/(?P<form_class>.+)$', 'openlavaweb.views.job_submit', name="olw_job_submit_class"),
                       url(r'^job/(\d+)$', 'openlavaweb.views.job_view', name="olw_job_view"),
                       url(r'^job/(\d+)/(\d+)$', 'openlavaweb.views.job_view', name="olw_job_view_array"),
                       url(r'^job/(\d+)/(\d+)/output$', 'openlavaweb.views.job_output', name="olw_job_output"),
                       url(r'^job/(\d+)/(\d+)/error$', 'openlavaweb.views.job_error', name="olw_job_error"),
                       url(r'^job/(\d+)/(\d+)/kill$', 'openlavaweb.views.job_kill', name="olw_job_kill"),
                       url(r'^job/(\d+)/(\d+)/suspend$', 'openlavaweb.views.job_suspend', name="olw_job_suspend"),
                       url(r'^job/(\d+)/(\d+)/resume$', 'openlavaweb.views.job_resume', name="olw_job_resume"),
                       url(r'^job/(\d+)/(\d+)/requeue$', 'openlavaweb.views.job_requeue', name="olw_job_requeue"),
                       url(r'^get_token$', 'openlavaweb.views.get_csrf_token', name="get_token"),
                       url(r'^users/$', 'openlavaweb.views.user_list', name="olw_user_list"),
                       url(r'^users/(.+?)$', 'openlavaweb.views.user_view', name="olw_user_view"),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'openlavaweb/login.html'}, name="olw_login"),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
                           {'template_name': 'openlavaweb/logout.html'}, name="olw_logout"),
                       url(r'^accounts/ajax_login$', 'openlavaweb.views.ajax_login', name="olw_ajax_login"),
)


