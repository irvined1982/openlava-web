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
import datetime
import json

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
	def json_attributes(self):
		return [
			'cluster_type',
			'job_id',
			'array_index',
			'begin_time',
			'command',
			'consumed_resources',
			'cpu_time',
			'dependency_condition',
			'email_user',
			'end_time',
			'error_file_name',
			'execution_hosts',
			'input_file_name',
			'max_requested_slots',
			'name',
			'options',
			'output_file_name',
			'pending_reasons',
			'predicted_start_time',
			'priority',
			'process_id',
			'processes',
			'project_names',
			'requested_resources',
			'requested_slots',
			'reservation_time',
			'runtime_limits',
			'start_time',
			'status',
			'submission_host',
			'submit_time',
			'suspension_reasons',
			'termination_time',
			'user_name',
			'user_priority',
			'queue',
			'requested_hosts',
		]
	@property
	def job_id(self):
		return self._job_id
	
	@property
	def array_index(self):
		return self._array_index
	
	@property
	def begin_time_datetime_local(self):
		'''Datetime object for begin time deadline'''
		return datetime.datetime.fromtimestamp(self.begin_time)

	@property
	def predicted_start_time_datetime_local(self):
		'''Datetime object of the predicted start time'''
		return datetime.datetime.fromtimestamp(self.predicted_start_time)

	@property
	def end_time_datetime_local(self):
		'''End time as datetime'''
		return datetime.datetime.utcfromtimestamp(self.end_time)

	@property
	def cpu_time_timedelta(self):
		return datetime.timedelta(seconds=self.cpu_time)

	@property
	def reservation_time_datetime_local(self):
		return datetime.datetime.fromtimestamp(self.reservation_time)

	@property
	def start_time_datetime_local(self):
		'''Start time as datetime'''
		return datetime.datetime.utcfromtimestamp(self.start_time)

	@property
	def submit_time_datetime_local(self):
		'''Submit time as datetime'''
		return datetime.datetime.fromtimestamp(self.submit_time)

	@property
	def termination_time_datetime_local(self):
		'''Datetime object for termination deadline'''
		return datetime.datetime.fromtimestamp(self.termination_time)




	## The following must be implemented by each class
	@property
	def begin_time(self):
		'''Job will not start before this time'''
		raise NotImplementedError
		
	@property
	def command(self):
		'''Command to execute'''
		raise NotImplementedError
	
	@property
	def consumed_resources(self):
		'''Array of resource usage information'''
		raise NotImplementedError
	
	@property
	def cpu_time(self):
		'''CPU Time in seconds that the job has consumed'''
		raise NotImplementedError

	@property
	def dependency_condition(self):
		'''Job dependency information'''
		raise NotImplementedError
	
	@property
	def email_user(self):
		'''User supplied email address to send notifications to'''
		raise NotImplementedError
	
	@property
	def end_time(self):
		'''Time the job ended in seconds since epoch UTC'''
		raise NotImplementedError
	
	@property
	def error_file_name(self):
		'''Path to the error file'''
		raise NotImplementedError
	
	@property
	def execution_hosts(self):
		'''List of hosts that job is running on'''
		raise NotImplementedError
	
	@property
	def input_file_name(self):
		'''Path to the input file'''
		raise NotImplementedError
	
	@property
	def is_pending(self):
		'''True if the job is pending'''
		if self.status.name=="JOB_STAT_PEND":
			return True
		return false
	
	@property
	def is_running(self):
		'''True if the job is executing'''
		if self.status.name=="JOB_STAT_RUN":
			return True
		return False
	
	@property
	def is_suspended(self):
		'''True if the job is suspended'''
		if self.status=="JOB_STAT_USUSP" or self.status=="JOB_STAT_SSUSP" or "JOB_STAT_PSUSP":
			return True
		return False
	
	@property
	def max_requested_slots(self):
		'''The maximum number of job slots that could be used by the job'''
		raise NotImplementedError
	
	@property
	def name(self):
		'''User or system given name of the job'''
		raise NotImplementedError
	
	@property
	def options(self):
		'''List of options that apply to the job'''
		raise NotImplementedError
	
	@property
	def output_file_name(self):
		'''Path to the output file'''
		raise NotImplementedError
	
	@property
	def pending_reasons(self):
		'''Text string explainging why the job is pending'''
		raise NotImplementedError
	
	@property
	def predicted_start_time(self):
		'''Predicted start time of the job'''
		raise NotImplementedError
	
	@property
	def priority(self):
		'''Actual priority of the job'''
		raise NotImplementedError
	
	@property
	def process_id(self):
		'''Process id of the job'''
		raise NotImplementedError
	
	@property
	def processes(self):
		'''Array of processes started by the job'''
		raise NotImplementedError
	
	@property
	def project_names(self ):
		'''Array of project names that the job was submitted with'''
		raise NotImplementedError
	
	@property
	def requested_resources(self):
		'''Resources requested by the job'''
		raise NotImplementedError
	
	@property
	def requested_slots(self):
		'''The number of job slots requested by the job'''
		raise NotImplementedError
	
	@property
	def reservation_time(self):
		raise NotImplementedError
	
	@property
	def runtime_limits(self):
		'''Array of run time limits imposed on the job'''
		raise NotImplementedError
	
	@property
	def start_time(self):
		'''start time of the job in seconds since epoch UTC'''
		raise NotImplementedError
		
	@property
	def status(self):
		'''Status of the job'''
		raise NotImplementedError
	
	@property
	def submission_host(self):
		'''Host job was submitted from'''
		raise NotImplementedError
	
	@property
	def submit_time(self):
		'''Submit time in seconds since epoch'''
		raise NotImplementedError
	
	@property
	def suspension_reasons(self,):
		'''Reasons the job has been suspended'''
		raise NotImplementedError
	
	@property
	def termination_time(self):
		'''Termination deadline - the job will finish before or on this time'''
		raise NotImplementedError
		
	@property
	def user_name(self):
		'''User name of the job owner'''
		raise NotImplementedError
	
	@property
	def user_priority(self ):
		'''User given priority of the job'''
		raise NotImplementedError
	
	def queue(self):
		'''The queue object for the queue the job is currently in.'''
		raise NotImplementedError
	
	def requested_hosts(self):
		'''Array of host objects the job was submitted to'''
		raise NotImplementedError
	
	


