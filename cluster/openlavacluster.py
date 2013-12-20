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
from cluster import *
from openlava import lslib, lsblib
import datetime
import time

initialized_openlava=False

def initialize():
	global initialized_openlava
	if initialized_openlava == False:
		if lsblib.lsb_init("Openlava Cluster Interface") != 0:
			raise ClusterInterfaceError(lslib.ls_sysmsg)
		else:
			initialized_openlava=True		

class Cluster(ClusterBase):
	def __init__(self):
		initialize()
		
	@property
	def name(self):
		return lslib.ls_getclustername()

	@property
	def master(self):
		return Host(lslib.ls_getmastername())

	def hosts(self):
		'''Returns an array of hosts that are part of the cluster'''
		raise NotImplementedError

	def queues(self, queue_name=None, host_name=None, user_name=None):
		'''Returns an array of queues that are part of the cluster'''
		raise NotImplementedError

	
	def jobs(self, job_id=None, job_name=None, user_name=None, host_name=None, job_state="all"):
		'''Returns an array of jobs that are part of the cluster'''
		raise NotImplementedError
		
	def resources(self, resource_name=None, host_name=None, user_name=None):
		'''Returns an array of resources that are part of thecluster'''
		cluster_info=lslib.ls_info()
		if cluster_info==None:
			raise OpenLavaError(lslib.ls_sysmsg())
		return [Resource(r) for r in cluster_info.resTable]
			

class OpenLavaError(ClusterException):
	pass

class NumericStatus(Status):
	def __init__(self,status):
		self._status=status

	def __unicode__(self):
		try:
			return u'%s' % self.states[self._status]['friendly']
		except KeyError:
			return u'UNKNOWN'
	def __repr__(self):
		try:
			return u'%s' % self.states[self._status]['name']
		except KeyError:
			return u'UNKNOWN'
	def __str__(self):
		try:
			return '%s' % self.states[self._status]['friendly']
		except KeyError:
			return 'UNKNOWN'

	def __int__(self):
		return self._status

	@property
	def name(self):
		return u"%s" % self.states[self._status]['name']

	@property
	def description(self):
		try:
			return u'%s' % self.states[self._status]['description']
		except KeyError:
			return "Unknown Code."

	@property
	def status(self):
		return self._status

	@property
	def friendly(self):
		try:
			return u"%s" % self.states[self._status]['friendly']
		except:
			return u""

	@classmethod
	def get_status_list(cls, mask):
		statuses=[]
		for key in cls.states.keys():
			if (key & mask) == key: 
				statuses.append(cls(key))
		return statuses
	

class HostStatus(NumericStatus):
	states={
			0x0:{
				'friendly':'Ok',
				'name':'HOST_STAT_OK',
				'description': "Ready to accept and run jobs.  ",
				},
			0x01:{
				'friendly':'Busy',
				'name':'HOST_STAT_BUSY',
				'description': "The host load is greater than a scheduling threshold.  In this status, no new job will be scheduled to run on this host.  ",
				},
			0x02:{
				'friendly':'Dispatch Window Closed',
				'name':'HOST_STAT_WIND',
				'description': "The host dispatch window is closed.  In this status, no new job will be accepted.  ",
				},
			0x04:{
				'friendly':'Disabled by Administrator',
				'name':'HOST_STAT_DISABLED',
				'description': "The host has been disabled by the LSF administrator and will not accept jobs.  In this status, no new job will be scheduled to run on this host.  ",
				},
			0x08:{
				'friendly':'Locked',
				'name':'HOST_STAT_LOCKED',
				'description': "The host is locked by a exclusive task.  In this status, no new job will be scheduled to run on this host.  ",
				},
			0x10:{
				'friendly':'Full',
				'name':'HOST_STAT_FULL',
				'description': "Great than job limit.  The host has reached its job limit. In this status, no new job will be scheduled to run on this host.  ",
				},
			0x20:{
				'friendly':'Unreachable',
				'name':'HOST_STAT_UNREACH',
				'description': "The sbatchd on this host is unreachable.  ",
				},
			0x40:{
				'friendly':'Unavailable',
				'name':'HOST_STAT_UNAVAIL',
				'description': "The LIM and sbatchd on this host are unavailable.  ",
				},
			0x80:{
				'friendly':'No LIM',
				'name':'HOST_STAT_NO_LIM',
				'description': "The host is running an sbatchd but not a LIM.  ",
				},
			0x100:{
				'friendly':'Exclusive',
				'name':'HOST_STAT_EXCLUSIVE',
				'description': "Running exclusive job.  ",
				},
			0x200:{
				'friendly':'Locked by Master LIM',
				'name':'HOST_STAT_LOCKED_MASTER',
				'description': "Lim locked by master LIM.  ",
				},
			}
	
