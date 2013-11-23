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
from openlava import OpenLava, OpenLavaCAPI, User, Host, Job, Queue

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

def queue_list(request):
	queue_list=OpenLava.get_queue_list()
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(queue_list,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/queue_list.html',{"queue_list":queue_list})

def queue_view(request,queue_name):
	try:
		queue=Queue(queue_name)
		job_list=OpenLava.get_job_list(queue=queue_name)
		if len(job_list)>20:
			del(job_list[20:])
	except ValueError:
		raise Http404 ("Queue not found")
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(queue,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/queue_detail.html', {"queue": queue, 'job_list':job_list },)


def host_view(request,host_name):
	try:
		host=Host(host_name)
		job_list=OpenLava.get_job_list(host=host_name)
		if len(job_list)>20:
			del(job_list[20:])
	except ValueError:
		raise Http404 ("Host not found")

	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(host,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/host_detail.html', {"host": host, 'job_list':job_list },)

def host_list(request):
	host_list=OpenLava.get_host_list()
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(host_list,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/host_list.html',{"host_list":host_list})

def user_list(request):
	user_list=OpenLava.get_user_list()
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(user_list,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/user_list.html',{"user_list":user_list})

def user_view(request,user_name):
	try:
		user=User(user_name)
		job_list=OpenLava.get_job_list(user=user_name)
		if len(job_list)>20:
			del(job_list[20:])
	except ValueError:
		raise Http404 ("User not found")

	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(user,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/user_detail.html', {"user": user, 'job_list':job_list },)

def job_view(request,job_id, array_id=0):
	job_id=int(job_id)
	array_id=int(array_id)
	try:
		job=Job(job_id=job_id, array_id=array_id)
	except ValueError:
		raise Http404 ("Job not found")
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(job,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/job_detail.html', {"job": job },)



def job_list(request, queue_name="", host_name="", user_name="all"):
	job_list=OpenLava.get_job_list(queue=queue_name,host=host_name, user=user_name)
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(job_list,cls=LavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/job_list.html',{"job_list":job_list})


def system_view(request):
	cluster_name=OpenLavaCAPI.ls_getclustername()
	master_name=OpenLavaCAPI.ls_getmastername()
	problem_hosts=[]
	for h in OpenLava.get_host_list():
		if h.status.name not in ['HOST_STAT_CU_EXCLUSIVE','HOST_STAT_EXCLUSIVE','HOST_STAT_FULL','HOST_STAT_LOCKED','HOST_STAT_WIND','HOST_STAT_OK']:
			problem_hosts.append(h)
	queue_list=OpenLava.get_queue_list()
	user_list=OpenLava.get_user_list()
	fields={
			'cluster_name':cluster_name,
			'master_name':master_name,
			'problem_hosts':problem_hosts,
			'queue_list':queue_list,
			'user_list':user_list,
			}
	return render(request, 'openlavaweb/system_view.html',fields)

