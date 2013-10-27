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

from django.http import Http404
from django.shortcuts import render
from openlava.jobs import JobList, get_job_by_id

def job_view(request,job_id):
	try:
		job=get_job_by_id(int(job_id))
	except ValueError:
		raise Http404 ("Job not found")
	return render(request, 'openlavaweb/job_detail.html', {"job": job },)

def job_list(request):
	job_list=[]
	attribute_list=['name','job_id','status','submit_time','submit_time_datetime_local','start_time','start_time_datetime_local','end_time','end_time_datetime_local',]
	try:
		for j in JobList():
			job=j.job
			row={}
			for attr in attribute_list:
				row[attr]=getattr(job,attr)
			job_list.append(row)
	except ValueError:
		pass
	return render(request, 'openlavaweb/job_list.html',{"job_list":job_list})
