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
	def json_attributes(self ):
		return ['name','description','status','friendly']
	
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
	

class Submit2Option(NumericStatus):
        states={
                        0x01:{
                                'name':'SUB2_HOLD',
                                'description': "",
                                'friendly': "SUB2_HOLD",
                                },
                        0x02:{
                                'name':'SUB2_MODIFY_CMD',
                                'description': "",
                                'friendly': "SUB2_MODIFY_CMD",
                                },
                        0x04:{
                                'name':'SUB2_BSUB_BLOCK',
                                'description': "",
                                'friendly': "SUB2_BSUB_BLOCK",
                                },
                        0x08:{
                                'name':'SUB2_HOST_NT',
                                'description': "",
                                'friendly': "SUB2_HOST_NT",
                                },
                        0x10:{
                                'name':'SUB2_HOST_UX',
                                'description': "",
                                'friendly': "SUB2_HOST_UX",
                                },
                        0x20:{
                                'name':'SUB2_QUEUE_CHKPNT',
                                'description': "",
                                'friendly': "SUB2_QUEUE_CHKPNT",
                                },
                        0x40:{
                                'name':'SUB2_QUEUE_RERUNNABLE',
                                'description': "",
                                'friendly': "SUB2_QUEUE_RERUNNABLE",
                                },
                        0x80:{
                                'name':'SUB2_IN_FILE_SPOOL',
                                'description': "",
                                'friendly': "SUB2_IN_FILE_SPOOL",
                                },
                        0x100:{
                                'name':'SUB2_JOB_CMD_SPOOL',
                                'description': "",
                                'friendly': "SUB2_JOB_CMD_SPOOL",
                                },
                        0x200:{
                                'name':'SUB2_JOB_PRIORITY',
                                'description': "",
                                'friendly': "SUB2_JOB_PRIORITY",
                                },
                        0x400:{
                                'name':'SUB2_USE_DEF_PROCLIMIT',
                                'description': "",
                                'friendly': "SUB2_USE_DEF_PROCLIMIT",
                                },
                        0x800:{
                                'name':'SUB2_MODIFY_RUN_JOB',
                                'description': "",
                                'friendly': "SUB2_MODIFY_RUN_JOB",
                                },
                        0x1000:{
                                'name':'SUB2_MODIFY_PEND_JOB',
                                'description': "",
                                'friendly': "SUB2_MODIFY_PEND_JOB",
                                },
                        }
