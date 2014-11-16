#!/usr/bin/env python
# Copyright 2014 David Irvine
#
# This file is part of openlava-web
#
# python-cluster is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# python-cluster is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-cluster.  If not, see <http://www.gnu.org/licenses/>.
import unittest
import time
import os
import urllib
import urllib2
import subprocess

from olwclient import User as OLUser, Job as OLJob, Host as OLHost, Queue as OLQueue, OpenLavaConnection, RemoteServerError, NoSuchHostError, NoSuchJobError, \
    NoSuchQueueError, NoSuchUserError, ResourceDoesntExistError, ClusterInterfaceError, PermissionDeniedError, \
    JobSubmitError

from openlavaweb.cluster.openlavacluster import Job, Host, Queue, User
from openlavaweb.cluster import ConsumedResource


# Todo: Test Cluster
# Todo: Host inactive/active/close/open
# Todo: Queue close/open/clear/etc


class Cargs(object):
    username = None
    password = None
    url = None


class TestCLIScripts(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None)
                         and os.environ.get("OLWCLIENT_PATH", None), "OLWEB not defined")
    def check_bhosts(self):
        hosts = Host.get_host_list()
        for mod in [None, '-w']:
            cmd = [
                os.path.join(os.environ.get("OLWCLIENT_PATH", None), 'bhosts.py'),
                '--username',
                os.environ.get("OLWEB_USERNAME", None),
                '--password',
                os.environ.get("OLWEB_PASSWORD", None),
            ]
            if mod:
                cmd.append(mod)

            cmd.append(
                os.environ.get("OLWEB_URL", None)
            )

            output = subprocess.check_output(cmd)
            self.assertEqual(len(output.splitlines())-1, len(hosts))

            for host in hosts:
                try:
                    output = subprocess.check_output(cmd + [host.name])
                except subprocess.CalledProcessError:
                    print " ".join(cmd, [host.name])
                    raise
                self.assertGreater(len(output.splitlines()), 1)
                if mod == "-l":
                    continue
                self.assertEqual(len(output.splitlines()), 2)
                self.assertEqual(output.splitlines()[1].split()[0], host.name)

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None)
                         and os.environ.get("OLWCLIENT_PATH", None), "OLWEB not defined")
    def check_bjobs(self):
        jobs = Job.get_job_list()
        for mod in [[], ['-w']]:
            cmd = [
                os.path.join(os.environ.get("OLWCLIENT_PATH", None), 'bjobs.py'),
                '--username',
                os.environ.get("OLWEB_USERNAME", None),
                '--password',
                os.environ.get("OLWEB_PASSWORD", None),
            ]
            if mod:
                cmd.append(mod)

            cmd.append(
                os.environ.get("OLWEB_URL", None)
            )
            try:
                output = subprocess.check_output(cmd)
            except subprocess.CalledProcessError:
                    print " ".join(cmd)
                    raise

            if mod not in ['-l']:
                print " ".join(cmd)
                self.assertEqual(len(output.splitlines())-1, len(jobs))

            for job in jobs:
                job_str = str(job.job_id)
                if job.array_index > 0:
                    job_str += "[%s]" % job.array_index

                try:
                    output = subprocess.check_output(cmd + [job_str])
                except subprocess.CalledProcessError:
                    print " ".join(cmd + [job_str])
                    raise

                self.assertGreater(len(output), 0)
                if mod not in ['-l']:
                    self.assertEqual(len(output.splitlines()), 2)
                    if job.array_index == 0:
                        self.assertEqual(str(job.job_id), output.splitlines()[1].split()[0])



    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None)
                         and os.environ.get("OLWCLIENT_PATH", None), "OLWEB not defined")
    def check_bqueues(self):
        queues = Queue.get_queue_list()
        for mod in [[], ['-w']]:
            cmd = [
                os.path.join(os.environ.get("OLWCLIENT_PATH", None), 'bqueues.py'),
                '--username',
                os.environ.get("OLWEB_USERNAME", None),
                '--password',
                os.environ.get("OLWEB_PASSWORD", None),
            ]
            if mod:
                cmd.append(mod)

            cmd.append(
                os.environ.get("OLWEB_URL", None)
            )
            try:
                output = subprocess.check_output(cmd)
            except subprocess.CalledProcessError:
                    print " ".join(cmd)
                    raise

            if mod not in ['-l']:
                print " ".join(cmd)
                self.assertEqual(len(output.splitlines())-1, len(queues))

            for queue in queues:
                try:
                    output = subprocess.check_output(cmd + [queue.name])
                except subprocess.CalledProcessError:
                    print " ".join(cmd + [queue.name])
                    raise

                self.assertGreater(len(output), 0)
                if mod not in ['-l']:
                    self.assertEqual(len(output.splitlines()), 2)
                    self.assertEqual(output.splitlines()[1].split()[0], queue.name)


