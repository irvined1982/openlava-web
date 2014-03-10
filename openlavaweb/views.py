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
import os
import pwd
import sys
import datetime
from multiprocessing import Process as MPProcess
from multiprocessing import Queue as MPQueue
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from cluster import ClusterException
from cluster.openlavacluster import Cluster, Host, Job, Queue, User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token


def queue_list(request):
    queue_list = Queue.get_queue_list()
    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(queue_list, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type='application/json')
    return render(request, 'openlavaweb/queue_list.html', {"queue_list": queue_list})


def queue_view(request, queue_name):
    try:
        queue = Queue(queue_name)
    except ValueError:
        raise Http404("Queue not found")
    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(queue, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type='application/json')
    return render(request, 'openlavaweb/queue_detail.html', {"queue": queue, 'job_list': job_list}, )


@login_required
def queue_close(request, queue_name):
    queue_name = str(queue_name)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'queue_name': queue_name,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_queue_close, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, ClusterException):
                print "exception: ", rc
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        queue = Queue(queue=queue_name)
        return render(request, 'openlavaweb/queue_close_confirm.html', {"object": queue})


def execute_queue_close(request, queue, queue_name):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        q = Queue(queue=queue_name)
        q.close()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_queue_view", kwargs={'queue_name': queue_name})))
    except Exception as e:
        queue.put(e)


@login_required
def queue_open(request, queue_name):
    queue_name = str(queue_name)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'queue_name': queue_name,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_queue_open, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        queue = Queue(queue=queue_name)
        return render(request, 'openlavaweb/queue_open_confirm.html', {"object": queue})


def execute_queue_open(request, queue, queue_name):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        q = Queue(queue=queue_name)
        q.open()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_queue_view", kwargs={'queue_name': queue_name})))
    except Exception as e:
        queue.put(e)


@login_required
def queue_inactivate(request, queue_name):
    queue_name = str(queue_name)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'queue_name': queue_name,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_queue_inactivate, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        queue = Queue(queue=queue_name)
        return render(request, 'openlavaweb/queue_inactivate_confirm.html', {"object": queue})


def execute_queue_inactivate(request, queue, queue_name):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        q = Queue(queue=queue_name)
        q.inactivate()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_queue_view", kwargs={'queue_name': queue_name})))
    except Exception as e:
        queue.put(e)


@login_required
def queue_activate(request, queue_name):
    queue_name = str(queue_name)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'queue_name': queue_name,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_queue_activate, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        queue = Queue(queue=queue_name)
        return render(request, 'openlavaweb/queue_activate_confirm.html', {"object": queue})


def execute_queue_activate(request, queue, queue_name):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        q = Queue(queue=queue_name)
        q.activate()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_queue_view", kwargs={'queue_name': queue_name})))
    except Exception as e:
        queue.put(e)


def host_view(request, host_name):
    try:
        host = Host(host_name)
    except NoSuchHostError:
        raise Http404("Host not found")

    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(host, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type='application/json')
    return render(request, 'openlavaweb/host_detail.html', {"host": host}, )


@login_required
def host_close(request, host_name):
    host_name = str(host_name)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'host_name': host_name,
                'request': request,
                'queue': q,
            }
            print "Executing"
            p = MPProcess(target=execute_host_close, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            print "executed"
            print type(rc)
            if isinstance(rc, ClusterException):
                print "exception: ", rc
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        host = Host(host_name)
        return render(request, 'openlavaweb/host_close_confirm.html', {"object": host})


def execute_host_close(request, queue, host_name):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        h = Host(host_name)
        h.close()

        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_host_view", args=[host_name])))
    except Exception as e:
        queue.put(e)


@login_required
def host_open(request, host_name):
    host_name = str(host_name)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'host_name': host_name,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_host_open, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        host = Host(host_name)
        return render(request, 'openlavaweb/host_open_confirm.html', {"object": host})


def execute_host_open(request, queue, host_name):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        h = Host(host_name)
        h.open()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_host_view", args=[host_name])))
    except Exception as e:
        queue.put(e)


def host_list(request):
    host_list = Host.get_host_list()
    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(host_list, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type='application/json')

    paginator = Paginator(host_list, 25)
    page = request.GET.get('page')
    try:
        host_list = paginator.page(page)
    except PageNotAnInteger:
        host_list = paginator.page(1)
    except EmptyPage:
        host_list = paginator.page(paginator.num_pages)
    return render(request, 'openlavaweb/host_list.html', {"host_list": host_list})


def user_list(request):
    user_list = User.get_user_list()
    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(user_list, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type='application/json')
    paginator = Paginator(user_list, 25)
    page = request.GET.get('page')
    try:
        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)
    return render(request, 'openlavaweb/user_list.html', {"user_list": user_list})