class JobStatus(NumericStatus):
	states={
			0x00:{
				'friendly':"Null",
				'name':'JOB_STAT_NULL'  ,
				'description': 'State null.' ,
				},
			0x01:{
				'friendly':"Pending",
				'name':'JOB_STAT_PEND',
				'description':'The job is pending, i.e., it has not been dispatched yet.',
				},
			0x02:{
				'friendly':"Held",
				'name':"JOB_STAT_PSUSP",
				'description':"The pending job was suspended by its owner or the LSF system administrator.",
				},
			0x04:{
				'friendly':"Running",
				'name':"JOB_STAT_RUN",
				'description':"The job is running.",
				},
			0x08:{
				'friendly':"Suspended by system",
				'name':"JOB_STAT_SSUSP",
				'description':"The running job was suspended by the system because an execution host was overloaded or the queue run window closed.",
				},
			0x10:{
				'friendly':"Suspended by user",
				'name':"JOB_STAT_USUSP",
				'description':"The running job was suspended by its owner or the LSF system administrator.",
				},
			0x20:{
				'friendly':"Exited",
				'name':"JOB_STAT_EXIT",
				'description':"The job has terminated with a non-zero status - it may have been aborted due to an error in its execution, or killed by its owner or by the LSF system administrator.",
				},
			0x40:{
				'friendly':"Completed",
				'name':"JOB_STAT_DONE",
				'description':"The job has terminated with status 0.",
				},
			0x80:{
				'friendly':"Process Completed",
				'name':"JOB_STAT_PDONE",
				'description':"Post job process done successfully.",
				},
			0x100:{
				'friendly':"Process Error",
				'name':"JOB_STAT_PERR",
				'description':"Post job process has error.",
				},
			0x200:{
				'friendly':"Waiting for execution",
				'name':"JOB_STAT_WAIT",
				'description':"Chunk job waiting its turn to exec.",
				},
			0x10000:{
				'friendly':"Unknown",
				'name':"JOB_STAT_UNKWN",
				'description':"The slave batch daemon (sbatchd) on the host on which the job is processed has lost contact with the master batch daemon (mbatchd).",
				},
			}

	
class Job(JobBase):
	cluster_type="openlava"
	def __init__(self, job=None, job_id=None, array_index=0):
		initialize()
		self._last_update_time=0
		if job:
			print "Job"
			self._job_id=lsblib.get_job_id(job.jobId)
			self._array_index=lsblib.get_array_index(job.jobId)
		elif job_id:
			print "jobid"
			self._job_id=job_id
			self._array_index=array_index
			full_job_id=lsblib.create_job_id(job_id, array_index)
			num_jobs=lsblib.lsb_openjobinfo(job_id=full_job_id)
			print "got jobs"
			lsblib.lsb_closejobinfo()
			if num_jobs != 1:
				raise NoSuchJobError("Job: %s[%s] does not exist." % (job_id, array_index))
		else:
			raise ValueError("Job, or job_id required")
		
	def _update_jobinfo(self):
		if (int(time.time()) - self._last_update_time) < 60:
			return
		self._last_update_time=int(time.time())
		
		full_job_id=lsblib.create_job_id(self.job_id, self.array_index)
		num_jobs=lsblib.lsb_openjobinfo(job_id=full_job_id)
		if num_jobs == 1:
			job=lsblib.lsb_readjobinfo()
		lsblib.lsb_closejobinfo()
		if num_jobs != 1:
			raise NoSuchJobError("Job: %s[%s] does not exist." % self.job_id, self.array_index)
		self._status=job.status
		self._user_name=job.user
		self._submit_time=job.submitTime
		self._start_time=job.startTime
		self._end_time=job.endTime
		
	@property
	def submit_time(self):
		self._update_jobinfo()
		return self._submit_time
		
	@property
	def submit_time_datetime_local(self):
		return datetime.datetime.utcfromtimestamp(self.submit_time)
	
	@property
	def start_time(self):
		self._update_jobinfo()
		return self._start_time
	
	@property
	def start_time_datetime_local(self):
		return datetime.datetime.utcfromtimestamp(self.start_time)

	@property
	def end_time(self):
		self._update_jobinfo()
		return self._end_time
	
	@property
	def end_time_datetime_local(self):
		return datetime.datetime.utcfromtimestamp(self.end_time)
	
	@property
	def status(self):
		self._update_jobinfo()
		return JobStatus(self._status)

	def user_name(self):
		self._update_jobinfo()
		return self._user_name
		

