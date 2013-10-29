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
import json
from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from openlava.jobs import JobList, get_job_by_id
from openlava.queues import get_all_queues,get_queue_by_name
from openlava.hosts import get_all_hosts,get_host_by_name

class LavaEncoder(json.JSONEncoder):
	def default(self,obj):
		try:
			if isinstance(obj,JobList):
				items=[]
				for i in obj:
					items.append(i.job.to_dict())
				return items
			else:
				return obj.to_dict()
		except ValueError:
			pass
		return json.JSONEncoder.default(self, obj)

def process_job_list(JobList):
	attribute_list=['name','job_id','status','submit_time','submit_time_datetime_local','start_time','start_time_datetime_local','end_time','end_time_datetime_local',]
	job_list=[]
	try:
		for j in JobList:
			job=j.job
			row={}
			for attr in attribute_list:
				row[attr]=getattr(job,attr)
			job_list.append(row)
	except ValueError:
		pass
	return job_list

def queue_list(request):
	queue_list=get_all_queues()
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(queue_list,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/queue_list.html',{"queue_list":queue_list})

def queue_view(request,queue_name):
	try:
		queue=get_queue_by_name(queue_name)
		job_list=process_job_list(JobList(queue=queue_name))
		if len(job_list)>20:
			del(job_list[20:])
	except ValueError:
		raise Http404 ("Queue not found")
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(queue,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/queue_detail.html', {"queue": queue, 'job_list':job_list },)


def host_view(request,host_name):
	try:
		host=get_host_by_name(host_name)
		job_list=process_job_list(JobList(host=host_name))
		if len(job_list)>20:
			del(job_list[20:])
	except ValueError:
		raise Http404 ("Host not found")

	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(host,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/host_detail.html', {"host": host, 'job_list':job_list },)

def host_list(request):
	host_list=get_all_hosts()
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(host_list,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/host_list.html',{"host_list":host_list})

def job_view(request,job_id):
	try:
		job=get_job_by_id(int(job_id))
	except ValueError:
		raise Http404 ("Job not found")
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(job,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/job_detail.html', {"job": job },)


def job_list(request, queue_name="", host_name=""):
	if request.is_ajax() or request.GET.get("json",None):
		job_list=JobList(queue=queue_name,host=host_name)
		return HttpResponse(json.dumps(job_list,cls=LavaEncoder),content_type='application/json')
	job_list=process_job_list(JobList(queue=queue_name,host=host_name))
	return render(request, 'openlavaweb/job_list.html',{"job_list":job_list})