def user_view(request, user_name):
    try:
        user = User(user_name)
    except ValueError:
        raise Http404("User not found")
    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(user, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type='application/json')
    return render(request, 'openlavaweb/user_detail.html', {"oluser": user, 'job_list': job_list}, )



@login_required
def job_kill(request, job_id, array_index=0):
    job_id = int(job_id)
    array_index = int(array_index)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'job_id': job_id,
                'array_index': array_index,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_job_kill, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        job = Job(job_id=job_id, array_index=array_index)
        return render(request, 'openlavaweb/job_kill_confirm.html', {"object": job})


def execute_job_kill(request, queue, job_id, array_index):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        job = Job(job_id=job_id, array_index=array_index)
        job.kill()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_job_list")))
    except Exception as e:
        queue.put(e)


@login_required
def job_suspend(request, job_id, array_index=0):
    job_id = int(job_id)
    array_index = int(array_index)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'job_id': job_id,
                'array_index': array_index,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_job_suspend, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        job = Job(job_id=job_id, array_index=array_index)
        return render(request, 'openlavaweb/job_suspend_confirm.html', {"object": job})


def execute_job_suspend(request, queue, job_id, array_index):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        job = Job(job_id=job_id, array_index=array_index)
        job.suspend()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_job_view_array", args=[job_id, array_index])))
    except Exception as e:
        queue.put(e)


@login_required
def job_suspend(request, job_id, array_index=0):
    job_id = int(job_id)
    array_index = int(array_index)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'job_id': job_id,
                'array_index': array_index,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_job_suspend, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        job = Job(job_id=job_id, array_index=array_index)
        return render(request, 'openlavaweb/job_suspend_confirm.html', {"object": job})


def execute_job_suspend(request, queue, job_id, array_index):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        job = Job(job_id=job_id, array_index=array_index)
        job.suspend()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_job_view_array", args=[job_id, array_index])))
    except Exception as e:
        queue.put(e)


