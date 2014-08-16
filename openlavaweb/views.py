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
from cluster import ClusterException, NoSuchJobError
from cluster.openlavacluster import Cluster, Host, Job, Queue, User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from openlava import lsblib
from django.conf import settings

def create_js_success(data=None, message=""):
    """
    Takes a json serializable object, and an optional message, and creates a standard json response document.

    :param data: json serializable object
    :param message: Optional message to include with response
    :return: HttpResponse object

    """
    data = {
        'status': "OK",
        'data': data,
        'message': message,
    }
    return HttpResponse(json.dumps(data, cls=ClusterEncoder),
                            content_type='application/json')



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

def execute_get_output_path(request, queue, job_id, array_index):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        job = Job(job_id=job_id, array_index=array_index)
        path=job.get_output_path()
        if path:
            queue.put(path)
    except Exception as e:
        queue.put(e)

def job_error(request, job_id, array_index=0):
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
        try:
            path = q.get(False) + ".err"
        except MPQueue.Empty:
            path=None

        if isinstance(path, Exception):
            raise path

        if path and os.path.exists(path):
            f=open(path,'r')
            return HttpResponse(f, mimetype="text/plain")
        else:
            return HttpResponse("Not Available", mimetype=="text/plain")

    except ClusterException as e:
        if request.is_ajax() or request.GET.get("json", None):
            return HttpResponse(e.to_json(), content_type='application/json')
        else:
            return render(request, 'openlavaweb/exception.html', {'exception': e})


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
        try:
            path = q.get(False) + ".out"
        except:
            path=None

        if isinstance(path, Exception):
            raise path
        if path and os.path.exists(path):
            f=open(path,'r')
            return HttpResponse(f, mimetype="text/plain")
        else:
            return HttpResponse("Not Available", mimetype="text/plain")

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






@ensure_csrf_cookie
def get_csrf_token(request):
    return HttpResponse(json.dumps({'cookie': get_token(request)}), content_type="application/json")