class SubmitOption(NumericStatus):
        states={
                        0x01:{
                                'name':'SUB_JOB_NAME',
                                'description': "Submitted with a job name",
                                'friendly': "Job submitted with name",
                                },
                        0x02:{
                                'name':'SUB_QUEUE',
                                'description': "",
                                'friendly': "Job submitted with queue",
                                },
                        0x04:{
                                'name':'SUB_HOST',
                                'description': "",
                                'friendly': "SUB_HOST",
                                },
                        0x08:{
                                'name':'SUB_IN_FILE',
                                'description': "",
                                'friendly': "Job Submitted with input file",
                                },
                        0x10:{
                                'name':'SUB_OUT_FILE',
                                'description': "",
                                'friendly': "Job submitted with output file",
                                },
                        0x20:{
                                'name':'SUB_ERR_FILE',
                                'description': "",
                                'friendly': "Job submitted with error file",
                                },
                        0x40:{
                                'name':'SUB_EXCLUSIVE',
                                'description': "",
                                'friendly': "Job submitted to run exclusively",
                                },
                        0x80:{
                                'name':'SUB_NOTIFY_END',
                                'description': "",
                                'friendly': "SUB_NOTIFY_END",
                                },
                        0x100:{
                                'name':'SUB_NOTIFY_BEGIN',
                                'description': "",
                                'friendly': "SUB_NOTIFY_BEGIN",
                                },
                        0x200:{
                                'name':'SUB_USER_GROUP',
                                'description': "",
                                'friendly': "SUB_USER_GROUP",
                                },
                        0x400:{
                                'name':'SUB_CHKPNT_PERIOD',
                                'description': "",
                                'friendly': "Job submitted with checkpoint period",
                                },
                        0x800:{
                                'name':'SUB_CHKPNT_DIR',
                                'description': "",
                                'friendly': "Job submitted with checkpoint directory",
                                },
                        0x1000:{
                                'name':'SUB_RESTART_FORCE',
                                'description': "",
                                'friendly': "SUB_RESTART_FORCE",
                                },
                        0x2000:{
                                'name':'SUB_RESTART',
                                'description': "",
                                'friendly': "SUB_RESTART",
                                },
                        0x4000:{
                                'name':'SUB_RERUNNABLE',
                                'description': "",
                                'friendly': "Job submitted as rerunnable",
                                },
                        0x8000:{
                                'name':'SUB_WINDOW_SIG',
                                'description': "",
                                'friendly': "SUB_WINDOW_SIG",
                                },
                        0x10000:{
                                'name':'SUB_HOST_SPEC',
                                'description': "",
                                'friendly': "Job submitted with host spec",
                                },
                        0x20000:{
                                'name':'SUB_DEPEND_COND',
                                'description': "",
                                'friendly': "Job submitted with depend conditions",
                                },
                        0x40000:{
                                'name':'SUB_RES_REQ',
                                'description': "",
                                'friendly': "Job submitted with resource request",
                                },
                        0x80000:{
                                'name':'SUB_OTHER_FILES',
                                'description': "",
                                'friendly': "SUB_OTHER_FILES",
                                },
                        0x100000:{
                                'name':'SUB_PRE_EXEC',
                                'description': "",
                                'friendly': "Job submitted with pre exec script",
                                },
                        0x200000:{
                                'name':'SUB_LOGIN_SHELL',
                                'description': "",
                                'friendly': "Job submitted with login shell",
                                },
                        0x400000:{
                                'name':'SUB_MAIL_USER',
                                'description': "",
                                'friendly': "Job submitted to email user",
                                },
                        0x800000:{
                                'name':'SUB_MODIFY',
                                'description': "",
                                'friendly': "SUB_MODIFY",
                                },
                        0x1000000:{
                                'name':'SUB_MODIFY_ONCE',
                                'description': "",
                                'friendly': "SUB_MODIFY_ONCE",
                                },
                        0x2000000:{
                                'name':'SUB_PROJECT_NAME',
                                'description': "",
                                'friendly': "Job submitted to project",
                                },
                        0x4000000:{
                                'name':'SUB_INTERACTIVE',
                                'description': "",
                                'friendly': "Job submitted as interactive",
                                },
                        0x8000000:{
                                'name':'SUB_PTY',
                                'description': "",
                                'friendly': "SUB_PTY",
                                },
                        0x10000000:{
                                'name':'SUB_PTY_SHELL',
                                'description': "",
                                'friendly': "SUB_PTY_SHELL",
                                },
                        }

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
	def json_attributes(self):
		attribs=JobBase.json_attributes(self)
		attribs.extend([
			"checkpoint_directory",
			"checkpoint_period",
			"cpu_factor",
			"cwd",
			"execution_cwd",
			"execution_home_directory",
			"execution_user_id",
			"execution_user_name",
			"host_specification",
			"login_shell",
			"parent_group",
			"pre_execution_command",
			"resource_usage_last_update_time",
			"service_port",
			"submit_home_directory",
			"termination_signal",
		])
		return attribs
	
	@classmethod
	def get_job_list(cls):
		initialize()
		num_jobs=lsblib.lsb_openjobinfo()
		jl= [Job(job=lsblib.lsb_readjobinfo()) for i in range(num_jobs)]
		lsblib.lsb_closejobinfo()
		return jl
	cluster_type="openlava"
	
	def __init__(self, job=None, job_id=None, array_index=0):
		initialize()
		self._last_update_time=0
		if job:
			self._job_id=lsblib.get_job_id(job.jobId)
			self._array_index=lsblib.get_array_index(job.jobId)
			#self._update_jobinfo(job)
		elif job_id:
			self._job_id=job_id
			self._array_index=array_index
			full_job_id=lsblib.create_job_id(job_id, array_index)
			num_jobs=lsblib.lsb_openjobinfo(job_id=full_job_id)
			lsblib.lsb_closejobinfo()
			if num_jobs != 1:
				raise NoSuchJobError("Job: %s[%s] does not exist." % (job_id, array_index))
		else:
			raise ValueError("Job, or job_id required")
		
	def _update_jobinfo(self, job=None):
		if (int(time.time()) - self._last_update_time) < 60:
			return
		self._last_update_time=int(time.time())
		
		full_job_id=lsblib.create_job_id(self.job_id, self.array_index)
		if job==None:
			num_jobs=lsblib.lsb_openjobinfo(job_id=full_job_id)
			if num_jobs == 1:
				job=lsblib.lsb_readjobinfo()
			lsblib.lsb_closejobinfo()
			if num_jobs != 1:
				raise NoSuchJobError("Job: %s[%s] does not exist." % self.job_id, self.array_index)
			
		self._submission_host=job.fromHost
		self._status=job.status
		self._user_name=job.user
		self._submit_time=job.submitTime
		self._start_time=job.startTime
		self._end_time=job.endTime
		self._process_id=job.jobPid
		self._cpu_time=job.cpuTime
		self._cwd=job.cwd
		self._submit_home_directory=job.subHomeDir
		self._execution_hosts=job.exHosts
		self._cpu_factor=job.cpuFactor
		self._execution_user_id=job.execUid
		self._execution_user_name=job.execUsername
		self._execution_cwd=job.execCwd
		self._parent_group=job.parentGroup
		self._name=job.jName
		self._execution_home_directory=job.execHome
		self._service_port=job.port
		self._priority=job.jobPriority
		self._reservation_time=job.reserveTime
		self._predicted_start_time=job.predictedStartTime
		self._resource_usage_last_update_time=job.jRusageUpdateTime
		self._processes=[]
		for pid in job.runRusage.pidInfo:
			self._processes.append(
				Process(
					hostname=None,
					process_id=pid.pid,
					parent_process_id=pid.ppid,
					process_group_id=pid.pgid,
					cray_job_id=pid.jobid,
				)
			)
		names=["CPU Time","File Size","Data Segment Size","Stack Size","Core Size","RSS Size","Num Files","Max Open Files","Swap Limit","Run Limit","Process Limit"]
		rlims=job.submit.rLimits
		units=[ None,"KB","KB","KB","KB","KB",None,None,"KB",None,None]
		self._runtime_limits=[]
		for i in range(len(rlims)):
			self._runtime_limits.append(
				ResourceLimit(
					name=names[i],
					soft_limit=rlims[i],
					hard_limit=rlims[i],
					unit=units[i]				
				)
			)
		
		
		
		self._consumed_resources=[
			ConsumedResource(
				name="Resident Memory",
				value=job.runRusage.mem,
				limit=job.submit.rLimits[lslib.MEM],
				unit="KB",
			),
			ConsumedResource(
				name="Virtual Memory",
				value=job.runRusage.swap,
				limit=job.submit.rLimits[lslib.SWP],
				unit="KB",
			),
			ConsumedResource(
				name="User Time",
				value=datetime.timedelta(seconds=job.runRusage.utime),
				limit=job.submit.rLimits[lslib.UT],
			),
			ConsumedResource(
				name="System Time",
				value=datetime.timedelta(seconds=job.runRusage.stime),
			),
			ConsumedResource(
				name="Num Active Processes",
				value=job.runRusage.npids,
				unit="Processes"
			)
		]
		self._options=SubmitOption.get_status_list(job.submit.options)
		self._options.extend(SubmitOption.get_status_list(job.submit.options2))
		self._name=job.submit.jobName
		self._queue_name=job.submit.queue
		self._requested_hosts=job.submit.askedHosts
		self._requested_resources=job.submit.resReq
		self._host_specification=job.submit.hostSpec
		self._requested_slots=job.submit.numProcessors
		self._max_requested_slots=job.submit.maxNumProcessors
		self._dependency_condition=job.submit.dependCond
		self._begin_time=job.submit.beginTime
		self._termination_time=job.submit.termTime
		self._termination_signal=job.submit.sigValue
		self._input_file_name=job.submit.inFile
		self._output_file_name=job.submit.outFile
		self._error_file_name=job.submit.errFile
		self._command=job.submit.command
		self._checkpoint_period=job.submit.chkpntPeriod
		self._checkpoint_directory=job.submit.chkpntDir
		self._pre_execution_command=job.submit.preExecCmd
		self._email_user=job.submit.mailUser
		self._project_names=[job.submit.projectName]
		self._login_shell=job.submit.loginShell
		self._user_priority=job.submit.userPriority
		ld=lsblib.LoadIndexLog()
		self._pend_reasons=lsblib.lsb_pendreason(job.numReasons, job.reasonTb, None, ld)
		self._susp_reasons=lsblib.lsb_suspreason(job.reasons, job.subreasons, ld)
		
	@property
	def begin_time(self):
		'''Job will not start before this time'''
		self._update_jobinfo()
		return self._begin_time
	
	@property
	def command(self):
		'''Command to execute'''
		self._update_jobinfo()
		return self._command
	
	@property
	def consumed_resources(self):
		'''Array of resource usage information'''
		self._update_jobinfo()
		return self._consumed_resources
	
	@property
	def cpu_time(self):
		'''CPU Time in seconds that the job has consumed'''
		self._update_jobinfo()
		return self._cpu_time
	
	@property
	def dependency_condition(self):
		'''Job dependency information'''
		self._update_jobinfo()
		return self._dependency_condition
	
	@property
	def email_user(self):
		'''User supplied email address to send notifications to'''
		self._update_jobinfo()
		return self._email_user
	
	@property
	def end_time(self):
		'''Time the job ended in seconds since epoch UTC'''
		self._update_jobinfo()
		return self._end_time
	
	@property
	def error_file_name(self):
		'''Path to the error file'''
		self._update_jobinfo()
		return self._error_file_name
	
	@property
	def execution_hosts(self):
		'''List of hosts that job is running on'''
		self._update_jobinfo()
		return [ExecutionHost(hn) for hn in self._execution_hosts]
	
	@property
	def input_file_name(self):
		'''Path to the input file'''
		self._update_jobinfo()
		return self._input_file_name
	
	@property
	def max_requested_slots(self):
		'''The maximum number of job slots that could be used by the job'''
		self._update_jobinfo()
		return self._max_requested_slots
	
	@property
	def name(self):
		'''User or system given name of the job'''
		self._update_jobinfo()
		return self._name
	
	@property
	def options(self):
		'''List of options that apply to the job'''
		self._update_jobinfo()
		return self._options
	
	@property
	def output_file_name(self):
		'''Path to the output file'''
		self._update_jobinfo()
		return self._output_file_name
	
	@property
	def pending_reasons(self):
		'''Text string explainging why the job is pending'''
		self._update_jobinfo()
		return self._pend_reasons
	
	@property
	def predicted_start_time(self):
		'''Predicted start time of the job'''
		self._update_jobinfo()
		return self._predicted_start_time
	
	@property
	def priority(self):
		'''Actual priority of the job'''
		self._update_jobinfo()
		return self._priority
	
	@property
	def process_id(self):
		'''Process id of the job'''
		self._update_jobinfo()
		return self._process_id
	
	@property
	def processes(self):
		'''Array of processes started by the job'''
		self._update_jobinfo()
		return self._processes
	
	@property
	def project_names(self ):
		'''Array of project names that the job was submitted with'''
		self._update_jobinfo()
		return self._project_names
	
	@property
	def requested_resources(self):
		'''Resources requested by the job'''
		self._update_jobinfo()
		return self._requested_resources
	
	@property
	def requested_slots(self):
		'''The number of job slots requested by the job'''
		self._update_jobinfo()
		return self._requested_slots
	
	@property
	def reservation_time(self):
		self._update_jobinfo()
		return self._reservation_time
	
	@property
	def runtime_limits(self):
		'''Array of run time limits imposed on the job'''
		self._update_jobinfo()
		return self._runtime_limits
	
	@property
	def start_time(self):
		'''start time of the job in seconds since epoch UTC'''
		self._update_jobinfo()
		return self._start_time
	
	@property
	def status(self):
		'''Status of the job'''
		self._update_jobinfo()
		return JobStatus(self._status)
	
	@property
	def submission_host(self):
		'''Host job was submitted from'''
		self._update_jobinfo()
		return Host(self._submission_host)
	
	@property
	def submit_time(self):
		'''Submit time in seconds since epoch'''
		self._update_jobinfo()
		return self._submit_time

	@property
	def suspension_reasons(self):
		self._update_jobinfo()
		return self._susp_reasons
	
	@property
	def termination_time(self):
		'''Termination deadline - the job will finish before or on this time'''
		self._update_jobinfo()
		return self._termination_time
	
	@property
	def user_name(self):
		'''User name of the job owner'''
		self._update_jobinfo()
		return self._user_name
	
	@property
	def user_priority(self ):
		'''User given priority of the job'''
		self._update_jobinfo()
		return self._user_priority


	
	def queue(self):
		'''The queue object for the queue the job is currently in.'''
		self._update_jobinfo()
		return Queue(queue_name=self._queue_name)
	
	def requested_hosts(self):
		'''Array of host objects the job was submitted to'''
		self._update_jobinfo()
		return [Host(hn) for hn in self._requested_hosts]
	



	## Openlava Only
	@property
	def checkpoint_directory(self):
		'''Directory to store checkpoint data'''
		self._update_jobinfo()
		return self._checkpoint_directory

	@property
	def checkpoint_period(self):
		'''Number of seconds between sending checkpoint signals'''
		self._update_jobinfo()
		return self._checkpoint_period
	
	@property
	def checkpoint_period_timedelta(self):
		'''Timedelta object for checkpointing period'''
		return datetime.timedelta(seconds=self.checkpoint_period)
	
	@property
	def cpu_factor(self):
		'''CPU Factor of execution host'''
		self._update_jobinfo()
		return self._cpu_factor
	
	@property
	def cwd(self):
		'''Current Working Directory of the job'''
		self._update_jobinfo()
		return self._cwd
	
	@property
	def execution_cwd(self):
		'''Current working directory on the execution host'''
		self._update_jobinfo()
		return self._execution_cwd
	
	@property
	def execution_home_directory(self):
		'''Home directory on execution host'''
		self._update_jobinfo()
		return self._execution_home_directory

	@property	
	def execution_user_id(self):
		'''User ID on execution host'''
		self._update_jobinfo()
		return self._execution_user_id
	
	@property
	def execution_user_name(self):
		'''User name on execution host'''
		self._update_jobinfo()
		return self._execution_user_name
	
	@property
	def host_specification(self):
		'''Host specification'''
		self._update_jobinfo()
		return self._host_specification
	
	@property
	def login_shell(self):
		'''Login shell of the user'''
		self._update_jobinfo()
		return self._login_shell
	
	@property
	def parent_group(self):
		'''Parent job group'''
		self._update_jobinfo()
		return self._parent_group
	
	@property
	def pre_execution_command(self):
		'''User supplied Pre Exec Command'''
		self._update_jobinfo()
		return self._pre_execution_command
	
	@property
	def resource_usage_last_update_time(self):
		self._update_jobinfo()
		return self._resource_usage_last_update_time
	@property
	def resource_usage_last_update_time_local(self):
		return datetime.datetime.fromtimestamp(self.resource_usage_last_update_time)
	
	@property
	def service_port(self):
		'''NIOS Port of the job'''
		self._update_jobinfo()
		return self._service_port
	
	@property
	def submit_home_directory(self):
		'''Home directory on the submit host'''
		self._update_jobinfo()
		return self._submit_home_directory
		
	@property
	def termination_signal(self):
		'''Signal to send when job exceeds termination deadline'''
		self._update_jobinfo()
		return self._termination_signal




