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
import json
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
from openlava import OpenLava, OpenLavaCAPI, User, Host, Job, Queue, OpenLavaEncoder

def queue_list(request):
	queue_list=OpenLava.get_queue_list()
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(queue_list,sort_keys=True, indent=3, cls=OpenLavaEncoder),content_type='application/json')
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
		return HttpResponse(json.dumps(queue,sort_keys=True, indent=3, cls=OpenLavaEncoder),content_type='application/json')
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
		return HttpResponse(json.dumps(host, sort_keys=True, indent=3, cls=OpenLavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/host_detail.html', {"host": host, 'job_list':job_list },)

def host_list(request):
	host_list=OpenLava.get_host_list()
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(host_list, sort_keys=True, indent=3, cls=OpenLavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/host_list.html',{"host_list":host_list})

def user_list(request):
	user_list=OpenLava.get_user_list()
	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(user_list, sort_keys=True, indent=3, cls=OpenLavaEncoder),content_type='application/json')
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
		return HttpResponse(json.dumps(user, sort_keys=True, indent=3, cls=OpenLavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/user_detail.html', {"oluser": user, 'job_list':job_list },)

def job_kill(request,job_id, array_id=0):
	job_id=int(job_id)
	array_id=int(array_id)
	try:
		job=Job(job_id=job_id, array_id=array_id)
	except ValueError:
		raise Http404 ("Job not found")
	if request.user not in job.admins:
		return HttpResponseForbidden("User: %s is not a job admin" % request.user)
	if request.GET.get('confirm', None):
		if job.kill()==0:
			return HttpResponseRedirect(reverse("olw_job_list"))
		else:
			return HttpResponseRedirect(reverse("olw_job_view_array", args=[str(job.job_id), str(job.array_id)]))

	elif request.is_ajax() or request.GET.get("json",None):
		if job.kill()==0:
			data={'status':'OK'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data={'status':'FAIL'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		return render(request, 'openlavaweb/job_kill_confirm.html', {"object": job})

def job_suspend(request,job_id, array_id=0):
	job_id=int(job_id)
	array_id=int(array_id)
	try:
		job=Job(job_id=job_id, array_id=array_id)
	except ValueError:
		raise Http404 ("Job not found")
	if request.user not in job.admins:
		return HttpResponseForbidden("User: %s is not a job admin" % request.user)
	if request.GET.get('confirm', None):
		if job.suspend()==0:
			return HttpResponseRedirect(reverse("olw_job_view_array", args=[str(job.job_id), str(job.array_id)]))
		else:
			return HttpResponseRedirect(reverse("olw_job_view_array", args=[str(job.job_id), str(job.array_id)]))

	elif request.is_ajax() or request.GET.get("json",None):
		if job.suspend()==0:
			data={'status':'OK'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data={'status':'FAIL'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		return render(request, 'openlavaweb/job_suspend_confirm.html', {"object": job})

def job_resume(request,job_id, array_id=0):
	job_id=int(job_id)
	array_id=int(array_id)
	try:
		job=Job(job_id=job_id, array_id=array_id)
	except ValueError:
		raise Http404 ("Job not found")
	if request.user not in job.admins:
		return HttpResponseForbidden("User: %s is not a job admin" % request.user)
	if request.GET.get('confirm', None):
		if job.resume()==0:
			return HttpResponseRedirect(reverse("olw_job_view_array", args=[str(job.job_id), str(job.array_id)]))
		else:
			return HttpResponseRedirect(reverse("olw_job_view_array", args=[str(job.job_id), str(job.array_id)]))

	elif request.is_ajax() or request.GET.get("json",None):
		if job.resume()==0:
			data={'status':'OK'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data={'status':'FAIL'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		return render(request, 'openlavaweb/job_resume_confirm.html', {"object": job})



def job_requeue(request,job_id, array_id=0):
	job_id=int(job_id)
	array_id=int(array_id)
	hold=False
	if request.GET.get("hold",False):
		hold=True

	try:
		job=Job(job_id=job_id, array_id=array_id)
	except ValueError:
		raise Http404 ("Job not found")
	if request.user not in job.admins:
		return HttpResponseForbidden("User: %s is not a job admin" % request.user)
	if request.GET.get('confirm', None):
		if job.requeue(hold=hold) == 0:
			return HttpResponseRedirect(reverse("olw_job_view_array", args=[str(job.job_id), str(job.array_id)]))
		else:
			return HttpResponseRedirect(reverse("olw_job_view_array", args=[str(job.job_id), str(job.array_id)]))
	elif request.is_ajax() or request.GET.get("json",None):
		if job.requeue(hold=hold):
			data={'status':'OK'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data={'status':'FAIL'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		return render(request, 'openlavaweb/job_requeue_confirm.html', {"object": job})

def job_view(request,job_id, array_id=0):
	job_id=int(job_id)
	array_id=int(array_id)
	try:
		job=Job(job_id=job_id, array_id=array_id)
	except ValueError:
		raise Http404 ("Job not found")
	if request.is_ajax() or request.GET.get("json",None):
		jobdict=job.to_dict()
		jobdict['execution_hosts']=get_execution_hosts(job)
		return HttpResponse(json.dumps(jobdict,sort_keys=True, indent=3, cls=OpenLavaEncoder),content_type='application/json')
	return render(request, 'openlavaweb/job_detail.html', {"job": job, },)

def get_execution_hosts(job):
	hosts={}
	for host in job.execution_hosts:
		if host not in hosts:
			hosts[host]={
				'host':host,
				'url':reverse("olw_host_view", args=[host]),
				'num_slots':0,
				}
		hosts[host]['num_slots']+=1
	return hosts.values()


def job_list(request, queue_name="", host_name="", user_name="all"):
	job_list=OpenLava.get_job_list(queue=queue_name,host=host_name, user=user_name)

	if request.is_ajax() or request.GET.get("json",None):
		return HttpResponse(json.dumps(job_list, sort_keys=True, indent=3, cls=OpenLavaEncoder),content_type='application/json')

	paginator = Paginator(job_list, 25)
	page = request.GET.get('page')
	try:
		job_list = paginator.page(page)
	except PageNotAnInteger:
		job_list= paginator.page(1)
	except EmptyPage:
		job_list=paginator.page(paginator.num_pages)
	return render(request, 'openlavaweb/job_list.html',{"job_list":job_list, })


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


def job_submit(request):
	form = JobSubmitForm()
	return render( request, 'openlavaweb/job_submit.html', {'form':form})

class JobSubmitForm(forms.Form):
	# options....
	opts=[
			(0x40, "Exclusive"),
			(0x4000, "Re-Runnable"),
			]

	options=forms.MultipleChoiceField(choices=opts, required=False)
	num_processors=forms.IntegerField(initial=1)
	command=forms.CharField(widget=forms.TextArea, max_length=512)
	job_name=forms.CharField(max_length=512, required=False)
	queues=[(u'', u'Default') ]
	for q in OpenLava.get_queue_list():
		queues.append([q.name, q.name])
	queue_name=forms.ChoiceField(choices=queues, required=False)
	hosts=[]
	for h in OpenLava.get_host_list():
		hosts.append([h.name, h.name])
	requested_hosts=forms.MultipleChoiceField(choices=hosts, required=False )
	resource_request=forms.CharField(max_length=512, required=False)
	## Rlimits
	host_specification=forms.CharField(max_length=512, required=False)
	dependency_conditions=forms.CharField(max_length=512, required=False)
	begin_time=forms.DateTimeField(required=False)
	term_time=forms.DateTimeField(required=False)
	signal_value=forms.IntegerField(required=False)
	input_file=forms.CharField(max_length=512, required=False)
	output_file=forms.CharField(max_length=512, required=False)
	error_file=forms.CharField(max_length=512, required=False)
	checkpoint_period=forms.CharField(max_length=512, required=False)
	checkpoint_directory=forms.CharField(max_length=512, required=False)
	email_user=forms.EmailField(required=False)
	project_name=forms.CharField(max_length=128, required=False)
	max_num_processors=forms.IntegerField(required=False)
	login_shell=forms.CharField(128, required=False)
	priority=forms.IntegerField(required=False)