class HostBase:
	
	def json_attributes(self):
		return [
			'name',
			'host_name',
			'description',
			'has_checkpoint_support',
			'host_model',
			'host_type',
			'resources',
			'max_jobs',
			'max_processors',
			'max_ram',
			'max_slots',
			'max_swap',
			'max_tmp',
			'num_reserved_slots',
			'num_running_jobs',
			'num_running_slots',
			'num_suspended_jobs',
			'num_suspended_slots',
			'status',
			'total_jobs',
			'total_slots',
			'jobs',
			'load_information',
			'cluster_type',
		]

	def __init__(self, host_name, description=u""):
		self.name=host_name
		self.host_name=host_name
		self.description=description

	@property
	def has_checkpoint_support(self):
		'''True if the host supports checkpointing'''
		raise NotImplementedError
	
	@property
	def host_model(self):
		'''String containing model information'''
		raise NotImplementedError

	@property
	def host_type(self):
		'''String containing host type information'''
		raise NotImplementedError

	@property
	def resources(self):
		'''Array of resources available'''
		raise NotImplementedError

	@property
	def max_jobs(self):
		'''Returns the maximum number of jobs that may execute on this host'''
		raise NotImplementedError

	@property
	def max_processors(self):
		'''Maximum number of processors available on the host'''
		raise NotImplementedError
	
	@property
	def max_ram(self):
		'''Max Ram'''
		raise NotImplementedError
		
	@property
	def max_slots(self):
		'''Returns the maximum number of scheduling slots that may be consumed on this host'''
		raise NotImplementedError
	

	@property
	def max_swap(self):
		'''Max swap space'''
		raise NotImplementedError
	
	@property
	def max_tmp(self):
		'''Max tmp space'''
		raise NotImplementedError

	@property
	def num_reserved_slots(self):
		'''Returns the number of scheduling slots that are reserved'''
		raise NotImplementedError
	
	@property
	def num_running_jobs(self):
		'''Returns the nuber of jobs that are executing on the host'''
		raise NotImplementedError
	
	@property
	def num_running_slots(self):
		'''Returns the total number of scheduling slots that are consumed on this host'''
		raise NotImplementedError
	
	@property
	def num_suspended_jobs(self):
		'''Returns the number of jobs that are suspended on this host'''
		raise NotImplementedError
	
	@property
	def num_suspended_slots(self):
		'''Returns the number of scheduling slots that are suspended on this host'''
		raise NotImplementedError

	@property
	def status(self):
		'''Array of statuses that apply to the host'''
		raise NotImplementedError

	@property
	def total_jobs(self):
		'''Returns the total number of jobs that are running on this host, including suspended jobs.'''
		raise NotImplementedError
	
	@property
	def total_slots(self):
		'''Returns the total number of slots that are consumed on this host, including those from  suspended jobs.'''
		raise NotImplementedError

	def jobs(self, job_id=0, job_name="", user="all", queue="", options=0):
		'''Return jobs on this host'''
		raise NotImplementedError
	
	def load_information(self):
		'''Return load information on the host'''
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
	def get_class(self):
		return u"%s" % self.__class__
	
	def to_json(self):
		return json.dumps({'type':str(type(self)),'message':self.message})

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

class Process:
	def __init__(self, hostname, process_id, **kwargs):
		self.hostname=hostname
		self.process_id=process_id
		self.extras=[]
		for k,v in kwargs.iteritems():
			setattr(self,k,v)
			self.extras.append(k)
		
	def json_attributes(self):
		return ['hostname','process_id']+self.extras
class ResourceLimit:
	def __init__(self, name, soft_limit, hard_limit, description=None, unit=None):
		self.name=name
		self.soft_limit=soft_limit
		self.hard_limit=hard_limit
		self.description=description
		self.unit=unit
	def json_attributes(self):
		return ['name','soft_limit','hard_limit','description','unit']
	


class ConsumedResource:
	def __init__(self, name, value, limit=None, unit=None):
		self.name=name
		self.value=value
		self.limit=None
		self.unit=None
	
	def json_attributes(self):
		return ['name','value','limit','unit']

__ALL__=[ClusterBase, ResourceLimit, ConsumedResource, HostBase, JobBase, Status, Process, ClusterException, NoSuchHostError, NoSuchJobError, ResourceDoesntExistError, ClusterInterfaceError]
