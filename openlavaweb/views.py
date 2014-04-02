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



def job_view(request, job_id, array_index=0):
    job_id = int(job_id)
    array_index = int(array_index)
    try:
        job = Job(job_id=job_id, array_index=array_index)
        if request.is_ajax() or request.GET.get("json", None):
            return HttpResponse(json.dumps(job, sort_keys=True, indent=3, cls=ClusterEncoder),
                            content_type="application/json")
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

@login_required
def job_submit(request):
    kwargs = None
    form_class=request.GET.get("form", "JobSubmitForm")
    for cls in OLWSubmit.__subclasses__():
        if form_class == cls.__name__:
            form_class = cls
    if not issubclass(form_class, OLWSubmit):
        raise ValueError

    if request.is_ajax() or request.GET.get("json", None):
        kwargs = json.loads(request.body)
    else:
        if request.method == 'POST':
            form = form_class(request.POST)
            if form.is_valid():
                # submit the job
                kwargs = form._get_args()
        else:
            form = form_class()
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


def execute_job_submit(request, queue, args, submit_form):
    try:
        user_id = pwd.getpwnam(request.user.username).pw_uid
        os.setuid(user_id)
        submit_form._pre_submit()
        job = Job.submit(**args)
        submit_form._post_submit(job)
        queue.put(HttpResponseRedirect(reverse("olw_job_view_array", args=[job.job_id, job.array_index])))
    except Exception as e:
        queue.put(e)



class OLWSubmit(forms.Form):
    """Openlava job submission form"""
    name="basesubmit"
    friendly_name="Base Submit"
    def _get_args(selfs):
        """Return all arguments for job submission"""
        raise NotImplemented()

    def _pre_submit(self):
        """Called before the job is submitted, run as the user who is submitting the job."""
        return None

    def _post_submit(self, job):
        """Called after the job has been submitted, Job is the newly submitted job."""
        return None


class JobSubmitForm(OLWSubmit):
    friendly_name = "Generic Job"
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

    num_processors = forms.IntegerField(initial=1)
    command = forms.CharField(widget=forms.Textarea, max_length=512)
    queues = [(u'', u'Default')]
    for q in Queue.get_queue_list():
        queues.append([q.name, q.name])
    queue_name = forms.ChoiceField(choices=queues, required=False)

class TrinityJobSubmitForm(OLWSubmit):
    friendly_name = "Trinity Job"

    def _get_args(self):
        kwargs = {}
        for f in ['num_processors', 'job_name']:
            kwargs[f]=self.cleaned_data[f]

        command="/home/irvined/trinityrnaseq_r20131110/Trinity.pl"
        command += " --seqType %s" % self.cleaned_data['seqType']
        command += " --JM %sG" % self.cleaned_data['JM']
        command += " --SS_lib_type %s" % self.cleaned_data['SS_lib_type']
        command += " --min_contig_length %s" % self.cleaned_data['min_contig_length']
        if self.cleaned_data['jaccard_clip']:
            command += " --jaccard_clip"
        if self.cleaned_data['prep']:
            command += " --prep"
        if self.cleaned_data['no_cleanup']:
            command += " --no_cleanup"
        if self.cleaned_data['full_cleanup']:
            command += " --full_cleanup"
        command += " --min_kmer_cov %s" % self.cleaned_data['min_kmer_cov']
        command += " --inchworm_cpu %s" % self.cleaned_data['inchworm_cpu']
        if self.cleaned_data['no_run_inchworm']:
            command += " --no_run_inchworm"

        command += " --left /home/irvined/trinityrnaseq_r20131110/sample_data/test_Trinity_Assembly/reads.left.fq"
        command += " --right /home/irvined/trinityrnaseq_r20131110/sample_data/test_Trinity_Assembly/reads.right.fq"
        command += " --CPU %s" % self.cleaned_data['num_processors']
        kwargs['command'] = command
        print "KWWWAAARRRRGS"
        print kwargs
        return kwargs

    num_processors = forms.ChoiceField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)], initial=1)
    job_name = forms.CharField(max_length=512, required=False)
    seqType = forms.ChoiceField(choices=[('fa', 'fa'), ('fq', 'fq')], help_text="Type of reads.")
    JM=forms.ChoiceField(choices=[(x,x) for x in range(1,32)], help_text="Amount of GB of system memory to use for k-mer counting by jellyfish.")
    SS_lib_type = forms.ChoiceField(choices=[('RF','RF'), ('FR','FR'), ('F','F'), ('R', 'R')], help_text="Strand-specific RNA-Seq read orientation. if paired: RF or FR if single: F or R.  (dUTP method = RF)")
    min_contig_length= forms.IntegerField(min_value=1, initial=200, help_text="Minimum assembled contig length to report.")
    jaccard_clip=forms.BooleanField(initial=False, help_text="Set if you have paired reads and you expect high gene density with UTR overlap (use FASTQ input file format for reads).  (Note: jaccard_clip is an expensive operation, so avoid using it unless necessary due to finding excessive fusion transcripts w/o it.)")
    prep = forms.BooleanField(initial=False, help_text="Only prepare files (high I/O usage) and stop before kmer counting.")
    no_cleanup=forms.BooleanField(initial=False, help_text="Retain all intermediate input files.")
    full_cleanup=forms.BooleanField(initial=False, help_text="only retain the Trinity fasta file, rename as ${output_dir}.Trinity.fasta")
    min_kmer_cov=forms.IntegerField(min_value=1, initial=1)
    inchworm_cpu=forms.ChoiceField(initial=6, choices=[(x,x) for x in range(6)], help_text="Number of CPUs to use for Inchworm, defaults to the number of CPUs specified for the job, or 6, whichever is lower" )
    no_run_inchworm=forms.BooleanField(initial=False, help_text="Stop after running jellyfish, before inchworm.")