@login_required
def job_resume(request, job_id, array_index=0):
    job_id = int(job_id)
    array_index = int(array_index)
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:
            q = MPQueue()
            kwargs = {
                'job_id': job_id,
                'array_index': array_index,
                'request': request,
                'queue': q,
            }
            p = MPProcess(target=execute_job_resume, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        job = Job(job_id=job_id, array_index=array_index)
        return render(request, 'openlavaweb/job_resume_confirm.html', {"object": job})


def execute_job_resume(request, queue, job_id, array_index):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        job = Job(job_id=job_id, array_index=array_index)
        job.resume()
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_job_view_array", args=[job_id, array_index])))
    except Exception as e:
        queue.put(e)


@login_required
def job_requeue(request, job_id, array_index=0):
    job_id = int(job_id)
    array_index = int(array_index)
    hold = False
    if request.GET.get("hold", False):
        hold = True
    if request.GET.get('confirm', None) or request.is_ajax() or request.GET.get("json", None):
        try:

            q = MPQueue()
            kwargs = {
                'job_id': job_id,
                'array_index': array_index,
                'request': request,
                'queue': q,
                'hold': hold,
            }
            p = MPProcess(target=execute_job_requeue, kwargs=kwargs)
            p.start()
            p.join()
            rc = q.get(False)
            if isinstance(rc, Exception):
                raise rc
            else:
                return rc
        except ClusterException as e:
            if request.is_ajax() or request.GET.get("json", None):
                return HttpResponse(e.to_json(), content_type='application/json')
            else:
                return render(request, 'openlavaweb/exception.html', {'exception': e})
    else:
        job = Job(job_id=job_id, array_index=array_index)
        return render(request, 'openlavaweb/job_requeue_confirm.html', {"object": job, 'hold': hold})


def execute_job_requeue(request, queue, job_id, array_index, hold):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        job = Job(job_id=job_id, array_index=array_index)
        job.requeue(hold=hold)
        if request.is_ajax():
            queue.put(HttpResponse(json.dumps({'status': "OK"}), content_type="application/json"))
        else:
            queue.put(HttpResponseRedirect(reverse("olw_job_view_array", args=[job_id, array_index])))
    except Exception as e:
        queue.put(e)

def execute_get_output_path(queue, job_id, array_index):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        job = Job(job_id=job_id, array_index=array_index)
        queue.put(job.get_output_path())
    except Exception as e:
        queue.put(e)

def job_output(request, job_id, array_index=0):
    job_id = int(job_id)
    array_index = int(array_index)
    try:
        q = MPQueue()
        kwargs = {
            'job_id': job_id,
            'array_index': array_index,
            'request': request,
            'queue': q,
        }
        p = MPProcess(target=execute_get_output_path, kwargs=kwargs)
        p.start()
        p.join()
        path = q.get(False)
        if isinstance(path, Exception):
            raise path
        if path:
            f=open(path,'r')
            return HttpResponse(f, mimetype="text/plain")
        else:
            return HttpResponse("Not Available", mimetype=="text/plain")

    except ClusterException as e:
        if request.is_ajax() or request.GET.get("json", None):
            return HttpResponse(e.to_json(), content_type='application/json')
        else:
            return render(request, 'openlavaweb/exception.html', {'exception': e})


class ClusterEncoder(json.JSONEncoder):
    def check(self, obj):
        if isinstance(obj, Host):
            return {
                'type': "Host",
                'name': obj.name,
                'url': reverse("olw_host_view", args=[obj.name]),
            }
        if isinstance(obj, Job):
            return {
                'type': "Job",
                'name': obj.name,
                'job_id': obj.job_id,
                'array_index': obj.array_index,
                'url': reverse("olw_job_view_array", args=[obj.job_id, obj.array_index]),
                'user_name': obj.user_name,
                'user_url': reverse("olw_user_view", args=[obj.user_name]),
                'status': obj.status,
                'submit_time': obj.submit_time,
                'start_time': obj.start_time,
                'end_time': obj.end_time,
            }
        if isinstance(obj, Queue):
            return {
                'type': "Queue",
                'name': obj.name,
                'url': reverse("olw_queue_view", args=[obj.name]),
            }
        return obj

    def default(self, obj):
        if isinstance(obj, datetime.timedelta):
            return obj.total_seconds()

        d = {}
        d['type'] = obj.__class__.__name__
        for name in obj.json_attributes():
            value = getattr(obj, name)
            if hasattr(value, '__call__'):
                value = value()
            if isinstance(value, list):
                value = [self.check(i) for i in value]
            else:
                value = self.check(value)

            d[name] = value
        return d



def job_view(request, job_id, array_index=0):
    job_id = int(job_id)
    array_index = int(array_index)
    try:
        job = Job(job_id=job_id, array_index=array_index)
    except ClusterException as e:
        if request.is_ajax() or request.GET.get("json", None):
            return HttpResponse(e.to_json(), content_type='application/json')
        else:
            return render(request, 'openlavaweb/exception.html', {'exception': e})

    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(job, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type="application/json")
    else:
        return render(request, 'openlavaweb/job_detail.html', {"job": job, }, )


def job_list(request, job_id=0):
    user_name = request.GET.get('user_name', 'all')
    queue_name = request.GET.get('queue_name', "")
    host_name = request.GET.get('host_name', "")
    job_state = request.GET.get('job_state', 'ACT')
    job_name = request.GET.get('job_name', "")

    job_list = Job.get_job_list(user_name=user_name, queue_name=queue_name, host_name=host_name, job_state=job_state,
                                job_name=job_name)

    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(job_list, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type='application/json')

    paginator = Paginator(job_list, 25)
    page = request.GET.get('page')
    try:
        job_list = paginator.page(page)
    except PageNotAnInteger:
        job_list = paginator.page(1)
    except EmptyPage:
        job_list = paginator.page(paginator.num_pages)
    return render(request, 'openlavaweb/job_list.html', {"job_list": job_list, })


@ensure_csrf_cookie
def get_csrf_token(request):
    return HttpResponse(json.dumps({'cookie': get_token(request)}), content_type="application/json")

def system_view(request):
    cluster = Cluster()
    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(cluster, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type="application/json")

    return render(request, 'openlavaweb/system_view.html', {'cluster': cluster})


@csrf_exempt
def ajax_login(request):
    try:
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
    except:
        response = HttpResponse()
        response.status_code = 400
        return response
    if user:
        if user.is_active:
            login(request, user)
            res = {
                'status': "OK",
                'description': "Success"
            }
        else:
            res = {
                'status': 'Fail',
                'description': "User is inactive"
            }
    else:
        res = {
            'status': "Fail",
            'description': "Unable to authenticate",
        }
    return HttpResponse(json.dumps(res), content_type="application/json")

@login_required
def job_submit(request):
    kwargs = None
    if request.is_ajax() or request.GET.get("json", None):
        kwargs = json.loads(request.body)
    else:
        if request.method == 'POST':
            form = JobSubmitForm(request.POST)
            if form.is_valid():
                # submit the job
                kwargs = form._get_args()
        else:
            form = JobSubmitForm()
        return render(request, 'openlavaweb/job_submit.html', {'form': form})

    q = MPQueue()
    p = MPProcess(target=execute_job_submit, kwargs={'queue': q, 'request': request, 'args': kwargs})
    p.start()
    p.join()
    rc = q.get(False)
    try:
        if isinstance(rc, Exception):
            raise rc
        else:
            return rc
    except ClusterException as e:
        if request.is_ajax() or request.GET.get("json", None):
            return HttpResponse(e.to_json(), content_type='application/json')
        else:
            return render(request, 'openlavaweb/exception.html', {'exception': e})


def execute_job_submit(request, queue, args):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        job = Job.submit(**args)
        queue.put(HttpResponseRedirect(reverse("olw_job_view_array", args=[job.job_id, job.array_index])))
    except Exception as e:
        queue.put(e)


class JobSubmitForm(forms.Form):
    from openlava import lsblib

    def _get_args(self):
        kwargs = {}
        if 'options' in self.cleaned_data:
            opt = 0
            for i in self.cleaned_data['options']:
                opt = opt | int(i)
            kwargs['options'] = opt

        if 'options2' in self.cleaned_data:
            opt = 0
            for i in self.cleaned_data['options2']:
                opt = opt | int(i)
            kwargs['options2'] = opt

        for field, value in self.cleaned_data.items():
            if field in ['options', 'options2']:
                continue
            if value:
                kwargs[field] = value
        return kwargs

    #transfer files
    #rlimits

    # options....
    opts = [
        (lsblib.SUB_EXCLUSIVE, "Exclusive"),
        (lsblib.SUB_NOTIFY_END, "Notify End"),
        (lsblib.SUB_NOTIFY_BEGIN, "Notify Begin"),
        (lsblib.SUB_RERUNNABLE, "Re-Runnable"),
    ]
    opts2 = [
        (lsblib.SUB2_HOLD, "Hold Job"),
        (lsblib.SUB2_QUEUE_CHKPNT, "Checkpointable Queue Only"),
        (lsblib.SUB2_QUEUE_RERUNNABLE, "Re-Runnable Queue Only"),
    ]
    options = forms.MultipleChoiceField(choices=opts, required=False)
    options2 = forms.MultipleChoiceField(choices=opts2, required=False)
    num_processors = forms.IntegerField(initial=1)
    command = forms.CharField(widget=forms.Textarea, max_length=512)
    job_name = forms.CharField(max_length=512, required=False)
    queues = [(u'', u'Default')]
    for q in Queue.get_queue_list():
        queues.append([q.name, q.name])
    queue_name = forms.ChoiceField(choices=queues, required=False)
    hosts = []
    for h in Host.get_host_list():
        hosts.append([h.name, h.name])
    requested_hosts = forms.MultipleChoiceField(choices=hosts, required=False)
    resource_request = forms.CharField(max_length=512, required=False)
    ## Rlimits
    host_specification = forms.CharField(max_length=512, required=False)
    dependency_conditions = forms.CharField(max_length=512, required=False)
    #begin_time=forms.DateTimeField(required=False)
    #term_time=forms.DateTimeField(required=False)
    signal_value = forms.IntegerField(required=False)
    input_file = forms.CharField(max_length=512, required=False)
    output_file = forms.CharField(max_length=512, required=False)
    error_file = forms.CharField(max_length=512, required=False)
    checkpoint_period = forms.IntegerField(required=False)
    checkpoint_directory = forms.CharField(max_length=512, required=False)
    email_user = forms.EmailField(required=False)
    project_name = forms.CharField(max_length=128, required=False)
    max_num_processors = forms.IntegerField(required=False)
    login_shell = forms.CharField(128, required=False)
    user_priority = forms.IntegerField(required=False)