class Host(HostBase):
	cluster_type="openlava"
	def json_attributes(self):
		attribs=HostBase.json_attributes(self)
		attribs.extend([
			'cpu_factor',
			'is_server',
			'num_disks',
			'num_user_suspended_jobs',
			'num_user_suspended_slots',
			'num_system_suspended_jobs',
			'num_system_suspended_slots',
			'has_kernel_checkpoint_copy',	
		])
		return attribs
	def __init__(self, host_name):
		initialize()
		self._lsb_update_time=0
		self._update_time=0
		HostBase.__init__(self,host_name)
		
		# check host exists
		self._model=lslib.ls_gethostmodel(host_name)
		if self._model == None:
			raise NoSuchHostError("Host: %s does not exist" % host_name)
		
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
			if r.name in resource_names:
				self._resources.append(r)
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
	def has_checkpoint_support(self):
		'''True if the host supports checkpointing'''
		self._update_lsb_hostinfo()
		return self._has_checkpoint_support
	
	@property
	def host_model(self):
		'''String containing model information'''
		return self._model

	@property
	def host_type(self):
		'''String containing host type information'''
		return lslib.ls_gethosttype(self.name)


	@property
	def resources(self):
		'''Array of resources available'''
		self._update_hostinfo()
		return self._resources

	@property
	def max_jobs(self):
		'''Returns the maximum number of jobs that may execute on this host'''
		self._update_lsb_hostinfo()
		return self._max_jobs

	@property
	def max_processors(self):
		'''Maximum number of processors available on the host'''
		self._update_hostinfo()
		return self._max_processors
	
	@property
	def max_ram(self):
		'''Max Ram'''
		self._update_hostinfo()
		return self._max_ram
		
	@property
	def max_slots(self):
		'''Returns the maximum number of scheduling slots that may be consumed on this host'''
		self._update_lsb_hostinfo()
		return self._max_slots
	

	@property
	def max_swap(self):
		'''Max swap space'''
		self._update_hostinfo()
		return self._max_swap
	
	@property
	def max_tmp(self):
		'''Max tmp space'''
		self._update_hostinfo()
		return self._max_tmp

	@property
	def num_reserved_slots(self):
		'''Returns the number of scheduling slots that are reserved'''
		self._update_lsb_hostinfo()
		return self._num_reserved_slots
	
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
	def status(self):
		'''Array of statuses that apply to the host'''
		self._update_lsb_hostinfo()
		return HostStatus.get_status_list(self._status)

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


	#Openlava Only
	
	@property
	def cpu_factor(self):
		'''Openlava Specific - returns the CPU factor of the host'''
		return lslib.ls_gethostfactor(self.name)
		
	@property
	def is_server(self):
		'''True if host is an openlava server (as opposed to submission host)'''
		self._update_hostinfo()
		return self._is_server
	
	@property
	def num_disks(self):
		'''Openlava specific: Returns the number of physical disks installed in the machine'''
		self._update_hostinfo()
		return self._num_disks
		
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
	def has_kernel_checkpoint_copy(self):
		'''Returns true if the host supports kernel checkpointing'''
		self._update_lsb_hostinfo()
		return self._has_kernel_checkpoint_support



	def jobs(self, job_id=0, job_name="", user="all", queue="", options=0):
		'''Return jobs on this host'''
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
	
	def load_information(self):
		'''Return load information on the host'''
		self._update_lsb_hostinfo()

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
	
	def json_attributes(self):
		return ['name','description','type','order','interval','flags']
	
class ExecutionHost(Host):
	def __init__(self, host_name, num_slots=1):
		Host.__init__(self,host_name)
		self.num_slots=num_slots
	def json_attributes(self):
		attribs=Host.json_attributes(self)
		attribs.append('num_slots')
		return attribs
	
class Queue:
	def __init__(self, queue_name=None):
			self.name=queue_name

	def json_attributes(self):
		return ['name']	