class CompareWebLocal(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_queue_attributes(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        for local_queue in Queue.get_queue_list():
            remote_ob = OLQueue(connection, queue_name=local_queue.name)
            local_ob = Queue(local_queue.name)
            for attr in local_ob.json_attributes():

                local_attr_val = getattr(local_ob, attr)
                remote_attr_val = getattr(remote_ob, attr)

                if isinstance(local_attr_val, list):
                    self.assertEqual(len(local_attr_val), len(remote_attr_val))
                elif isinstance(local_attr_val, dict):
                    keys = local_attr_val.keys()
                    rkeys = getattr(remote_ob, attr).keys()
                    for key in keys:
                        self.assertIn(key, rkeys)
                    for key in rkeys:
                        self.assertIn(key, keys)
                else:
                    self.assertEqual(str(local_attr_val), str(remote_attr_val))

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_queue_list(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        remote_list = OLQueue.get_queue_list(connection)
        local_list = Queue.get_queue_list()

        local_names = set()
        remote_names = set()
        for ob in local_list:
            local_names.add(str(ob))

        for ob in remote_list:
            remote_names.add(str(ob))

        for ob in local_list:
            self.assertIn(str(ob), remote_names)

        for ob in remote_list:
            self.assertIn(str(ob), local_names)

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_user_attributes(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        for local_user in Host.get_host_list():
            remote_ob = OLUser(connection, user_name=local_user.name)
            local_ob = User(local_user.name)
            for attr in local_ob.json_attributes():

                local_attr_val = getattr(local_ob, attr)
                remote_attr_val = getattr(remote_ob, attr)

                if isinstance(local_attr_val, list):
                    self.assertEqual(len(local_attr_val), len(remote_attr_val))
                elif isinstance(local_attr_val, dict):
                    keys = local_attr_val.keys()
                    rkeys = getattr(remote_ob, attr).keys()
                    for key in keys:
                        self.assertIn(key, rkeys)
                    for key in rkeys:
                        self.assertIn(key, keys)
                else:
                    self.assertEqual(str(local_attr_val), str(remote_attr_val))

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_user_list(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        remote_list = OLUser.get_user_list(connection)
        local_list = User.get_user_list()

        local_names = set()
        remote_names = set()
        for ob in local_list:
            local_names.add(str(ob))

        for ob in remote_list:
            remote_names.add(str(ob))

        for ob in local_list:
            self.assertIn(str(ob), remote_names)

        for ob in remote_list:
            self.assertIn(str(ob), local_names)

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_host_attributes(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        for local_host in Host.get_host_list():
            remote_ob = OLHost(connection, host_name=local_host.name)
            local_ob = Host(local_host.name)
            for attr in local_ob.json_attributes():

                local_attr_val = getattr(local_ob, attr)
                remote_attr_val = getattr(remote_ob, attr)

                if isinstance(local_attr_val, list):
                    self.assertEqual(len(local_attr_val), len(remote_attr_val))
                elif isinstance(local_attr_val, dict):
                    keys = local_attr_val.keys()
                    rkeys = getattr(remote_ob, attr).keys()
                    for key in keys:
                        self.assertIn(key, rkeys)
                    for key in rkeys:
                        self.assertIn(key, keys)
                else:
                    self.assertEqual(str(local_attr_val), str(remote_attr_val))

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_host_list(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        remote_list = OLHost.get_host_list(connection)
        local_list = Host.get_host_list()

        local_names = set()
        remote_names = set()
        for ob in local_list:
            local_names.add(str(ob))

        for ob in remote_list:
            remote_names.add(str(ob))

        for ob in local_list:
            self.assertIn(str(ob), remote_names)

        for ob in remote_list:
            self.assertIn(str(ob), local_names)


    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_job_attributes(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        for local_job in Job.get_job_list():
            remote_ob = OLJob(connection, job_id=local_job.job_id, array_index=local_job.array_index)
            local_ob = Job(job_id=local_job.job_id, array_index=local_job.array_index)
            for attr in local_ob.json_attributes():

                local_attr_val = getattr(local_ob, attr)
                remote_attr_val = getattr(remote_ob, attr)

                if isinstance(local_attr_val, list):
                    self.assertEqual(len(local_attr_val), len(remote_attr_val))
                elif isinstance(local_attr_val, dict):
                    keys = local_attr_val.keys()
                    rkeys = getattr(remote_ob, attr).keys()
                    for key in keys:
                        self.assertIn(key, rkeys)
                    for key in rkeys:
                        self.assertIn(key, keys)
                else:
                    self.assertEqual(str(local_attr_val), str(remote_attr_val))


    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_job_list(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        remote_job_list = OLJob.get_job_list(connection)
        local_job_list = Job.get_job_list()
        local_jobs = set()
        remote_jobs = set()
        for job in local_job_list:
            local_jobs.add(str(job))

        for job in remote_job_list:
            remote_jobs.add(str(job))

        for job in local_jobs:
            self.assertIn(job, remote_jobs)

        for job in remote_jobs:
            self.assertIn(job, local_jobs)

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def compare_job_attributes(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)

        for local_job in Job.get_job_list():
            remote_job = OLJob(connection, job_id=local_job.job_id, array_index=local_job.array_index)
            local_job = Job(job_id=local_job.job_id, array_index=local_job.array_index)
            for attr in local_job.json_attributes():
                self.assertEqual(str(getattr(local_job, attr)), str(getattr(remote_job, attr)))


class TestWebServer(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("OLWEB_URL", None), "OLWEB_URL not defined")
    def test_job_urls(self):
        base_url = os.environ.get("OLWEB_URL", None)
        if not base_url:
            return
        base_url.rstrip("/")

        response = urllib.urlopen("%s/jobs/" % base_url)
        self.assertTrue(self.check_content_type(response, "text/html"))
        response = urllib.urlopen("%s/jobs/?json=1" % base_url)
        self.assertTrue(self.check_content_type(response, "application/json"))

        for job in Job.get_job_list():
            response = urllib.urlopen("%s/jobs/%d/" % (base_url, job.job_id))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/jobs/%d/?json=1" % (base_url, job.job_id))
            self.assertTrue(self.check_content_type(response, "application/json"))
            response = urllib.urlopen("%s/job/%d/%d" % (base_url, job.job_id, job.array_index))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/job/%d/%d?json=1" % (base_url, job.job_id, job.array_index))
            self.assertTrue(self.check_content_type(response, "application/json"))

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None), "OLWEB_URL not defined")
    def test_user_urls(self):
        base_url = os.environ.get("OLWEB_URL", None)
        if not base_url:
            return
        base_url.rstrip("/")
        response = urllib.urlopen("%s/users/" % base_url)
        self.assertTrue(self.check_content_type(response, "text/html"))
        response = urllib.urlopen("%s/users/?json=1" % base_url)
        self.assertTrue(self.check_content_type(response, "application/json"))
        for u in User.get_user_list():
            response = urllib.urlopen("%s/users/%s" % (base_url, u.name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/users/%s?json=1" % (base_url, u.name))
            self.assertTrue(self.check_content_type(response, "application/json"))

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None), "OLWEB_URL not defined")
    def test_queue_urls(self):
        base_url = os.environ.get("OLWEB_URL", None)
        if not base_url:
            return
        base_url.rstrip("/")
        response = urllib.urlopen("%s/queues/" % base_url)
        self.assertTrue(self.check_content_type(response, "text/html"))
        response = urllib.urlopen("%s/queues/?json=1" % base_url)
        self.assertTrue(self.check_content_type(response, "application/json"))
        for q in Queue.get_queue_list():
            response = urllib.urlopen("%s/queues/%s" % (base_url, q.name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/queues/%s?json=1" % (base_url, q.name))
            self.assertTrue(self.check_content_type(response, "application/json"))
            response = urllib.urlopen("%s/queues/%s/close" % (base_url, q.name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/queues/%s/open" % (base_url, q.name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/queues/%s/activate" % (base_url, q.name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/queues/%s/inactivate" % (base_url, q.name))
            self.assertTrue(self.check_content_type(response, "text/html"))

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None), "OLWEB_URL not defined")
    def test_host_urls(self):
        base_url = os.environ.get("OLWEB_URL", None)
        if not base_url:
            return
        base_url.rstrip("/")
        response = urllib.urlopen("%s/hosts/" % base_url)
        self.assertTrue(self.check_content_type(response, "text/html"))
        response = urllib.urlopen("%s/hosts/?json=1" % base_url)
        self.assertTrue(self.check_content_type(response, "application/json"))

        for host in Host.get_host_list():
            response = urllib.urlopen("%s/hosts/%s" % (base_url, host.host_name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/hosts/%s?json=1" % (base_url, host.host_name))
            self.assertTrue(self.check_content_type(response, "application/json"))
            response = urllib.urlopen("%s/hosts/%s/close" % (base_url, host.host_name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/hosts/%s/open" % (base_url, host.host_name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/hosts/%s/close?confirm=True" % (base_url, host.host_name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/hosts/%s/open?confirm=True" % (base_url, host.host_name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/hosts/%s/close" % (base_url, host.host_name))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/hosts/%s/open" % (base_url, host.host_name))
            self.assertTrue(self.check_content_type(response, "text/html"))

    @staticmethod
    def check_content_type(response, c_type):
        for header in response.info().headers:
            if header.startswith("Content-Type") and not header.startswith("Content-Type: %s" % c_type):
                print "Actual CT: %s" % header
                return False
        return True


class TestConsumedResource(unittest.TestCase):
    def test_creation(self):
        c = ConsumedResource(name="MyRes", value=100)
        self.assertEqual(c.name, "MyRes")
        self.assertEqual(c.value, '100')
        self.assertEqual(c.limit, 'None')
        self.assertEqual(c.unit, 'None')

        c = ConsumedResource(name="MyRes", value=100, unit="BogoUnits")
        self.assertEqual(c.name, "MyRes")
        self.assertEqual(c.value, '100')
        self.assertEqual(c.unit, "BogoUnits")
        self.assertEqual(c.limit, 'None')

        c = ConsumedResource(name="MyRes", value=100, limit=120, unit="BogoUnits")
        self.assertEqual(c.name, "MyRes")
        self.assertEqual(c.value, '100')
        self.assertEqual(c.unit, "BogoUnits")
        self.assertEqual(c.limit, '120')

        c = ConsumedResource(name="MyRes", value=100, limit=101)
        self.assertEqual(c.name, "MyRes")
        self.assertEqual(c.value, '100')
        self.assertEqual(c.limit, '101')
        self.assertEqual(c.unit, 'None')


class TestUser(unittest.TestCase):
    def test_user_list(self):
        for user in User.get_user_list():
            self.assertIsInstance(user, User)

    def test_user_get(self):
        for u in User.get_user_list():
            user = User(u.host_name)
            self.assertEqual(user.name, u.name)


class TestHost(unittest.TestCase):
    def test_host_list(self):
        for host in Host.get_host_list():
            self.assertIsInstance(host, Host)

    def test_host_get(self):
        for h in Host.get_host_list():
            host = Host(h.host_name)
            self.assertEqual(host.host_name, h.host_name)


class TestQueue(unittest.TestCase):
    def test_queue_list(self):
        for queue in Queue.get_queue_list():
            self.assertIsInstance(queue, Queue)

    def test_queue_get(self):
        for q in Queue.get_queue_list():
            queue = Queue(q.name)
            self.assertEqual(q.name, queue.name)


class TestRemoteExceptions(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_exception(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        base_url = os.environ.get("OLWEB_URL", None)
        base_url.rstrip("/")
        for ex in [
            RemoteServerError,
            NoSuchHostError,
            NoSuchJobError,
            NoSuchQueueError,
            NoSuchUserError,
            ResourceDoesntExistError,
            ClusterInterfaceError,
            PermissionDeniedError,
            JobSubmitError
        ]:
            print "Raising: %s" % ex.__name__
            url = "%s/exception_test?json=1&exception_name=%s" % (base_url, ex.__name__)
            request = urllib2.Request(url, None, {'Content-Type': 'application/json'})
            self.assertRaises(
                ex,
                connection.open, request
            )


class TestRemoteJob(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_job_list(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        job_list = OLJob.get_job_list(connection)
        for job in job_list:
            self.assertIsInstance(job, OLJob)

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_job_submit(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        jobs = OLJob.submit(connection, requested_slots=1, command="hostname")
        self.assertIs(len(jobs), 1, msg="Submitting one job returns 1 item")
        self.job_state_test(jobs[0])

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_job_submit_array(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        jobs = OLJob.submit(connection, job_name="JobTestSubmitArray[1-100]", requested_slots=1, command="hostname")
        self.assertIs(len(jobs), 100, msg="Submitting one job returns 1 item")
        for job in jobs[:5]:
            self.job_state_test(job)

    def job_state_test(self, job):
        self.assertIsInstance(job.is_completed, bool)
        self.assertIsInstance(job.is_failed, bool)
        self.assertIsInstance(job.is_pending, bool)
        self.assertIsInstance(job.is_running, bool)
        self.assertIsInstance(job.is_suspended, bool)
        count = 0
        if job.is_completed:
            count += 1

        if job.is_failed:
            count += 1

        if job.is_pending:
            count += 1

        if job.is_running:
            count += 1

        if job.is_suspended:
            count += 1

        self.assertIs(count, 1, msg="Only one active job mode per time.")

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_job_kill(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        jobs = OLJob.submit(connection, requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        # kill the job
        job.kill()

        # Wait for the job to actually die
        time.sleep(15)

        job = OLJob(connection, job_id=job.job_id, array_index=job.array_index)
        self.assertTrue(job.is_completed or job.is_failed or job.was_killed)

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_job_suspend(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        jobs = OLJob.submit(connection, requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        job.suspend()
        time.sleep(15)
        job = OLJob(connection, job_id=job.job_id, array_index=job.array_index)
        self.assertTrue(job.is_suspended)
        job.kill()

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_job_resume(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        jobs = OLJob.submit(connection, requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        job.suspend()
        time.sleep(15)
        job = OLJob(connection, job_id=job.job_id, array_index=job.array_index)
        self.assertTrue(job.is_suspended)
        job.resume()
        time.sleep(15)
        job = OLJob(connection, job_id=job.job_id, array_index=job.array_index)
        self.assertFalse(job.is_suspended)
        job.kill()

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_job_requeue(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        jobs = OLJob.submit(connection, requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        while job.is_pending:
            time.sleep(1)
            job = OLJob(connection, job_id=job.job_id, array_index=job.array_index)

        if not job.is_running:
            self.skipTest("Job no longer running")

        start_time = job.start_time
        job.requeue(hold=False)
        time.sleep(45)
        job = OLJob(connection, job_id=job.job_id, array_index=job.array_index)
        if job.is_pending:
            # Passed
            job.kill()
            return None

        self.assertNotEqual(job.start_time, start_time)
        job.kill()

    @unittest.skipUnless(os.environ.get("OLWEB_URL", None)
                         and os.environ.get("OLWEB_USERNAME", None)
                         and os.environ.get("OLWEB_PASSWORD", None), "OLWEB_URL not defined")
    def test_job_requeue_hold(self):
        Cargs.username = os.environ.get("OLWEB_USERNAME")
        Cargs.password = os.environ.get("OLWEB_PASSWORD")
        Cargs.url = os.environ.get("OLWEB_URL")
        connection = OpenLavaConnection(Cargs)
        jobs = OLJob.submit(connection, requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        while job.is_pending:
            time.sleep(1)
            job = OLJob(connection, job_id=job.job_id, array_index=job.array_index)

        if not job.is_running:
            self.skipTest("Job no longer running")

        job.requeue(hold=True)
        time.sleep(45)  # Takes a while, first state is exit...
        job = OLJob(connection, job_id=job.job_id, array_index=job.array_index)
        self.assertTrue(job.is_suspended)
        job.kill()


class TestJob(unittest.TestCase):

    def test_job_list(self):
        job_list = Job.get_job_list()
        for job in job_list:
            self.assertIsInstance(job, Job)

    def test_job_submit(self):
        jobs = Job.submit(requested_slots=1, command="hostname")
        self.assertIs(len(jobs), 1, msg="Submitting one job returns 1 item")
        self.job_state_test(jobs[0])

    def test_job_submit_array(self):
        jobs = Job.submit(job_name="JobTestSubmitArray[1-100]", requested_slots=1, command="hostname")
        self.assertIs(len(jobs), 100, msg="Submitting one job returns 1 item")
        for job in jobs[:5]:
            self.job_state_test(job)

    def job_state_test(self, job):
        self.assertIsInstance(job.is_completed, bool)
        self.assertIsInstance(job.is_failed, bool)
        self.assertIsInstance(job.is_pending, bool)
        self.assertIsInstance(job.is_running, bool)
        self.assertIsInstance(job.is_suspended, bool)
        count = 0
        if job.is_completed:
            count += 1

        if job.is_failed:
            count += 1

        if job.is_pending:
            count += 1

        if job.is_running:
            count += 1

        if job.is_suspended:
            count += 1

        self.assertIs(count, 1, msg="Only one active job mode per time.")

    def test_job_kill(self):
        jobs = Job.submit(requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        # kill the job
        job.kill()

        # Wait for the job to actually die
        time.sleep(15)

        job = Job(job_id=job.job_id, array_index=job.array_index)
        self.assertTrue(job.is_completed or job.is_failed or job.was_killed)

    def test_job_suspend(self):
        jobs = Job.submit(requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        job.suspend()
        time.sleep(15)
        job = Job(job_id=job.job_id, array_index=job.array_index)
        self.assertTrue(job.is_suspended)
        job.kill()

    def test_job_resume(self):
        jobs = Job.submit(requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        job.suspend()
        time.sleep(15)
        job = Job(job_id=job.job_id, array_index=job.array_index)
        self.assertTrue(job.is_suspended)
        job.resume()
        time.sleep(15)
        job = Job(job_id=job.job_id, array_index=job.array_index)
        self.assertFalse(job.is_suspended)
        job.kill()

    def test_job_requeue(self):
        jobs = Job.submit(requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        while job.is_pending:
            time.sleep(1)
            job = Job(job_id=job.job_id, array_index=job.array_index)

        if not job.is_running:
            self.skipTest("Job no longer running")

        start_time = job.start_time
        job.requeue(hold=False)
        time.sleep(45)
        job = Job(job_id=job.job_id, array_index=job.array_index)
        if job.is_pending:
            # Passed
            job.kill()
            return None

        self.assertNotEqual(job.start_time, start_time)
        job.kill()

    def test_job_requeue_hold(self):
        jobs = Job.submit(requested_slots=1, command="sleep 1000")
        job = jobs.pop()
        while job.is_pending:
            time.sleep(1)
            job = Job(job_id=job.job_id, array_index=job.array_index)

        if not job.is_running:
            self.skipTest("Job no longer running")

        job.requeue(hold=True)
        time.sleep(45)  # Takes a while, first state is exit...
        job = Job(job_id=job.job_id, array_index=job.array_index)
        self.assertTrue(job.is_suspended)
        job.kill()

if __name__ == '__main__':
    unittest.main()