class Host(HostBase):
	cluster_type="openlava"
	def __init__(self, host_name):
		initialize()
		self._lsb_update_time=0
		self._update_time=0
		
		# check host exists
		self._model=lslib.ls_gethostmodel(host_name)
		if self._model == None:
			raise NoSuchHostError("Host: %s does not exist" % host_name)
		self._name=host_name
		self._description=u""
	
	def jobs(self, job_id=0, job_name="", user="all", queue="", options=0):
		num_jobs=lsblib.lsb_openjobinfo(job_id=job_id, job_name=job_name, user=user, queue=queue, host=self.host_name, options=options)
		jobs=[]
		if num_jobs<1:
			return jobs
		jobs=[]
		for i in range(num_jobs):
			j=lsblib.lsb_readjobinfo()
			jobs.append(Job(job=j))
		lsblib.lsb_closejobinfo()
		return jobs
	
	def _update_lsb_hostinfo(self):
		if (int(time.time()) - self._lsb_update_time) < 60:
			return
		self._lsb_update_time=int(time.time())
		
		hosts=lsblib.lsb_hostinfo(hosts=[self.host_name])
		if hosts==None or len(hosts) != 1:
			raise ValueError("Invalid number of hosts")
		host=hosts[0]
		self._status=host.hStatus
		self._max_slots=host.maxJobs
		self._total_slots=host.numJobs
		
		self._num_running_slots=host.numRUN
		self._num_suspended_slots=host.numSSUSP+host.numUSUSP
		self._num_user_suspended_slots=host.numUSUSP
		self._num_system_suspended_slots=host.numSSUSP
		self._num_reserved_slots=host.numRESERVE
		
		self._max_jobs=host.maxJobs
		self._total_jobs=0
		self._num_running_jobs=0
		self._num_suspended_jobs=0
		self._num_user_suspended_jobs=0
		self._num_system_suspended_jobs=0
		
		if (host.attr & lsblib.H_ATTR_CHKPNTABLE) != 0:
			self._has_checkpoint_support=True
		else:
			self._has_checkpoint_support=False
			
		if (host.attr & lsblib.H_ATTR_CHKPNT_COPY ) != 0:
			self._has_kernel_checkpoint_support=True
		else:
			self._has_kernel_checkpoint_support=False
		
		self._load=host.load
		
		self._load_sched=host.loadSched
		for i in range(len(self._load_sched)):
			if self._load_sched[i] == 2147483648.0 or self._load_sched[i] == -2147483648.00:
				self._load_sched[i]=-1
	
		self._load_stop=host.loadStop
		for i in range(len(self._load_stop)):
			if self._load_stop[i] == 2147483648.0 or self._load_stop[i] == -2147483648.00:
				self._load_stop[i]=-1
				
		## iterate through jobs and count/sum each one.
		for j in self.jobs():
			self._total_jobs+=1
			if j.status.name=="JOB_STAT_RUN":
				self._num_running_jobs+=1
			elif j.status.name=="JOB_STAT_SSUSP":
				self._num_suspended_jobs+=1
				self._num_system_suspended_jobs+=1
			elif j.status.name=="JOB_STAT_USUSP":
				self._num_suspended_jobs+=1
				self._num_user_suspended_jobs+=1
				
		
	@property
	def status(self):
		self._update_lsb_hostinfo()
		return HostStatus.get_status_list(self._status)
	@property
	def host_type(self):
		return lslib.ls_gethosttype(self.name)
	
	@property
	def host_model(self):
		return self._model
	
	@property
	def cpu_factor(self):
		'''Openlava Specific - returns the CPU factor of the host'''
		return lslib.ls_gethostfactor(self.name)
	
	@property
	def max_processors(self):
		self._update_hostinfo()
		return self._max_processors
	
	@property
	def max_ram(self):
		self._update_hostinfo()
		return self._max_ram
	
	@property
	def max_swap(self):
		self._update_hostinfo()
		return self._max_swap
	
	@property
	def max_tmp(self):
		self._update_hostinfo()
		return self._max_tmp
	
	@property
	def num_disks(self):
		'''Openlava specific: Returns the number of physical disks installed in the machine'''
		self._update_hostinfo()
		return self._num_disks
		
	@property
	def max_jobs(self):
		'''Returns the maximum number of jobs that may execute on this host'''
		self._update_lsb_hostinfo()
		return self._max_jobs
	
	@property
	def max_slots(self):
		'''Returns the maximum number of scheduling slots that may be consumed on this host'''
		self._update_lsb_hostinfo()
		return self._max_slots
	
	@property
	def total_jobs(self):
		'''Returns the total number of jobs that are running on this host, including suspended jobs.'''
		self._update_lsb_hostinfo()
		return self._total_jobs
	
	@property
	def total_slots(self):
		'''Returns the total number of slots that are consumed on this host, including those from  suspended jobs.'''
		self._update_lsb_hostinfo()
		return self._total_slots

	@property
	def num_running_jobs(self):
		'''Returns the nuber of jobs that are executing on the host'''
		self._update_lsb_hostinfo()
		return self._num_running_jobs
	
	@property
	def num_running_slots(self):
		'''Returns the total number of scheduling slots that are consumed on this host'''
		self._update_lsb_hostinfo()
		return self._num_running_slots
	
	@property
	def num_suspended_jobs(self):
		'''Returns the number of jobs that are suspended on this host'''
		self._update_lsb_hostinfo()
		return self._num_suspended_jobs
	
	@property
	def num_suspended_slots(self):
		'''Returns the number of scheduling slots that are suspended on this host'''
		self._update_lsb_hostinfo()
		return self._num_suspended_jobs

	@property
	def num_user_suspended_jobs(self):
		'''Returns the number of jobs that have been suspended by the user on this host'''
		self._update_lsb_hostinfo()
		return self._num_user_suspended_jobs
	
	@property
	def num_user_suspended_slots(self):
		'''Returns the number of scheduling slots that have been suspended by the user on this host'''
		self._update_lsb_hostinfo()
		return self._num_user_suspended_slots
	@property
	def num_system_suspended_jobs(self):
		'''Returns the number of jobs that have been suspended by the system on this host'''
		self._update_lsb_hostinfo()
		return self._num_system_suspended_jobs
	
	@property
	def num_system_suspended_slots(self):
		'''Returns the number of scheduling slots that have been suspended by the system on this host'''
		self._update_lsb_hostinfo()
		return self._num_system_suspended_slots

	@property
	def num_reserved_slots(self):
		'''Returns the number of scheduling slots that are reserved'''
		self._update_lsb_hostinfo()
		return self._num_reserved_slots
	
	def _update_hostinfo(self):
		if (int(time.time()) - self._update_time) < 60:
			return
		self._update_time=int(time.time())
		# cache this....
		hosts=lslib.ls_gethostinfo(resReq="", hostList=[self.host_name], options=0)
		if len(hosts) != 1:
			raise ValueError("Invalid number of hosts returned")
		host=hosts[0]
		self._max_processors=host.maxCpus
		self._max_ram=host.maxMem
		self._max_swap=host.maxSwap
		self._max_tmp = host.maxTmp
		self._num_disks=host.nDisks
		self._is_server=host.isServer
		resource_names=host.resources
		self._resources=[]
		c=Cluster()
		for r in c.resources():
			print resource_names
			if r.name in resource_names:
				self._resources.append(r)
	@property
	def resources(self):
		self._update_hostinfo()
		return self._resources
	@property
	def is_server(self):
		'''True if host is an openlava server (as opposed to submission host)'''
		self._update_hostinfo()
		return self._is_server
	@property
	def has_checkpoint_support(self):
		self._update_lsb_hostinfo()
		return self._has_checkpoint
	
	@property
	def has_kernel_checkpoint_copy(self):
		self._update_lsb_hostinfo()
		return self._has_kernel_checkpoint
	
	def load_information(self):
		self._update_lsb_hostinfo()
		#index tyep:[{name,value,unit}]
		indexes={
			'names':["15s Load","1m Load","15m Load","Avg CPU Utilization","Paging Rate (Pages/Sec)","Disk IO Rate (MB/Sec)","Num Users","Idle Time","Tmp Space (MB)","Free Swap (MB)","Free Memory (MB)"],
			'values':[]
		}
		
		indexes['values'].append({
			'name':"Actual Load",
			'values':self._load
		})
		
		indexes['values'].append({
			'name':"Stop Dispatching Load",
			'values':self._load_sched
		})
		
		indexes['values'].append({
			'name':"Stop Executing Load",
			'values':self._load_stop
		})
		
		return indexes
	
class Resource(BaseResource):
	def __init__(self, res):
		if isinstance(res, lslib.ResItem):
			self._name=res.name
			self._description=res.des
			self._type=res.valueType
			self._order=res.orderType
			self._interval=res.interval
			self._flags=res.flags
			
		elif isinstance(res, str):
			# lookup
			pass
		else:
			raise ValueError("ri must be a ResItem object or resource name")


	@property
	def type(self):
		return self._type[3:].capitalize()
	
	@property
	def order(self):
		return self._order

	def interval(self):
		return datetime.timedelta(seconds=self._interval)

	def flags(self):
		return self._flags
	