#!/usr/bin/env python
# Copyright 2014 David Irvine
#
# This file is part of python-cluster
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

class ClusterBase:
	@property
	def name(self):
		'''Returns the name of the cluster'''
		raise NotImplementedError

	@property
	def master(self):
		'''Returns the host object of the current master host'''
		raise NotImplementedError

	def hosts(self):
		'''Returns an array of hosts that are part of the cluster'''
		raise NotImplementedError

	def queues(self, queue_name=None, host_name=None, user_name=None):
		'''Returns an array of queues that are part of the cluster'''
		raise NotImplementedError

	def jobs(self, job_id=None, job_name=None, user_name=None, host_name=None, job_state="all" ):
		'''Returns an array of jobs that are part of the cluster'''
		raise NotImplementedError
	
	def pending_jobs(self, job_id=None, job_name=None, user_name=None, host_name=None):
		'''Returns an array of Jobs that are pending'''
		return self.jobs(job_id=job_id, job_name=job_name, user_name=user_name, host_name=host_name, job_state="pending")

	def running_jobs(self, job_id=None, job_name=None, user_name=None, host_name=None):
		'''Returns an array of Jobs that are running'''
		return self.jobs(job_id=job_id, job_name=job_name, user_name=user_name, host_name=host_name, job_state="running")
	
	def suspended_jobs(self, job_id=None, job_name=None, user_name=None, host_name=None):
		'''Returns an array of Jobs that are suspended'''
		return self.jobs(job_id=job_id, job_name=job_name, user_name=user_name, host_name=host_name, job_state="suspended")
	
	def held_jobs(self, job_id=None, job_name=None, user_name=None, host_name=None):
		'''Returns an array of Jobs that are held in the queue'''
		return self.jobs(job_id=job_id, job_name=job_name, user_name=user_name, host_name=host_name, job_state="held")
	
	def resources(self, resource_name=None, host_name=None, user_name=None):
		raise NotImplementedError

class JobBase:
	@property
	def job_id(self):
		return self._job_id
	
	@property
	def array_index(self):
		return self._array_index
	
	@property
	def status(self):
		raise NotImplementedError
	
class HostBase:
	@property
	def name(self):
		'''Returns the hostname of the host'''
		return self._name

	@property
	def host_name(self):
		'''Host name of the host'''
		return self.name
	
	@property
	def status(self):
		'''Returns an array of applicable statuses for the host'''

	@property
	def max_processors(self):
		'''Maximum number of processors available on the host'''
		raise NotImplementedError
	
	@property
	def max_ram(self):
		'''Total amount of RAM available on the machine in Kb'''
		raise NotImplementedError
	@property
	def max_swap(self):
		'''Total amount of Swap available on the machine in Kb'''
		raise NotImplementedError
	
	@property
	def max_tmp(self):
		'''Total amount of Tmp space available on the machine in Kb'''
		raise NotImplementedError


	def load_indexes(self):
		'''Returns an array of load index objects for the host'''
		raise NotImplementedError

	def max_jobs(self):
		'''Returns the maximum number of jobs that may execute on the host'''
		raise NotImplementedError
	def max_slots(self):
		'''Returns the maximum number of scheduling slots that may be consumed on this host'''
		raise NotImplementedError
	
	def num_jobs(self):
		'''Returns the nuber of jobs that are executing on the host'''
		raise NotImplementedError
	
	def num_slots(self):
		'''Returns the total number of scheduling slots that are consumed on this host'''
		raise NotImplementedError
	
	def num_suspended_jobs(self):
		'''Returns the number of jobs that are suspended on this host'''
		raise NotImplementedError
	
	def num_suspended_slots(self):
		'''Returns the number of scheduling slots that are suspended on this host'''
		raise NotImplementedError
		
	def jobs(self):
		'''Returns an array of Job Objects that are running on the host'''
		raise NotImplementedError

class LoadIndex:
	def __init__(self, name, value, description=""):
		self._name=unicode(name)
		self._value=float(value)
		self._description=unicode(description)

	@property
	def name(self):
		return self._name

	@property
	def value(self):
		return self._value

	@property
	def description(self):
		return self._description


class BaseResource:
	def __init__(self, name, description=""):
		self._name=unicode(name)
		self._value=value
		self._description=unicode(description)
		raise NotImplementedError

	@property
	def name(self):
		'''Host name of the host'''
		return self._name
	
	@property
	def description(self):
		return self._description
	
	

	def jobs(self, job_id=None, job_name=None, user_name=None, job_state="all"):
		'''Returns jobs that are running on the host'''
		raise NotImplementedError
	
class ClusterException(Exception):
	def to_ajax(self):
		return json.dumps({'type':type(self),'message':self.message})

class NoSuchHostError(ClusterException):
	pass

class NoSuchJobError(ClusterException):
	pass

class ResourceDoesntExistError(ClusterException):
	pass

class ClusterInterfaceError(ClusterException):
	pass

class Status:
	pass

__ALL__=[ClusterBase, HostBase, JobBase, Status, ClusterException, NoSuchHostError, NoSuchJobError, ResourceDoesntExistError, ClusterInterfaceError]
