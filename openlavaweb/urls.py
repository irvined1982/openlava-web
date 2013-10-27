#!/usr/bin/env python
# Copyright 2011 David Irvine
#
# This file is part of Openlava Webm
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
	url(r'^hosts/$', 'openlavaweb.views.host_list', name="host_list"),
	url(r'^hosts/(?P<host_name>.+?)/jobs$', 'openlavaweb.views.job_list', name="job_view_by_host"),
	url(r'^hosts/(.+?)$', 'openlavaweb.views.host_view', name="host_view"),
	url(r'^queues/$', 'openlavaweb.views.queue_list', name="queue_list"),
	url(r'^queues/(?P<queue_name>.+?)/jobs$', 'openlavaweb.views.job_list', name="job_view_by_queue"),
	url(r'^queues/(.+?)$', 'openlavaweb.views.queue_view', name="queue_view"),
	url(r'^jobs/$', 'openlavaweb.views.job_list', name="job_list"),
	url(r'^jobs/(\d+)$', 'openlavaweb.views.job_view', name="job_view"),
)

