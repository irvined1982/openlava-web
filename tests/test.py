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
from cluster.openlavacluster import Job, Host, Queue
from cluster import ConsumedResource
from olwclient import Job as OLJob, OpenLavaConnection, RemoteServerError, NoSuchHostError, NoSuchJobError, \
    NoSuchQueueError, NoSuchUserError, ResourceDoesntExistError, ClusterInterfaceError, PermissionDeniedError, \
    JobSubmitError

# Todo: Test Queue
# Todo: Test Host
# Todo: Test User
# Todo: Test Cluster


class Cargs:
    username = None
    password = None
    url = None


class CompareWebLocal(unittest.TestCase):
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
