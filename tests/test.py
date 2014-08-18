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
from cluster.openlavacluster import Job


class TestJob(unittest.TestCase):

    def test_job_list(self):
        job_list = Job.get_job_list()
        for job in job_list:
            self.assertIsInstance(job, Job)

    def test_job_submit(self):
        jobs = Job.submit(requested_slots=1, command="sleep 1000")
        self.assertIs(len(jobs), 1, msg="Submitting one job returns 1 item")
        self.test_job_actions(jobs[0])

    def test_job_submit(self):
        jobs = Job.submit(job_name="JobTestSubmitArray[1-100]", requested_slots=1, command="sleep 20")
        self.assertIs(len(jobs), 100, msg="Submitting one job returns 1 item")
        for job in jobs[:5]:
            self.test_job_actions(job)

    def test_job_actions(self, job):
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
        if job.is_pending or job.is_running:
            job.suspend()
            time.sleep(10)
            j2 = Job(job_id=job.job_id, array_index=job.array_index)
            self.assertEqual(j2.job_id, job.job_id)
            self.assertEqual(j2.array_index, job.array_index)
            self.assertEqual(j2.is_suspended, True)
            job = j2

        if job.is_suspended:
            job.resume()
            time.sleep(10)
            j2 = Job(job_id=job.job_id, array_index=job.array_index)
            self.assertEqual(j2.job_id, job.job_id)
            self.assertEqual(j2.array_index, job.array_index)
            self.assertEqual(j2.is_suspended, False)
            job = j2

        if job.is_pending or job.is_running:
            job.kill()
            time.sleep(10)
            j2 = Job(job_id=job.job_id, array_index=job.array_index)
            self.assertEqual(j2.job_id, job.job_id)
            self.assertEqual(j2.array_index, job.array_index)
            self.assertEqual(j2.was_killed, True)

if __name__ == '__main__':
    unittest.main()
