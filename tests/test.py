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
import doctest
import time
import os
import urllib
import cluster.openlavacluster
from cluster.openlavacluster import Job
from cluster import ConsumedResource


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
            response = urllib.urlopen("%s/job/%d" % (base_url, job.job_id, job.array_index))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/job/%d?json=1" % (base_url, job.job_id, job.array_index))
            self.assertTrue(self.check_content_type(response, "application/json"))
            response = urllib.urlopen("%s/job/%d/%d" % (base_url, job.job_id, job.array_index))
            self.assertTrue(self.check_content_type(response, "text/html"))
            response = urllib.urlopen("%s/job/%d/%d?json=1" % (base_url, job.job_id, job.array_index))
            self.assertTrue(self.check_content_type(response, "application/json"))
    
    @staticmethod
    def check_content_type(response, type):
        for header in response.info().headers:
            if header.startswith("Content-Type") and not header.endswith("%s\r\n" % type):
                return False
        return True


class TestConsumedResource(unittest.TestCase):
    def test_creation(self):
        c = ConsumedResource(name="MyRes", value=100)
        self.assertEqual(c.name, "MyRes")
        self.assertEqual(c.value, 100)
        self.assertIsNone(c.unit)
        self.assertIsNone(c.limit)

        c = ConsumedResource(name="MyRes", value=100, unit="BogoUnits")
        self.assertEqual(c.name, "MyRes")
        self.assertEqual(c.value, 100)
        self.assertEqual(c.unit, "BogoUnits")
        self.assertIsNone(c.limit)

        c = ConsumedResource(name="MyRes", value=100, limit=120, unit="BogoUnits")
        self.assertEqual(c.name, "MyRes")
        self.assertEqual(c.value, 100)
        self.assertEqual(c.unit, "BogoUnits")
        self.assertEqual(c.limit, 120)

        c = ConsumedResource(name="MyRes", value=100, limit=101)
        self.assertEqual(c.name, "MyRes")
        self.assertEqual(c.value, 100)
        self.assertEqual(c.limit, 101)
        self.assertIsNone(c.unit)


class TestJob(unittest.TestCase):

    def test_job_list(self):
        job_list = Job.get_job_list()
        for job in job_list:
            self.assertIsInstance(job, Job)

    def test_job_submit(self):
        jobs = Job.submit(requested_slots=1, command="sleep 1000")
        self.assertIs(len(jobs), 1, msg="Submitting one job returns 1 item")
        self.job_actions_test(jobs[0])

    def test_job_submit_array(self):
        jobs = Job.submit(job_name="JobTestSubmitArray[1-100]", requested_slots=1, command="sleep 20")
        self.assertIs(len(jobs), 100, msg="Submitting one job returns 1 item")
        for job in jobs[:5]:
            self.job_actions_test(job)

    def job_actions_test(self, job):
        self.assertIsInstance(job.is_completed, bool)
        # self.assertIsInstance(job.is_failed, bool)
        # self.assertIsInstance(job.is_pending, bool)
        # self.assertIsInstance(job.is_running, bool)
        # self.assertIsInstance(job.is_suspended, bool)
        # count = 0
        # if job.is_completed:
        #     count += 1
        #
        # if job.is_failed:
        #     count += 1
        #
        # if job.is_pending:
        #     count += 1
        #
        # if job.is_running:
        #     count += 1
        #
        # if job.is_suspended:
        #     count += 1
        #
        # self.assertIs(count, 1, msg="Only one active job mode per time.")
        # if job.is_pending or job.is_running:
        #     job.suspend()
        #     time.sleep(10)
        #     j2 = Job(job_id=job.job_id, array_index=job.array_index)
        #     self.assertEqual(j2.job_id, job.job_id)
        #     self.assertEqual(j2.array_index, job.array_index)
        #     self.assertEqual(j2.is_suspended, True)
        #     job = j2
        #
        # if job.is_suspended:
        #     job.resume()
        #     time.sleep(10)
        #     j2 = Job(job_id=job.job_id, array_index=job.array_index)
        #     self.assertEqual(j2.job_id, job.job_id)
        #     self.assertEqual(j2.array_index, job.array_index)
        #     self.assertEqual(j2.is_suspended, False)
        #     job = j2
        #
        # if job.is_pending or job.is_running:
        #     job.kill()
        #     time.sleep(10)
        #     j2 = Job(job_id=job.job_id, array_index=job.array_index)
        #     self.assertEqual(j2.job_id, job.job_id)
        #     self.assertEqual(j2.array_index, job.array_index)
        #     self.assertEqual(j2.was_killed, True)
        #     job = j2



"""
Create job with each individual argument, check that job matches.

Kill job, check job is killed

Check server, for each job available, check normal request, ajax request.

"""


def load_tests(loader, tests, ignore):
    #tests.addTests(doctest.DocTestSuite(cluster.openlavacluster))
    return tests

if __name__ == '__main__':
    unittest.main()