def system_view(request):
    cluster = Cluster()
    if request.is_ajax() or request.GET.get("json", None):
        return HttpResponse(json.dumps(cluster, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type="application/json")

    return render(request, 'openlavaweb/system_view.html', {'cluster': cluster})


def system_overview_hosts(request):
    cluster=Cluster()
    states={
        'Down': 0,
        'Full': 0,
        'In Use': 0,
        'Empty': 0,
        'Closed': 0,
    }
    for host in cluster.hosts():
        if not host.is_server:
            continue
        if host.is_down():
            states['Down'] += 1
        elif host.is_busy():
            states['Full'] += 1
        elif host.is_closed():
            states['Closed'] += 1
        elif len(host.jobs()) > 0:
            states['In Use'] += 1
        else:
            states['Empty'] += 1

    nvstates=[]
    for k,v in states.iteritems():
        nvstates.append(
            {'label':k, 'value': v}
        )
    return HttpResponse(json.dumps(nvstates, sort_keys=True, indent=3, cls=ClusterEncoder), content_type="application/json")

def system_overview_jobs(request):
    cluster=Cluster()
    states={}

    for job in cluster.jobs():
        try:
            states[job.status.friendly] += 1
        except KeyError:
            states[job.status.friendly] = 1
    nvstates=[]
    for k,v in states.iteritems():
        nvstates.append(
            {'label':k, 'value': v}
        )
    return HttpResponse(json.dumps(nvstates, sort_keys=True, indent=3, cls=ClusterEncoder), content_type="application/json")

def system_overview_slots(request):
    cluster=Cluster()
    states={}

    for job in cluster.jobs():
        try:
            states[job.status.friendly] += job.requested_slots
        except KeyError:
            states[job.status.friendly] = job.requested_slots

    nvstates=[]
    for k,v in states.iteritems():
        nvstates.append(
            {'label':k, 'value': v}
        )
    return HttpResponse(json.dumps(nvstates, sort_keys=True, indent=3, cls=ClusterEncoder), content_type="application/json")


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

def job_view(request, job_id, array_index=0):
    """
    Renders a HTML page showing the specified job.

    :param request: Request object
    :param job_id: Job ID.
    :param array_index: The array index, must be zero or higher.
    :return:

        If the request is AJAX, returns a single json encoded job object.  If it is not an ajax request, then renders
        a HTML page showing information about the specified job.

        If the job does not exist, raises and renders NoSuchJob


    """
    job_id = int(job_id)
    array_index = int(array_index)
    assert(array_index >= 0)
    try:
        job = Job(job_id=job_id, array_index=array_index)
        if request.is_ajax() or request.GET.get("json", None):
            return create_js_success(data=job)
        else:
            return render(request, 'openlavaweb/job_detail.html', {"job": job, }, )

    except ClusterException as e:
        if request.is_ajax() or request.GET.get("json", None):
            return HttpResponse(e.to_json(), content_type='application/json')
        else:
            return render(request, 'openlavaweb/exception.html', {'exception': e})

    except NoSuchJobError as e:
        if request.is_ajax() or request.GET.get("json", None):
            return HttpResponse(e.to_json(), content_type='application/json')
        else:
            return render(request, 'openlavaweb/exception.html', {'exception': e})


def get_job_list(request, job_id=0):
    """
    Renders a HTML page listing jobs that match the query.

    :param request:
        Request object

    :param job_id:
        Numeric Job ID.  If job_id != 0, then all elements of that job will be returned, use this to see all tasks from
        an array job.

    :param ?queue_name:
            The name of the queue.  If specified, implies that job_id and array_index are set to default.  Only returns
            jobs that are submitted into the named queue.

    :param ?host_name:
        The name of the host.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are executing on the specified host.

    :param ?user_name:
        The name of the user.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are owned by the specified user.

    :param ?job_state:
        Only return jobs in this state, state can be "ACT" - all active jobs, "ALL" - All jobs, including finished
        jobs, "EXIT" - Jobs that have exited due to an error or have been killed by the user or an administator,
        "PEND" - Jobs that are in a pending state, "RUN" - Jobs that are currently running, "SUSP" Jobs that are
        currently suspended.

    :param ?job_name:
        Only return jobs that are named job_name.

    :return:
        If an ajax request, then returns an array of JSON Job objects that match the query. Otherwise returns a
        rendered HTML page listing each job.  Pages are paginated using a paginator.

    """
    job_id=int(job_id)
    if job_id != 0:
        # Get a list of active elements of the specified job.
        job_list = Job.get_job_list(job_id=job_id, array_index=-1)
    else:
        user_name = request.GET.get('user_name', 'all')
        queue_name = request.GET.get('queue_name', "")
        host_name = request.GET.get('host_name', "")
        job_state = request.GET.get('job_state', 'ACT')
        job_name = request.GET.get('job_name', "")
        job_list = Job.get_job_list(user_name=user_name, queue_name=queue_name, host_name=host_name, job_state=job_state,
                                    job_name=job_name)

    if request.is_ajax() or request.GET.get("json", None):
        print "creating response"
        return create_js_success(data=job_list)

    paginator = Paginator(job_list, 50)
    page = request.GET.get('page')
    try:
        job_list = paginator.page(page)
    except PageNotAnInteger:
        job_list = paginator.page(1)
    except EmptyPage:
        job_list = paginator.page(paginator.num_pages)
    return render(request, 'openlavaweb/job_list.html', {"job_list": job_list, })

@login_required
def job_submit(request, form_class="JobSubmitForm"):
    ajax_args = None
    form = None
    for cls in OLWSubmit.__subclasses__():
        if form_class == cls.__name__:
            form_class = cls
            break
    if not issubclass(form_class, OLWSubmit):
        raise ValueError

    if request.is_ajax() or request.GET.get("json", None):
        # configure form and arguments for ajax submission
        ajax_args = json.loads(request.body)
        form = form_class()
    else:
        # configure form an arguments for normal submission
        if request.method == 'POST':
            form = form_class(request.POST)
            # IF the form is not valid, then return the rendered form.
            if not form.is_valid():
                return render(request, 'openlavaweb/job_submit.html', {'form': form})
        else:
            # The form wasn't submitted yet, so render the form.
            form = form_class()
            return render(request, 'openlavaweb/job_submit.html', {'form': form})


    # Process the actual form.
    q = MPQueue()
    p = MPProcess(target=execute_job_submit, kwargs={'queue': q, 'request': request, 'ajax_args': ajax_args, 'submit_form':form})
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


def execute_job_submit(request, queue, ajax_args, submit_form):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        queue.put(submit_form.submit(ajax_args))
    except Exception as e:
        queue.put(e)



class OLWSubmit(forms.Form):
    """Openlava job submission form, redirects the user to the first job, or if ajax, dumps all jobs"""
    name="basesubmit"
    friendly_name="Base Submit"
    # If this needs to be treated as a formset, set to true so the
    # template knows to iterate through each form etc.
    is_formset=False

    def get_name(self):
        return self.__class__.__name__

    def submit(self, ajax_args = None):
        kwargs = None
        if ajax_args:
            kwargs = ajax_args
        else:
            kwargs = self._get_args()

        self._pre_submit()

        try:
            jobs = Job.submit(**kwargs)
            self._post_submit(jobs)

            if ajax_args:
                return HttpResponse(json.dumps(jobs, sort_keys=True, indent=3, cls=ClusterEncoder),
                                    content_type='application/json')
            return HttpResponseRedirect(reverse("olw_job_view_array", args=[jobs[0].job_id, jobs[0].array_index]))
        except Exception as e:
            return e

    def _get_args(selfs):
        """Return all arguments for job submission.  For normal simple web submission forms, this is all that is needed
        simply parse the form data and return a dict which will be passed to Job.submit()"""
        raise NotImplemented()

    def _pre_submit(self):
        """Called before the job is submitted, run as the user who is submitting the job."""
        return None

    def _post_submit(self, job):
        """Called after the job has been submitted, Job is the newly submitted job."""
        return None


class JobSubmitForm(OLWSubmit):
    friendly_name = "Generic Job"


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
    requested_slots = forms.IntegerField(initial=1)
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
    max_requested_slots = forms.IntegerField(required=False)
    login_shell = forms.CharField(128, required=False)
    user_priority = forms.IntegerField(required=False)


class SimpleJobSubmitForm(OLWSubmit):
    friendly_name = "Simple Job"

    def _get_args(self):
        kwargs = {}
        for field, value in self.cleaned_data.items():
            if field in ['options', 'options2']:
                continue
            if value:
                kwargs[field] = value
        return kwargs

    requested_slots = forms.IntegerField(initial=1)
    command = forms.CharField(widget=forms.Textarea, max_length=512)
    queues = [(u'', u'Default')]
    for q in Queue.get_queue_list():
        queues.append([q.name, q.name])
    queue_name = forms.ChoiceField(choices=queues, required=False)





class ConsumeResourcesJob(OLWSubmit):
    friendly_name = "Consume Resources"

    job_name = forms.CharField(max_length=512, required=False)
    requested_slots = forms.ChoiceField(choices=[(x, x) for x in xrange(1, 6)], initial=1, help_text="How many processors to execute on")
    run_time = forms.IntegerField(min_value=1, initial=120, help_text="How many seconds to execute for")

    memory_size = forms.IntegerField(min_value=1, initial=128, help_text="How many MB to consume")
    consume_cpu = forms.BooleanField(required=False, initial=True, help_text="Burn CPU cycles.")
    consume_network = forms.BooleanField(required=False, initial=False, help_text="Send MPI messages. (Experimental)")
    consume_disk = forms.BooleanField(required=False, initial=False, help_text="Read and write data to storage.")

    queues = [(u'', u'Default')]
    for q in Queue.get_queue_list():
        queues.append([q.name, q.name])
    queue_name = forms.ChoiceField(choices=queues, required=False)

    def _get_args(self):
        kwargs = {}

        if len(self.cleaned_data['job_name']) > 0:
            kwargs['job_name'] = self.cleaned_data['job_name']

        kwargs['requested_slots'] = self.cleaned_data['requested_slots']
        kwargs['queue_name'] = self.cleaned_data['queue_name']
        kwargs['job_name'] = self.cleaned_data['job_name']

        try:
            mpi_command = settings.MPIRUN_COMMAND
        except:
            mpi_command = "mpirun"

        try:
            command = settings.CONSUME_RESOURCES_COMMAND
        except:
            command = "consumeResources.py"

        if self.cleaned_data['consume_cpu']:
            command += " -c"
        if self.cleaned_data['consume_network']:
            command += " -n"
        if self.cleaned_data['consume_disk']:
            command += " -d"

        command += " -m "
        command += str(self.cleaned_data['memory_size'])
        command += " " + str(self.cleaned_data['run_time'])

        command = mpi_command + " " + command
        kwargs['command'] = command

        return kwargs


def submit_form_context(request):
    clses=[]
    for cls in OLWSubmit.__subclasses__():
        clses.append({
            'url':reverse("olw_job_submit_class", args=[cls.__name__]),
            'name':cls.friendly_name,
        })
    return {'submit_form_classes': clses}
