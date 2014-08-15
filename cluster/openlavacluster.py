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
from cluster import *
from openlava import lslib, lsblib
import datetime
import time

initialized_openlava = False


def initialize():
    global initialized_openlava
    if initialized_openlava == False:
        if lsblib.lsb_init("Openlava Cluster Interface") != 0:
            raise OpenLavaError(lslib.ls_sysmsg)
        else:
            initialized_openlava = True


def raise_cluster_exception(code, message):
    messages = {
    0: "No error",
    1: "No matching job found",
    2: "Job has not started yet",
    3: "Job has already started",
    4: "Job has already finished",
    5: "Error 5",
    6: "Dependency condition syntax error",
    7: "Queue does not accept EXCLUSIVE jobs",
    8: "Root job submission is disabled",
    9: "Job is already being migrated",
    10: "Job is not checkpointable",
    11: "No output so far",
    12: "No job Id can be used now",
    13: "Queue only accepts interactive jobs",
    14: "Queue does not accept interactive jobs",
    15: "No user is defined in the lsb.users file",
    16: "Unknown user",
    17: "User permission denied",
    18: "No such queue",
    19: "Queue name must be specified",
    20: "Queue has been closed",
    21: "Not activated because queue windows are closed",
    22: "User cannot use the queue",
    23: "Bad host name, host group name or cluster name",
    24: "Too many processors requested",
    25: "Reserved for future use",
    26: "Reserved for future use",
    27: "No user/host group defined in the system",
    28: "No such user/host group",
    29: "Host or host group is not used by the queue",
    30: "Queue does not have enough per-user job slots",
    31: "Current host is more suitable at this time",
    32: "Checkpoint log is not found or is corrupted",
    33: "Queue does not have enough per-processor job slots",
    34: "Request from non-LSF host rejected",
    35: "Bad argument",
    36: "Bad time specification",
    37: "Start time is later than termination time",
    38: "Bad CPU limit specification",
    39: "Cannot exceed queue's hard limit(s)",
    40: "Empty job",
    41: "Signal not supported",
    42: "Bad job name",
    43: "The destination queue has reached its job limit",
    44: "Unknown event",
    45: "Bad event format",
    46: "End of file",
    47: "Master batch daemon internal error",
    48: "Slave batch daemon internal error",
    49: "Batch library internal error",
    50: "Failed in an LSF library call",
    51: "System call failed",
    52: "Cannot allocate memory",
    53: "Batch service not registered",
    54: "LSB_SHAREDIR not defined",
    55: "Checkpoint system call failed",
    56: "Batch daemon cannot fork",
    57: "Batch protocol error",
    58: "XDR encode/decode error",
    59: "Fail to bind to an appropriate port number",
    60: "Contacting batch daemon: Communication timeout",
    61: "Timeout on connect call to server",
    62: "Connection refused by server",
    63: "Server connection already exists",
    64: "Server is not connected",
    65: "Unable to contact execution host",
    66: "Operation is in progress",
    67: "User or one of user's groups does not have enough job slots",
    68: "Job parameters cannot be changed now; non-repetitive job is running",
    69: "Modified parameters have not been used",
    70: "Job cannot be run more than once",
    71: "Unknown cluster name or cluster master",
    72: "Modified parameters are being used",
    73: "Queue does not have enough per-host job slots",
    74: "Mbatchd could not find the message that SBD mentions about",
    75: "Bad resource requirement syntax",
    76: "Not enough host(s) currently eligible",
    77: "Error 77",
    78: "Error 78",
    79: "No resource defined",
    80: "Bad resource name",
    81: "Interactive job cannot be rerunnable",
    82: "Input file not allowed with pseudo-terminal",
    83: "Cannot find restarted or newly submitted job's submission host and host type",
    84: "Error 109",
    85: "User not in the specified user group",
    86: "Cannot exceed queue's resource reservation",
    87: "Bad host specification",
    88: "Bad user group name",
    89: "Request aborted by esub",
    90: "Bad or invalid action specification",
    91: "Has dependent jobs",
    92: "Job group does not exist",
    93: "Bad/empty job group name",
    94: "Cannot operate on job array",
    95: "Operation not supported for a suspended job",
    96: "Operation not supported for a forwarded job",
    97: "Job array index error",
    98: "Job array index too large",
    99: "Job array does not exist",
    100: "Job exists",
    101: "Cannot operate on element job",
    102: "Bad jobId",
    103: "Change job name is not allowed for job array",
    104: "Child process died",
    105: "Invoker is not in specified project group",
    106: "No host group defined in the system",
    107: "No user group defined in the system",
    108: "Unknown jobid index file format",
    109: "Source file for spooling does not exist",
    110: "Number of failed spool hosts reached max",
    111: "Spool copy failed for this host",
    112: "Fork for spooling failed",
    113: "Status of spool child is not available",
    114: "Spool child terminated with failure",
    115: "Unable to find a host for spooling",
    116: "Cannot get $JOB_SPOOL_DIR for this host",
    117: "Cannot delete spool file for this host",
    118: "Bad user priority",
    119: "Job priority control undefined",
    120: "Job has already been requeued",
    121: "Multiple first execution hosts specified",
    122: "Host group specified as first execution host",
    123: "Host partition specified as first execution host",
    124: "\"Others\" specified as first execution host",
    125: "Too few processors requested",
    126: "Only the following parameters can be used to modify a running job: -c, -M, -W, -o, -e, -r",
    127: "You must set LSB_JOB_CPULIMIT in lsf.conf to modify the CPU limit of a running job",
    128: "You must set LSB_JOB_MEMLIMIT in lsf.conf to modify the memory limit of a running job",
    129: "No error file specified before job dispatch. Error file does not exist, so error file name cannot be changed",
    130: "The host is locked by master LIM",
    131: "Dependent arrays do not have the same size",
    }
    e = ClusterException
    if code == lsblib.LSBE_NO_JOB:
        e = NoSuchJobError
    elif code == lsblib.LSBE_NO_USER or code == lsblib.LSBE_BAD_USER:
        e = NoSuchUserError
    elif code == lsblib.LSBE_PERMISSION or code == lsblib.LSBE_QUEUE_USE:
        e = PermissionDeniedError
    elif code == lsblib.LSBE_BAD_QUEUE:
        e = NoSuchQueueError
    elif code == lsblib.LSBE_BAD_HOST:
        e = NoSuchHostError
    raise e("%s: %s" % (message, messages[code]), code=code)


class Cluster(ClusterBase):
    cluster_type = "openlava"

    def __init__(self):
        initialize()

    @property
    def name(self):
        return lslib.ls_getclustername()

    @property
    def master(self):
        return Host(lslib.ls_getmastername())

    def hosts(self):
        """Returns an array of hosts that are part of the cluster"""
        return Host.get_host_list()

    def queues(self):
        """Returns an array of queues that are part of the cluster"""
        return Queue.get_queue_list()

    def jobs(self):
        """Returns an array of jobs that are part of the cluster"""
        return Job.get_job_list()

    def resources(self):
        """Returns an array of resources that are part of thecluster"""
        cluster_info = lslib.ls_info()
        if cluster_info == None:
            raise OpenLavaError(lslib.ls_sysmsg())
        return [Resource(r) for r in cluster_info.resTable]

    @property
    def admins(self):
        """
		Gets the cluster administrators.  Cluster administrators can perform any action on the scheduling system.  This does not imply they are actual superusers on the physical systems.
		:returns: Array of usernames
		:rtype: array
		:raise: OpenLavaError on failure
		"""
        cluster_info = lslib.ls_clusterinfo(clusterList=[lslib.ls_getclustername()], listsize=1)
        if cluster_info == None:
            raise OpenLavaError(lslib.ls_sysmsg())
        cluster_info = cluster_info[0]
        if cluster_info.clusterName != lslib.ls_getclustername():
            raise OpenLavaError("Cluster returned didnt match cluster name")
        return cluster_info.admins

    def users(self):
        return User.get_user_list()


class OpenLavaError(ClusterException):
    pass


class NumericStatus(Status):
    def json_attributes(self):
        return ['name', 'description', 'status', 'friendly']

    def __init__(self, status):
        self._status = status

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
        try:
            return u"%s" % self.states[self._status]['name']
        except KeyError:
            return 'UNKNOWN'


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
            return u"Undetermined: %s" % self._status

    @classmethod
    def get_status_list(cls, mask):
        statuses = []
        for key in cls.states.keys():
            if (key & mask) == key:
                statuses.append(cls(key))
        return statuses


class Submit2Option(NumericStatus):
    states = {
        0x01: {
            'name': 'SUB2_HOLD',
            'description': "",
            'friendly': "SUB2_HOLD",
        },
        0x02: {
            'name': 'SUB2_MODIFY_CMD',
            'description': "",
            'friendly': "SUB2_MODIFY_CMD",
        },
        0x04: {
            'name': 'SUB2_BSUB_BLOCK',
            'description': "",
            'friendly': "SUB2_BSUB_BLOCK",
        },
        0x08: {
            'name': 'SUB2_HOST_NT',
            'description': "",
            'friendly': "SUB2_HOST_NT",
        },
        0x10: {
            'name': 'SUB2_HOST_UX',
            'description': "",
            'friendly': "SUB2_HOST_UX",
        },
        0x20: {
            'name': 'SUB2_QUEUE_CHKPNT',
            'description': "",
            'friendly': "SUB2_QUEUE_CHKPNT",
        },
        0x40: {
            'name': 'SUB2_QUEUE_RERUNNABLE',
            'description': "",
            'friendly': "SUB2_QUEUE_RERUNNABLE",
        },
        0x80: {
            'name': 'SUB2_IN_FILE_SPOOL',
            'description': "",
            'friendly': "SUB2_IN_FILE_SPOOL",
        },
        0x100: {
            'name': 'SUB2_JOB_CMD_SPOOL',
            'description': "",
            'friendly': "SUB2_JOB_CMD_SPOOL",
        },
        0x200: {
            'name': 'SUB2_JOB_PRIORITY',
            'description': "",
            'friendly': "SUB2_JOB_PRIORITY",
        },
        0x400: {
            'name': 'SUB2_USE_DEF_PROCLIMIT',
            'description': "",
            'friendly': "SUB2_USE_DEF_PROCLIMIT",
        },
        0x800: {
            'name': 'SUB2_MODIFY_RUN_JOB',
            'description': "",
            'friendly': "SUB2_MODIFY_RUN_JOB",
        },
        0x1000: {
            'name': 'SUB2_MODIFY_PEND_JOB',
            'description': "",
            'friendly': "SUB2_MODIFY_PEND_JOB",
        },
    }


class SubmitOption(NumericStatus):
    states = {
        0x01: {
            'name': 'SUB_JOB_NAME',
            'description': "Submitted with a job name",
            'friendly': "Job submitted with name",
        },
        0x02: {
            'name': 'SUB_QUEUE',
            'description': "",
            'friendly': "Job submitted with queue",
        },
        0x04: {
            'name': 'SUB_HOST',
            'description': "",
            'friendly': "SUB_HOST",
        },
        0x08: {
            'name': 'SUB_IN_FILE',
            'description': "",
            'friendly': "Job Submitted with input file",
        },
        0x10: {
            'name': 'SUB_OUT_FILE',
            'description': "",
            'friendly': "Job submitted with output file",
        },
        0x20: {
            'name': 'SUB_ERR_FILE',
            'description': "",
            'friendly': "Job submitted with error file",
        },
        0x40: {
            'name': 'SUB_EXCLUSIVE',
            'description': "",
            'friendly': "Job submitted to run exclusively",
        },
        0x80: {
            'name': 'SUB_NOTIFY_END',
            'description': "",
            'friendly': "SUB_NOTIFY_END",
        },
        0x100: {
            'name': 'SUB_NOTIFY_BEGIN',
            'description': "",
            'friendly': "SUB_NOTIFY_BEGIN",
        },
        0x200: {
            'name': 'SUB_USER_GROUP',
            'description': "",
            'friendly': "SUB_USER_GROUP",
        },
        0x400: {
            'name': 'SUB_CHKPNT_PERIOD',
            'description': "",
            'friendly': "Job submitted with checkpoint period",
        },
        0x800: {
            'name': 'SUB_CHKPNT_DIR',
            'description': "",
            'friendly': "Job submitted with checkpoint directory",
        },
        0x1000: {
            'name': 'SUB_RESTART_FORCE',
            'description': "",
            'friendly': "SUB_RESTART_FORCE",
        },
        0x2000: {
            'name': 'SUB_RESTART',
            'description': "",
            'friendly': "SUB_RESTART",
        },
        0x4000: {
            'name': 'SUB_RERUNNABLE',
            'description': "",
            'friendly': "Job submitted as rerunnable",
        },
        0x8000: {
            'name': 'SUB_WINDOW_SIG',
            'description': "",
            'friendly': "SUB_WINDOW_SIG",
        },
        0x10000: {
            'name': 'SUB_HOST_SPEC',
            'description': "",
            'friendly': "Job submitted with host spec",
        },
        0x20000: {
            'name': 'SUB_DEPEND_COND',
            'description': "",
            'friendly': "Job submitted with depend conditions",
        },
        0x40000: {
            'name': 'SUB_RES_REQ',
            'description': "",
            'friendly': "Job submitted with resource request",
        },
        0x80000: {
            'name': 'SUB_OTHER_FILES',
            'description': "",
            'friendly': "SUB_OTHER_FILES",
        },
        0x100000: {
            'name': 'SUB_PRE_EXEC',
            'description': "",
            'friendly': "Job submitted with pre exec script",
        },
        0x200000: {
            'name': 'SUB_LOGIN_SHELL',
            'description': "",
            'friendly': "Job submitted with login shell",
        },
        0x400000: {
            'name': 'SUB_MAIL_USER',
            'description': "",
            'friendly': "Job submitted to email user",
        },
        0x800000: {
            'name': 'SUB_MODIFY',
            'description': "",
            'friendly': "SUB_MODIFY",
        },
        0x1000000: {
            'name': 'SUB_MODIFY_ONCE',
            'description': "",
            'friendly': "SUB_MODIFY_ONCE",
        },
        0x2000000: {
            'name': 'SUB_PROJECT_NAME',
            'description': "",
            'friendly': "Job submitted to project",
        },
        0x4000000: {
            'name': 'SUB_INTERACTIVE',
            'description': "",
            'friendly': "Job submitted as interactive",
        },
        0x8000000: {
            'name': 'SUB_PTY',
            'description': "",
            'friendly': "SUB_PTY",
        },
        0x10000000: {
            'name': 'SUB_PTY_SHELL',
            'description': "",
            'friendly': "SUB_PTY_SHELL",
        },
    }


class HostStatus(NumericStatus):
    states = {
    0x0: {
    'friendly': 'Ok',
    'name': 'HOST_STAT_OK',
    'description': "Ready to accept and run jobs.  ",
    },
    0x01: {
    'friendly': 'Busy',
    'name': 'HOST_STAT_BUSY',
    'description': "The host load is greater than a scheduling threshold.  In this status, no new job will be scheduled to run on this host.  ",
    },
    0x02: {
    'friendly': 'Dispatch Window Closed',
    'name': 'HOST_STAT_WIND',
    'description': "The host dispatch window is closed.  In this status, no new job will be accepted.  ",
    },
    0x04: {
    'friendly': 'Disabled by Administrator',
    'name': 'HOST_STAT_DISABLED',
    'description': "The host has been disabled by the LSF administrator and will not accept jobs.  In this status, no new job will be scheduled to run on this host.  ",
    },
    0x08: {
    'friendly': 'Locked',
    'name': 'HOST_STAT_LOCKED',
    'description': "The host is locked by a exclusive task.  In this status, no new job will be scheduled to run on this host.  ",
    },
    0x10: {
    'friendly': 'Full',
    'name': 'HOST_STAT_FULL',
    'description': "Great than job limit.  The host has reached its job limit. In this status, no new job will be scheduled to run on this host.  ",
    },
    0x20: {
    'friendly': 'Unreachable',
    'name': 'HOST_STAT_UNREACH',
    'description': "The sbatchd on this host is unreachable.  ",
    },
    0x40: {
    'friendly': 'Unavailable',
    'name': 'HOST_STAT_UNAVAIL',
    'description': "The LIM and sbatchd on this host are unavailable.  ",
    },
    0x80: {
    'friendly': 'No LIM',
    'name': 'HOST_STAT_NO_LIM',
    'description': "The host is running an sbatchd but not a LIM.  ",
    },
    0x100: {
    'friendly': 'Exclusive',
    'name': 'HOST_STAT_EXCLUSIVE',
    'description': "Running exclusive job.  ",
    },
    0x200: {
    'friendly': 'Locked by Master LIM',
    'name': 'HOST_STAT_LOCKED_MASTER',
    'description': "Lim locked by master LIM.  ",
    },
    }


class JobStatus(NumericStatus):
    states = {
    0x00: {
    'friendly': "Null",
    'name': 'JOB_STAT_NULL',
    'description': 'State null.',
    },
    0x01: {
    'friendly': "Pending",
    'name': 'JOB_STAT_PEND',
    'description': 'The job is pending, i.e., it has not been dispatched yet.',
    },
    0x02: {
    'friendly': "Held",
    'name': "JOB_STAT_PSUSP",
    'description': "The pending job was suspended by its owner or the LSF system administrator.",
    },
    0x04: {
    'friendly': "Running",
    'name': "JOB_STAT_RUN",
    'description': "The job is running.",
    },
    0x08: {
    'friendly': "Suspended by system",
    'name': "JOB_STAT_SSUSP",
    'description': "The running job was suspended by the system because an execution host was overloaded or the queue run window closed.",
    },
    0x10: {
    'friendly': "Suspended by user",
    'name': "JOB_STAT_USUSP",
    'description': "The running job was suspended by its owner or the LSF system administrator.",
    },
    0x20: {
    'friendly': "Exited",
    'name': "JOB_STAT_EXIT",
    'description': "The job has terminated with a non-zero status - it may have been aborted due to an error in its execution, or killed by its owner or by the LSF system administrator.",
    },
    0x40: {
    'friendly': "Completed",
    'name': "JOB_STAT_DONE",
    'description': "The job has terminated with status 0.",
    },
    0x80: {
    'friendly': "Process Completed",
    'name': "JOB_STAT_PDONE",
    'description': "Post job process done successfully.",
    },
    0x100: {
    'friendly': "Process Error",
    'name': "JOB_STAT_PERR",
    'description': "Post job process has error.",
    },
    0x200: {
    'friendly': "Waiting for execution",
    'name': "JOB_STAT_WAIT",
    'description': "Chunk job waiting its turn to exec.",
    },
    0x10000: {
    'friendly': "Unknown",
    'name': "JOB_STAT_UNKWN",
    'description': "The slave batch daemon (sbatchd) on the host on which the job is processed has lost contact with the master batch daemon (mbatchd).",
    },
    }


class Job(JobBase):
    @classmethod
    def submit(cls, **kwargs):
        options = 0
        options2 = 0
        #beginTime
        #termTime
        #rlimits
        fields = {
        'options': {
        'sname': 'options',
        'options': 0,
        'options2': 0,
        },
        'options2': {
        'sname': 'options2',
        'options': 0,
        'options2': 0,
        },
        'num_processors': {
        'sname': 'numProcessors',
        'options': 0,
        'options2': 0,
        },
        'command': {
        'sname': 'command',
        'options': 0,
        'options2': 0,
        },
        'job_name': {
        'sname': 'jobName',
        'options': lsblib.SUB_JOB_NAME,
        'options2': 0,
        },
        'queue_name': {
        'sname': 'queue',
        'options': lsblib.SUB_QUEUE,
        'options2': 0,
        },
        'requested_hosts': {
        'sname': 'askedHosts',
        'options': lsblib.SUB_HOST,
        'options2': 0,
        },
        'resource_request': {
        'sname': 'resReq',
        'options': lsblib.SUB_RES_REQ,
        'options2': 0,
        },
        'host_specification': {
        'sname': 'hostSpec',
        'options': lsblib.SUB_HOST_SPEC,
        'options2': 0,
        },
        'dependency_conditions': {
        'sname': 'dependCond',
        'options': lsblib.SUB_DEPEND_COND,
        'options2': 0,
        },
        'signal_value': {
        'sname': 'sigValue',
        'options': lsblib.SUB_WINDOW_SIG,
        'options2': 0,
        },
        'input_file': {
        'sname': 'inFile',
        'options': lsblib.SUB_IN_FILE,
        'options2': 0,
        },
        'output_file': {
        'sname': 'outFile',
        'options': lsblib.SUB_OUT_FILE,
        'options2': 0,
        },
        'error_file': {
        'sname': 'errFile',
        'options': lsblib.SUB_ERR_FILE,
        'options2': 0,
        },
        'checkpoint_period': {
        'sname': 'chkpntPeriod',
        'options': lsblib.SUB_CHKPNT_PERIOD,
        'options2': 0,
        },
        'checkpoint_directory': {
        'sname': 'chkpntDir',
        'options': lsblib.SUB_CHKPNT_DIR,
        'options2': 0,
        },
        'email_user': {
        'sname': 'mailUser',
        'options': lsblib.SUB_MAIL_USER,
        'options2': 0,
        },
        'project_name': {
        'sname': 'projectName',
        'options': lsblib.SUB_PROJECT_NAME,
        'options2': 0,
        },
        'max_num_processors': {
        'sname': 'maxNumProcessors',
        'options': 0,
        'options2': 0,
        },
        'login_shell': {
        'sname': 'loginShell',
        'options': lsblib.SUB_LOGIN_SHELL,
        'options2': 0,
        },
        'user_priority': {
        'sname': 'userPriority',
        'options': 0,
        'options2': lsblib.SUB2_JOB_PRIORITY,
        },
        }

        s = lsblib.Submit()
        for k, v in kwargs.items():
            if k not in fields:
                raise JobSubmitError("Field: %s is not a valid field name" % k)
            print "setting %s to %s" % ( fields[k]['sname'], v)
            setattr(s, fields[k]['sname'], v)
            print "got %s from %s" % (getattr(s, fields[k]['sname']), fields[k]['sname'])
            options = options | fields[k]['options']
            options2 = options2 | fields[k]['options2']
        print "options: %s" % options
        s.command = kwargs['command']
        options = s.options | options
        s.options = options
        options2 = s.options2 | options2
        s.options2 = options2
        if s.maxNumProcessors < s.numProcessors:
            s.maxNumProcessors = s.numProcessors
        sr = lsblib.SubmitReply()
        job_id = lsblib.lsb_submit(s, sr)
        print "Job submitted"
        if job_id < 0:
            raise_cluster_exception(lsblib.get_lsberrno(), "Unable to submit job")

        job_id = lsblib.get_job_id(job_id)

        num_jobs = lsblib.lsb_openjobinfo(job_id, options=lsblib.JOBID_ONLY | lsblib.ALL_JOB)
        jobs = [Job(job=lsblib.lsb_readjobinfo()) for i in range(num_jobs)]

        lsblib.lsb_closejobinfo()
        print "Closed"
        if len(jobs) == 1:
            return jobs[1]
        return jobs


    def json_attributes(self):
        attribs = JobBase.json_attributes(self)
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
    def get_job_list(cls, job_id=0, array_index=0, queue_name="", host_name="", user_name="all", job_state="ACT",
                     job_name=""):
        initialize()
        if job_state == 'ACT':
            job_state = lsblib.CUR_JOB
        elif job_state == "ALL":
            job_state = lsblib.ALL_JOB
        elif job_state == "EXIT":
            job_state = lsblib.DONE_JOB
        elif job_state == "PEND":
            job_state = lsblib.PEND_JOB
        elif job_state == "RUN":
            job_state = lsblib.RUN_JOB
        elif job_state == "SUSP":
            job_state = lsblib.SUSP_JOB
        else:
            job_state = lsblib.ALL_JOB

        real_job_id = lsblib.create_job_id(job_id=0, array_index=array_index)
        num_jobs = lsblib.lsb_openjobinfo(job_id=real_job_id, user=user_name, queue=queue_name, host=host_name,
                                          job_name=job_name, options=job_state)
        jl = [Job(job=lsblib.lsb_readjobinfo()) for i in range(num_jobs)]
        lsblib.lsb_closejobinfo()
        return jl

    cluster_type = "openlava"

    def __init__(self, job=None, job_id=None, array_index=0):
        initialize()
        self._last_update_time = 0
        if job:
            self._job_id = lsblib.get_job_id(job.jobId)
            self._array_index = lsblib.get_array_index(job.jobId)
            self._update_jobinfo(job)
        elif job_id:
            self._job_id = job_id
            self._array_index = array_index
            full_job_id = lsblib.create_job_id(job_id, array_index)
            num_jobs = lsblib.lsb_openjobinfo(job_id=full_job_id, options=lsblib.ALL_JOB)
            lsblib.lsb_closejobinfo()
            if num_jobs != 1:
                errno = lsblib.get_lsberrno()
                if errno == lsblib.LSBE_NO_JOB:
                    raise NoSuchJobError("Job: %s[%s] does not exist." % (job_id, array_index))
                elif errno == 0:
                    raise NoSuchJobError("Job: %s[%s] does not exist." % (job_id, array_index))
                else:
                    raise ClusterException("%s" % lsblib.ls_sysmsg())
        else:
            raise ValueError("Job, or job_id required")

    def _update_jobinfo(self, job=None):
        if (int(time.time()) - self._last_update_time) < 60:
            return
        self._last_update_time = int(time.time())

        full_job_id = lsblib.create_job_id(self.job_id, self.array_index)
        if job == None:
            num_jobs = lsblib.lsb_openjobinfo(job_id=full_job_id, options=lsblib.ALL_JOB)
            if num_jobs == 1:
                job = lsblib.lsb_readjobinfo()
            lsblib.lsb_closejobinfo()
            if num_jobs != 1:
                raise NoSuchJobError("Job: %s[%s] does not exist." % (self.job_id, self.array_index))
        self._exit_status = job.exitStatus
        self._submission_host = job.fromHost
        self._status = job.status
        self._user_name = job.user
        self._submit_time = job.submitTime
        self._start_time = job.startTime
        self._end_time = job.endTime
        self._process_id = job.jobPid
        self._cpu_time = job.cpuTime
        self._cwd = job.cwd
        self._submit_home_directory = job.subHomeDir
        self._execution_hosts = job.exHosts
        self._cpu_factor = job.cpuFactor
        self._execution_user_id = job.execUid
        self._execution_user_name = job.execUsername
        self._execution_cwd = job.execCwd
        self._parent_group = job.parentGroup
        self._name = job.jName
        self._execution_home_directory = job.execHome
        self._service_port = job.port
        self._priority = job.jobPriority
        self._reservation_time = job.reserveTime
        self._predicted_start_time = job.predictedStartTime
        self._resource_usage_last_update_time = job.jRusageUpdateTime
        self._processes = []
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
        names = ["CPU Time", "File Size", "Data Segment Size", "Stack Size", "Core Size", "RSS Size", "Num Files",
                 "Max Open Files", "Swap Limit", "Run Limit", "Process Limit"]
        rlims = job.submit.rLimits
        units = [None, "KB", "KB", "KB", "KB", "KB", None, None, "KB", None, None]
        self._runtime_limits = []
        for i in range(len(rlims)):
            self._runtime_limits.append(
                ResourceLimit(
                    name=names[i],
                    soft_limit=rlims[i],
                    hard_limit=rlims[i],
                    unit=units[i]
                )
            )

        self._consumed_resources = [
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
        self._options = SubmitOption.get_status_list(job.submit.options)
        self._options.extend(SubmitOption.get_status_list(job.submit.options2))
        self._name = job.submit.jobName
        self._queue_name = job.submit.queue
        self._requested_hosts = job.submit.askedHosts
        self._requested_resources = job.submit.resReq
        self._host_specification = job.submit.hostSpec
        self._requested_slots = job.submit.numProcessors
        self._max_requested_slots = job.submit.maxNumProcessors
        self._dependency_condition = job.submit.dependCond
        self._begin_time = job.submit.beginTime
        self._termination_time = job.submit.termTime
        self._termination_signal = job.submit.sigValue
        self._input_file_name = job.submit.inFile
        self._output_file_name = job.submit.outFile
        self._error_file_name = job.submit.errFile
        self._command = job.submit.command
        self._checkpoint_period = job.submit.chkpntPeriod
        self._checkpoint_directory = job.submit.chkpntDir
        self._pre_execution_command = job.submit.preExecCmd
        self._email_user = job.submit.mailUser
        self._project_names = [job.submit.projectName]
        self._login_shell = job.submit.loginShell
        self._user_priority = job.submit.userPriority
        ld = lsblib.LoadIndexLog()
        self._pend_reasons = " ".join(lsblib.lsb_pendreason(job.numReasons, job.reasonTb, None, ld).splitlines())
        self._susp_reasons = " ".join(lsblib.lsb_suspreason(job.reasons, job.subreasons, ld).splitlines())

    @property
    def admins(self):
        return [self.user_name] + self.queue().admins

    @property
    def begin_time(self):
        """Job will not start before this time"""
        self._update_jobinfo()
        return self._begin_time

    @property
    def command(self):
        """Command to execute"""
        self._update_jobinfo()
        return self._command

    @property
    def consumed_resources(self):
        """Array of resource usage information"""
        self._update_jobinfo()
        return self._consumed_resources

    @property
    def cpu_time(self):
        """CPU Time in seconds that the job has consumed"""
        self._update_jobinfo()
        return self._cpu_time

    @property
    def dependency_condition(self):
        """Job dependency information"""
        self._update_jobinfo()
        return self._dependency_condition

    @property
    def email_user(self):
        """User supplied email address to send notifications to"""
        self._update_jobinfo()
        return self._email_user

    @property
    def end_time(self):
        """Time the job ended in seconds since epoch UTC"""
        self._update_jobinfo()
        return self._end_time

    @property
    def error_file_name(self):
        """Path to the error file"""
        self._update_jobinfo()
        return self._error_file_name

    @property
    def execution_hosts(self):
        """List of hosts that job is running on"""
        self._update_jobinfo()
        return [ExecutionHost(hn) for hn in self._execution_hosts]

    @property
    def input_file_name(self):
        """Path to the input file"""
        self._update_jobinfo()
        return self._input_file_name

    @property
    def is_completed(self):
        if self.status.name == "JOB_STAT_DONE":
            return True
        return False

    @property
    def was_killed(self):
        if self.status.name == "JOB_STAT_EXIT" and self._exit_status == 130:
            return True
        else:
            return False


    @property
    def is_failed(self):
        if self.status.name == "JOB_STAT_EXIT":
            return True
        return False

    @property
    def is_pending(self):
        if self.status.name == "JOB_STAT_PEND":
            return True
        return False

    @property
    def is_running(self):
        if self.status.name == "JOB_STAT_RUN":
            return True
        return False

    @property
    def is_suspended(self):
        if self.status.name == "JOB_STAT_USUSP" or self.status.name == "JOB_STAT_SSUSP" or self.status.name == "JOB_STAT_PSUSP":
            return True
        return False

    @property
    def max_requested_slots(self):
        """The maximum number of job slots that could be used by the job"""
        self._update_jobinfo()
        return self._max_requested_slots

    @property
    def name(self):
        """User or system given name of the job"""
        self._update_jobinfo()
        return self._name

    @property
    def options(self):
        """List of options that apply to the job"""
        self._update_jobinfo()
        return self._options

    @property
    def output_file_name(self):
        """Path to the output file"""
        self._update_jobinfo()
        return self._output_file_name

    @property
    def pending_reasons(self):
        """Text string explainging why the job is pending"""
        self._update_jobinfo()
        return self._pend_reasons

    @property
    def predicted_start_time(self):
        """Predicted start time of the job"""
        self._update_jobinfo()
        return self._predicted_start_time

    @property
    def priority(self):
        """Actual priority of the job"""
        self._update_jobinfo()
        return self._priority

    @property
    def process_id(self):
        """Process id of the job"""
        self._update_jobinfo()
        return self._process_id

    @property
    def processes(self):
        """Array of processes started by the job"""
        self._update_jobinfo()
        return self._processes

    @property
    def project_names(self):
        """Array of project names that the job was submitted with"""
        self._update_jobinfo()
        return self._project_names

    @property
    def requested_resources(self):
        """Resources requested by the job"""
        self._update_jobinfo()
        return self._requested_resources

    @property
    def requested_slots(self):
        """The number of job slots requested by the job"""
        self._update_jobinfo()
        return self._requested_slots

    @property
    def reservation_time(self):
        self._update_jobinfo()
        return self._reservation_time

    @property
    def runtime_limits(self):
        """Array of run time limits imposed on the job"""
        self._update_jobinfo()
        return self._runtime_limits

    @property
    def start_time(self):
        """start time of the job in seconds since epoch UTC"""
        self._update_jobinfo()
        return self._start_time

    @property
    def status(self):
        """Status of the job"""
        self._update_jobinfo()
        status = self._status
        if status & lsblib.JOB_STAT_DONE: # If its done, its done.
            status = 0x40
        return JobStatus(status)

    @property
    def submission_host(self):
        """Host job was submitted from"""
        self._update_jobinfo()
        return Host(self._submission_host)

    @property
    def submit_time(self):
        """Submit time in seconds since epoch"""
        self._update_jobinfo()
        return self._submit_time

    @property
    def suspension_reasons(self):
        self._update_jobinfo()
        return self._susp_reasons

    @property
    def termination_time(self):
        """Termination deadline - the job will finish before or on this time"""
        self._update_jobinfo()
        return self._termination_time

    @property
    def user_name(self):
        """User name of the job owner"""
        self._update_jobinfo()
        return self._user_name

    @property
    def user_priority(self):
        """User given priority of the job"""
        self._update_jobinfo()
        return self._user_priority


    def queue(self):
        """The queue object for the queue the job is currently in."""
        self._update_jobinfo()
        return Queue(self._queue_name)

    def requested_hosts(self):
        """Array of host objects the job was submitted to"""
        self._update_jobinfo()
        return [Host(hn) for hn in self._requested_hosts]

    def kill(self):
        full_job_id = lsblib.create_job_id(job_id=self.job_id, array_index=self.array_index)
        rc = lsblib.lsb_signaljob(full_job_id, lsblib.SIGKILL)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(), "Unable to kill job: %s[%s]" % ( self.job_id, self.array_index ))


    def suspend(self):
        full_job_id = lsblib.create_job_id(job_id=self.job_id, array_index=self.array_index)
        rc = lsblib.lsb_signaljob(full_job_id, lsblib.SIGSTOP)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(),
                                "Unable to suspend job: %s[%s]" % ( self.job_id, self.array_index ))

    def requeue(self, hold=False):
        rq = lsblib.JobRequeue()
        rq.jobId = lsblib.create_job_id(job_id=self.job_id, array_index=self.array_index)
        rq.status = lsblib.JOB_STAT_PEND
        if hold:
            rq.status = lsblib.JOB_STAT_PSUSP

        if self.status.name == u"JOB_STAT_DONE":
            rq.options = lsblib.REQUEUE_DONE
        elif self.status.name == u"JOB_STAT_RUN":
            rq.options = lsblib.REQUEUE_RUN
        elif self.status.name == u"JOB_STAT_EXIT":
            rq.options = lsblib.REQUEUE_EXIT
        else:
            raise ValueError(self.status)

        rc = lsblib.lsb_requeuejob(rq)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(),
                                "Unable to requeue job: %s[%s]" % ( self.job_id, self.array_index ))

    def resume(self):
        full_job_id = lsblib.create_job_id(job_id=self.job_id, array_index=self.array_index)
        rc = lsblib.lsb_signaljob(full_job_id, lsblib.SIGCONT)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(),
                                "Unable to resume job: %s[%s]" % ( self.job_id, self.array_index ))

    def get_output_path(self):
        full_job_id = lsblib.create_job_id(job_id=self.job_id, array_index=self.array_index)
        return lsblib.lsb_peekjob(full_job_id)


    ## Openlava Only
    @property
    def checkpoint_directory(self):
        """Directory to store checkpoint data"""
        self._update_jobinfo()
        return self._checkpoint_directory

    @property
    def checkpoint_period(self):
        """Number of seconds between sending checkpoint signals"""
        self._update_jobinfo()
        return self._checkpoint_period

    @property
    def checkpoint_period_timedelta(self):
        """Timedelta object for checkpointing period"""
        return datetime.timedelta(seconds=self.checkpoint_period)

    @property
    def cpu_factor(self):
        """CPU Factor of execution host"""
        self._update_jobinfo()
        return self._cpu_factor

    @property
    def cwd(self):
        """Current Working Directory of the job"""
        self._update_jobinfo()
        return self._cwd

    @property
    def execution_cwd(self):
        """Current working directory on the execution host"""
        self._update_jobinfo()
        return self._execution_cwd

    @property
    def execution_home_directory(self):
        """Home directory on execution host"""
        self._update_jobinfo()
        return self._execution_home_directory

    @property
    def execution_user_id(self):
        """User ID on execution host"""
        self._update_jobinfo()
        return self._execution_user_id

    @property
    def execution_user_name(self):
        """User name on execution host"""
        self._update_jobinfo()
        return self._execution_user_name

    @property
    def host_specification(self):
        """Host specification"""
        self._update_jobinfo()
        return self._host_specification

    @property
    def login_shell(self):
        """Login shell of the user"""
        self._update_jobinfo()
        return self._login_shell

    @property
    def parent_group(self):
        """Parent job group"""
        self._update_jobinfo()
        return self._parent_group

    @property
    def pre_execution_command(self):
        """User supplied Pre Exec Command"""
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
        """NIOS Port of the job"""
        self._update_jobinfo()
        return self._service_port

    @property
    def submit_home_directory(self):
        """Home directory on the submit host"""
        self._update_jobinfo()
        return self._submit_home_directory

    @property
    def termination_signal(self):
        """Signal to send when job exceeds termination deadline"""
        self._update_jobinfo()
        return self._termination_signal


class Host(HostBase):
    cluster_type = "openlava"

    def open(self):
        rc = lsblib.lsb_hostcontrol(self.name, lsblib.HOST_OPEN)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(), "Unable to open host: %s" % self.name)

    def close(self):
        rc = lsblib.lsb_hostcontrol(self.name, lsblib.HOST_CLOSE)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(), "Unable to close host: %s" % self.name)

    def admins(self):
        return Cluster().admins

    def is_busy(self):
        for s in self.statuses:
            busy = [
                "HOST_STAT_BUSY",
                "HOST_STAT_FULL",
                "HOST_STAT_LOCKED",
                "HOST_STAT_EXCLUSIVE",
                "HOST_STAT_LOCKED_MASTER",
            ]
            if s.name in busy:
                return True
        return False

    def is_down(self):
        for s in self.statuses:
            if s.name in ["HOST_STAT_UNREACH", "HOST_STAT_UNAVAIL", "HOST_STAT_NO_LIM", ]:
                return True
        return False

    def is_closed(self):
        for s in self.statuses:
            if s.name in ["HOST_STAT_WIND", "HOST_STAT_DISABLED", ]:
                return True
        return False

    def json_attributes(self):
        attribs = HostBase.json_attributes(self)
        attribs.extend([
            'cpu_factor',
            'is_server',
            'num_disks',
            'num_user_suspended_jobs',
            'num_user_suspended_slots',
            'num_system_suspended_jobs',
            'num_system_suspended_slots',
            'has_kernel_checkpoint_copy',
            'max_slots_per_user',
            'run_windows',
        ])
        return attribs

    @classmethod
    def get_host_list(cls):
        initialize()
        hs = lsblib.lsb_hostinfo()
        if hs is None:
            raise_cluster_exception(lsblib.get_lsberrno(), "Unable to get list of hosts")
        return [cls(h.host) for h in hs]

    def __init__(self, host_name):
        initialize()
        self._lsb_update_time = 0
        self._update_time = 0
        HostBase.__init__(self, host_name)

        # check host exists
        self._model = lslib.ls_gethostmodel(host_name)
        if self._model == None:
            raise NoSuchHostError("Host: %s does not exist" % host_name)

    def _update_hostinfo(self):
        if (int(time.time()) - self._update_time) < 60:
            return
        self._update_time = int(time.time())
        # cache this....
        hosts = lslib.ls_gethostinfo(resReq="", hostList=[self.host_name], options=0)
        if len(hosts) != 1:
            raise ValueError("Invalid number of hosts returned")
        host = hosts[0]
        self._max_processors = host.maxCpus
        self._max_ram = host.maxMem
        self._max_swap = host.maxSwap
        self._max_tmp = host.maxTmp
        self._num_disks = host.nDisks
        self._is_server = host.isServer
        self._run_windows = host.windows
        resource_names = host.resources
        self._resources = []
        c = Cluster()
        for r in c.resources():
            if r.name in resource_names:
                self._resources.append(r)

    def _update_lsb_hostinfo(self):
        if (int(time.time()) - self._lsb_update_time) < 60:
            return
        self._lsb_update_time = int(time.time())

        hosts = lsblib.lsb_hostinfo(hosts=[self.host_name])
        if hosts == None or len(hosts) != 1:
            raise ValueError("Invalid number of hosts")
        host = hosts[0]
        self._status = host.hStatus
        self._max_slots = host.maxJobs
        self._total_slots = host.numJobs

        self._num_running_slots = host.numRUN
        self._num_suspended_slots = host.numSSUSP + host.numUSUSP
        self._num_user_suspended_slots = host.numUSUSP
        self._num_system_suspended_slots = host.numSSUSP
        self._num_reserved_slots = host.numRESERVE

        self._max_jobs = host.maxJobs
        self._total_jobs = 0
        self._num_running_jobs = 0
        self._num_suspended_jobs = 0
        self._num_user_suspended_jobs = 0
        self._num_system_suspended_jobs = 0
        self._max_slots_per_user = host.userJobLimit

        if (host.attr & lsblib.H_ATTR_CHKPNTABLE) != 0:
            self._has_checkpoint_support = True
        else:
            self._has_checkpoint_support = False

        if (host.attr & lsblib.H_ATTR_CHKPNT_COPY ) != 0:
            self._has_kernel_checkpoint_support = True
        else:
            self._has_kernel_checkpoint_support = False

        self._load = host.load

        self._load_sched = host.loadSched
        for i in range(len(self._load_sched)):
            if self._load_sched[i] == 2147483648.0 or self._load_sched[i] == -2147483648.00:
                self._load_sched[i] = -1

        self._load_stop = host.loadStop
        for i in range(len(self._load_stop)):
            if self._load_stop[i] == 2147483648.0 or self._load_stop[i] == -2147483648.00:
                self._load_stop[i] = -1

        ## iterate through jobs and count/sum each one.
        for j in self.jobs():
            self._total_jobs += 1
            if j.status.name == "JOB_STAT_RUN":
                self._num_running_jobs += 1
            elif j.status.name == "JOB_STAT_SSUSP":
                self._num_suspended_jobs += 1
                self._num_system_suspended_jobs += 1
            elif j.status.name == "JOB_STAT_USUSP":
                self._num_suspended_jobs += 1
                self._num_user_suspended_jobs += 1

    @property
    def has_checkpoint_support(self):
        """True if the host supports checkpointing"""
        self._update_lsb_hostinfo()
        return self._has_checkpoint_support

    @property
    def host_model(self):
        """String containing model information"""
        return self._model

    @property
    def host_type(self):
        """String containing host type information"""
        return lslib.ls_gethosttype(self.name)


    @property
    def resources(self):
        """Array of resources available"""
        self._update_hostinfo()
        return self._resources

    @property
    def max_jobs(self):
        """Returns the maximum number of jobs that may execute on this host"""
        self._update_lsb_hostinfo()
        return self._max_jobs

    @property
    def max_processors(self):
        """Maximum number of processors available on the host"""
        self._update_hostinfo()
        return self._max_processors

    @property
    def max_ram(self):
        """Max Ram"""
        self._update_hostinfo()
        return self._max_ram

    @property
    def max_slots(self):
        """Returns the maximum number of scheduling slots that may be consumed on this host"""
        self._update_lsb_hostinfo()
        return self._max_slots


    @property
    def max_swap(self):
        """Max swap space"""
        self._update_hostinfo()
        return self._max_swap

    @property
    def max_tmp(self):
        """Max tmp space"""
        self._update_hostinfo()
        return self._max_tmp

    @property
    def num_reserved_slots(self):
        """Returns the number of scheduling slots that are reserved"""
        self._update_lsb_hostinfo()
        return self._num_reserved_slots

    @property
    def num_running_jobs(self):
        """Returns the nuber of jobs that are executing on the host"""
        self._update_lsb_hostinfo()
        return self._num_running_jobs

    @property
    def num_running_slots(self):
        """Returns the total number of scheduling slots that are consumed on this host"""
        self._update_lsb_hostinfo()
        return self._num_running_slots

    @property
    def num_suspended_jobs(self):
        """Returns the number of jobs that are suspended on this host"""
        self._update_lsb_hostinfo()
        return self._num_suspended_jobs

    @property
    def num_suspended_slots(self):
        """Returns the number of scheduling slots that are suspended on this host"""
        self._update_lsb_hostinfo()
        return self._num_suspended_jobs

    @property
    def run_windows(self):
        """Run Windows"""
        self._update_lsb_hostinfo()
        return self._run_windows

    @property
    def statuses(self):
        """Array of statuses that apply to the host"""
        self._update_lsb_hostinfo()
        return HostStatus.get_status_list(self._status)

    @property
    def total_jobs(self):
        """Returns the total number of jobs that are running on this host, including suspended jobs."""
        self._update_lsb_hostinfo()
        return self._total_jobs

    @property
    def total_slots(self):
        """Returns the total number of slots that are consumed on this host, including those from  suspended jobs."""
        self._update_lsb_hostinfo()
        return self._total_slots


    #Openlava Only

    @property
    def cpu_factor(self):
        """Openlava Specific - returns the CPU factor of the host"""
        return lslib.ls_gethostfactor(self.name)

    @property
    def is_server(self):
        """True if host is an openlava server (as opposed to submission host)"""
        self._update_hostinfo()
        return self._is_server

    @property
    def num_disks(self):
        """Openlava specific: Returns the number of physical disks installed in the machine"""
        self._update_hostinfo()
        return self._num_disks

    @property
    def num_user_suspended_jobs(self):
        """Returns the number of jobs that have been suspended by the user on this host"""
        self._update_lsb_hostinfo()
        return self._num_user_suspended_jobs

    @property
    def num_user_suspended_slots(self):
        """Returns the number of scheduling slots that have been suspended by the user on this host"""
        self._update_lsb_hostinfo()
        return self._num_user_suspended_slots

    @property
    def num_system_suspended_jobs(self):
        """Returns the number of jobs that have been suspended by the system on this host"""
        self._update_lsb_hostinfo()
        return self._num_system_suspended_jobs

    @property
    def num_system_suspended_slots(self):
        """Returns the number of scheduling slots that have been suspended by the system on this host"""
        self._update_lsb_hostinfo()
        return self._num_system_suspended_slots

    @property
    def has_kernel_checkpoint_copy(self):
        """Returns true if the host supports kernel checkpointing"""
        self._update_lsb_hostinfo()
        return self._has_kernel_checkpoint_support

    @property
    def max_slots_per_user(self):
        """Returns the maximum slots that a user can occupy on the host"""
        self._update_lsb_hostinfo()
        return self._max_slots_per_user


    def jobs(self, job_id=0, job_name="", user="all", queue="", options=0):
        """Return jobs on this host"""
        num_jobs = lsblib.lsb_openjobinfo(job_id=job_id, job_name=job_name, user=user, queue=queue, host=self.host_name,
                                          options=options)
        jobs = []
        if num_jobs < 1:
            return jobs
        jobs = []
        for i in range(num_jobs):
            j = lsblib.lsb_readjobinfo()
            jobs.append(Job(job=j))
        lsblib.lsb_closejobinfo()
        return jobs

    def load_information(self):
        """Return load information on the host"""
        self._update_lsb_hostinfo()

        indexes = {
        'names': ["15s Load", "1m Load", "15m Load", "Avg CPU Utilization", "Paging Rate (Pages/Sec)",
                  "Disk IO Rate (MB/Sec)", "Num Users", "Idle Time", "Tmp Space (MB)", "Free Swap (MB)",
                  "Free Memory (MB)"],
        'short_names': ['r15s', 'r1m', 'r15m', 'ut', 'pg', 'io', 'ls', 'it', 'tmp', 'swp', 'mem'],
        'values': []
        }

        indexes['values'].append({
        'name': "Actual Load",
        'values': self._load
        })

        indexes['values'].append({
        'name': "Stop Dispatching Load",
        'values': self._load_sched
        })

        indexes['values'].append({
        'name': "Stop Executing Load",
        'values': self._load_stop
        })

        return indexes


class Resource(BaseResource):
    def __init__(self, res):
        if isinstance(res, lslib.ResItem):
            self._name = res.name
            self._description = res.des
            self._type = res.valueType
            self._order = res.orderType
            self._interval = res.interval
            self._flags = res.flags

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
        return ['name', 'description', 'type', 'order', 'interval', 'flags']


class ExecutionHost(Host):
    def __init__(self, host_name, num_slots=1):
        Host.__init__(self, host_name)
        self.num_slots = num_slots

    def json_attributes(self):
        attribs = Host.json_attributes(self)
        attribs.append('num_slots')
        return attribs


class QueueStatus(NumericStatus):
    states = {
    0x01: {
    'friendly': "Open",
    'name': 'QUEUE_STAT_OPEN',
    'description': 'The queue is open to accept newly submitted jobs.',
    },
    0x02: {
    'friendly': "Active",
    'name': 'QUEUE_STAT_ACTIVE',
    'description': 'The queue is actively dispatching jobs. The queue can be inactivated and reactivated by the LSF administrator using lsb_queuecontrol. The queue will also be inactivated when its run or dispatch window is closed. In this case it cannot be reactivated manually; it will be reactivated by the LSF system when its run and dispatch windows reopen.',
    },
    0x04: {
    'friendly': 'Run windows open',
    'name': 'QUEUE_STAT_RUN',
    'description': 'The queue run and dispatch windows are open. The initial state of a queue at LSF boot time is open and either active or inactive, depending on its run and dispatch windows.',
    },
    0x08: {
    'friendly': 'No Pemission',
    'name': 'QUEUE_STAT_NOPERM',
    'description': 'Remote queue rejecting jobs.',
    },
    0x10: {
    'friendly': 'Remote Disconnected',
    'name': 'QUEUE_STAT_DISC',
    'description': 'Remote queue status is disconnected.',
    },
    0x20: {
    'friendly': 'Runwindow Closed',
    'name': 'QUEUE_STAT_RUNWIN_CLOSE',
    'description': 'Queue run windows are closed.',
    },
    }


class QueueAttribute(NumericStatus):
    states = {
    0x01: {
    'friendly': "Exclusive",
    'name': 'Q_ATTRIB_EXCLUSIVE',
    'description': "This queue accepts jobs which request exclusive execution. ",
    },
    0x02: {
    'friendly': "Default Queue",
    'name': 'Q_ATTRIB_DEFAULT',
    'description': "This queue is a default LSF queue. ",
    },
    0x04: {
    'friendly': "Round Robin Scheduling Policy",
    'name': 'Q_ATTRIB_FAIRSHARE',
    'description': "This queue uses the Round Robin scheduling policy.",
    },
    0x80: {
    'friendly': 'Backfill Enabled',
    'name': 'Q_ATTRIB_BACKFILL',
    'description': "This queue uses a backfilling policy. ",
    },
    0x100: {
    'friendly': "Preference Scheduling Policy",
    'name': 'Q_ATTRIB_HOST_PREFER',
    'description': "This queue uses a host preference policy. ",
    },
    0x800: {
    'friendly': "Non-Interactive only",
    'name': 'Q_ATTRIB_NO_INTERACTIVE',
    'description': "This queue does not accept batch interactive jobs. ",
    },
    0x1000: {
    'friendly': "Interactive Only",
    'name': 'Q_ATTRIB_ONLY_INTERACTIVE',
    'description': "This queue only accepts batch interactive jobs. ",
    },
    0x2000: {
    'friendly': "No host type resources",
    'name': 'Q_ATTRIB_NO_HOST_TYPE',
    'description': "No host type related resource name specified in resource requirement. ",
    },
    0x4000: {
    'friendly': "Ignores deadlines",
    'name': 'Q_ATTRIB_IGNORE_DEADLINE',
    'description': "This queue disables deadline constrained resource scheduling. ",
    },
    0x8000: {
    'friendly': "Checkpointing supported",
    'name': 'Q_ATTRIB_CHKPNT',
    'description': "Jobs may run as chkpntable. ",
    },
    0x10000: {
    'friendly': "Re-Runnable",
    'name': 'Q_ATTRIB_RERUNNABLE',
    'description': "Jobs may run as rerunnable. ",
    },
    0x80000: {
    'friendly': "Interactive First",
    'name': 'Q_ATTRIB_ENQUE_INTERACTIVE_AHEAD',
    'description': "Push interactive jobs in front of other jobs in queue. ",
    },
    }


class Queue:
    cluster_type = "openlava"

    @classmethod
    def get_queue_list(cls):
        initialize()
        qs = lsblib.lsb_queueinfo()
        if qs is None:
            raise_cluster_exception(lsblib.get_lsberrno(), "Unable to get list of queues")
        return [cls(q) for q in qs]

    def __init__(self, queue):
        initialize()
        if isinstance(queue, str) or isinstance(queue, unicode):
            queue = lsblib.lsb_queueinfo(queues=[queue])
            if queue == None or len(queue) != 1:
                raise_cluster_exception(lsblib.get_lsberrno(), "Unable to get load queue: %s" % queue)
            queue = queue[0]
        if not isinstance(queue, lsblib.QueueInfoEnt):
            raise ValueError("invalid Queue, must be string or QueueInfoEnt")
        self.name = queue.queue
        self.description = queue.description
        self.priority = queue.priority
        self.nice = queue.nice
        self._allowed_users = queue.userList
        self._allowed_hosts = queue.hostList
        self.max_jobs_per_user = queue.userJobLimit
        self.max_slots_per_user = queue.userJobLimit
        self.max_jobs_per_processor = queue.procJobLimit
        self.max_slots_per_processor = queue.procJobLimit
        self.run_windows = queue.windows
        names = ["CPU Time", "File Size", "Data Segment Size", "Stack Size", "Core Size", "RSS Size", "Num Files",
                 "Max Open Files", "Swap Limit", "Run Limit", "Process Limit"]
        units = [None, "KB", "KB", "KB", "KB", "KB", None, None, "KB", None, None]
        self.runtime_limits = []
        rlims = queue.rLimits
        for i in range(len(rlims)):
            self.runtime_limits.append(
                ResourceLimit(
                    name=names[i],
                    soft_limit=rlims[i],
                    hard_limit=rlims[i],
                    unit=units[i]
                )
            )
        self.host_specification = queue.defaultHostSpec.lstrip()
        self.attributes = QueueAttribute.get_status_list(queue.qAttrib)
        self.statuses = QueueStatus.get_status_list(queue.qStatus)
        self.max_slots = queue.maxJobs
        self.total_slots = queue.numJobs
        self.num_running_slots = queue.numRUN
        self.num_pending_slots = queue.numPEND
        self.num_suspended_slots = queue.numSSUSP + queue.numUSUSP
        self.num_user_suspended_slots = queue.numUSUSP
        self.num_system_suspended_slots = queue.numSSUSP
        self.num_reserved_slots = queue.numRESERVE
        self.max_jobs = queue.maxJobs
        self.total_jobs = 0
        self.num_running_jobs = 0
        self.num_pending_jobs = 0
        self.num_suspended_jobs = 0
        self.num_user_suspended_jobs = 0
        self.num_system_suspended_jobs = 0
        ## iterate through jobs and count/sum each one.
        for j in self.jobs():
            self.total_jobs += 1
            if j.status.name == "JOB_STAT_RUN":
                self.num_running_jobs += 1
            elif j.status.name == "JOB_STAT_SSUSP":
                self.num_suspended_jobs += 1
                self.num_system_suspended_jobs += 1
            elif j.status.name == "JOB_STAT_USUSP":
                self.num_suspended_jobs += 1
                self.num_user_suspended_jobs += 1
            elif j.status.name == "JOB_STAT_PEND":
                self.num_pending_jobs += 1
        self.pre_execution_command = queue.preCmd.lstrip()
        self.post_execution_command = queue.postCmd.lstrip()
        self.pre_post_user_name = queue.prepostUsername.lstrip()
        self.admins = queue.admins.split() + Cluster().admins
        self.migration_threshold = queue.mig
        self.migration_threshold_timedelta = datetime.timedelta(minutes=queue.mig)
        self.scheduling_delay = queue.schedDelay
        self.scheduling_delay_timedelta = datetime.timedelta(minutes=queue.schedDelay)
        self.accept_interval = queue.acceptIntvl
        self.accept_interval_timedelta = datetime.timedelta(seconds=queue.acceptIntvl)
        self.dispatch_windows = queue.windowsD.lstrip()
        self.max_slots_per_job = queue.procLimit
        self.requeue_exit_values = queue.requeueEValues.split()
        self.max_jobs_per_host = queue.hostJobLimit
        self.max_slots_per_host = queue.hostJobLimit
        self.resource_requirements = queue.resReq.lstrip()
        self.slot_hold_time = queue.slotHoldTime
        self.slot_hold_time_timedelta = datetime.timedelta(seconds=queue.slotHoldTime)
        self.stop_condition = queue.stopCond.lstrip()
        self.job_starter_command = queue.jobStarter.lstrip()
        self.suspend_action_command = queue.suspendActCmd.lstrip()
        self.resume_action_command = queue.resumeActCmd.lstrip()
        self.terminate_action_command = queue.terminateActCmd.lstrip()
        self.min_slots_per_job = queue.minProcLimit
        self.default_slots_per_job = queue.defProcLimit
        self.checkpoint_data_directory = queue.chkpntDir.lstrip()
        self.checkpoint_period = queue.chkpntPeriod
        self.checkpoint_period_timedelta = datetime.timedelta(minutes=queue.chkpntPeriod)
        self.resume_condition = queue.resumeCond.lstrip()
        self.stop_condition = queue.stopCond.lstrip()

    def is_accepting_jobs(self):
        for state in self.statuses:
            if state.name == "QUEUE_STAT_OPEN":
                return True
        return False

    def is_despatching_jobs(self):
        for state in self.statuses:
            if state.name == "QUEUE_STAT_ACTIVE":
                return True
        return False

    def close(self):
        rc = lsblib.lsb_queuecontrol(self.name, lsblib.QUEUE_CLOSED)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(), "Unable to close queue: %s" % self.name)

    def open(self):
        rc = lsblib.lsb_queuecontrol(self.name, lsblib.QUEUE_OPEN)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(), "Unable to open queue: %s" % self.name)

    def inactivate(self):
        rc = lsblib.lsb_queuecontrol(self.name, lsblib.QUEUE_INACTIVATE)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(), "Unable to inactivate queue: %s" % self.name)

    def activate(self):
        rc = lsblib.lsb_queuecontrol(self.name, lsblib.QUEUE_ACTIVATE)
        if rc == 0:
            return rc
        raise_cluster_exception(lsblib.get_lsberrno(), "Unable to activate queue: %s" % self.name)

    def allowed_hosts(self, ):
        pass

    def allowed_users(self):
        pass

    def jobs(self):
        return Job.get_job_list(queue_name=self.name)

    def json_attributes(self):
        return [
            'name',
            'description',
            'priority',
            'nice',
            'allowed_users',
            'allowed_hosts',
            'max_jobs_per_user',
            'max_slots_per_user',
            'max_jobs_per_processor',
            'max_slots_per_processor',
            'run_windows',
            'runtime_limits',
            'host_specification',
            'attributes',
            'statuses',
            'max_slots',
            'total_slots',
            'num_running_slots',
            'num_pending_slots',
            'num_suspended_slots',
            'num_user_suspended_slots',
            'num_system_suspended_slots',
            'num_reserved_slots',
            'max_jobs',
            'total_jobs',
            'num_running_jobs',
            'num_pending_jobs',
            'num_suspended_jobs',
            'num_user_suspended_jobs',
            'num_system_suspended_jobs',
            'pre_execution_command',
            'post_execution_command',
            'pre_post_user_name',
            'admins',
            'migration_threshold',
            'scheduling_delay',
            'accept_interval',
            'dispatch_windows',
            'max_slots_per_job',
            'requeue_exit_values',
            'max_jobs_per_host',
            'max_slots_per_host',
            'resource_requirements',
            'slot_hold_time',
            'stop_condition',
            'job_starter_command',
            'suspend_action_command',
            'resume_action_command',
            'terminate_action_command',
            'min_slots_per_job',
            'default_slots_per_job',
            'checkpoint_data_directory',
            'checkpoint_period',
            'resume_condition',
            'stop_condition',
            'is_accepting_jobs',
            'is_despatching_jobs',
            'jobs',
            'cluster_type',
        ]


class User(UserBase):
    cluster_type = "openlava"

    def __init__(self, user):
        initialize()
        if isinstance(user, str) or isinstance(user, unicode):
            user = lsblib.lsb_userinfo(user_list=[user], numusers=1)
            if user == None:
                raise_cluster_exception(lsblib.get_lsberrno(),
                                        "Unable load user: %s[%s]" % ( self.job_id, self.array_index ))
            if len(user) != 1:
                raise ValueError("Invalid User")
            user = user[0]
        if not isinstance(user, lsblib.UserInfoEnt):
            raise ValueError("Invalid User Object")

        self.name = user.user
        self.max_jobs_per_processor = user.procJobLimit
        self.max_slots = user.maxJobs
        self.total_slots = user.numJobs
        self.num_running_slots = user.numRUN
        self.num_pending_slots = user.numPEND
        self.num_suspended_slots = user.numSSUSP + user.numUSUSP
        self.num_user_suspended_slots = user.numUSUSP
        self.num_system_suspended_slots = user.numSSUSP
        self.num_reserved_slots = user.numRESERVE
        self.max_jobs = user.maxJobs
        self.total_jobs = 0
        self.num_running_jobs = 0
        self.num_pending_jobs = 0
        self.num_suspended_jobs = 0
        self.num_user_suspended_jobs = 0
        self.num_system_suspended_jobs = 0
        ## iterate through jobs and count/sum each one.
        for j in self.jobs():
            self.total_jobs += 1
            if j.status.name == "JOB_STAT_RUN":
                self.num_running_jobs += 1
            elif j.status.name == "JOB_STAT_SSUSP":
                self.num_suspended_jobs += 1
                self.num_system_suspended_jobs += 1
            elif j.status.name == "JOB_STAT_USUSP":
                self.num_suspended_jobs += 1
                self.num_user_suspended_jobs += 1
            elif j.status.name == "JOB_STAT_PEND":
                self.num_pending_jobs += 1

    def jobs(self, job_id=0, job_name="", queue="", host="", options=0):
        """Return jobs on this host"""
        num_jobs = lsblib.lsb_openjobinfo(job_id=job_id, job_name=job_name, user=self.name, queue=queue, host=host,
                                          options=options)
        jobs = []
        if num_jobs < 1:
            return jobs
        for i in range(num_jobs):
            j = lsblib.lsb_readjobinfo()
            jobs.append(Job(job=j))
        lsblib.lsb_closejobinfo()
        return jobs

    def json_attributes(self):
        return UserBase.json_attributes(self) + [
            'num_user_suspended_jobs',
            'num_system_suspended_jobs',
            'num_user_suspended_slots',
            'num_system_suspended_slots',
        ]

    @classmethod
    def get_user_list(cls):
        initialize()
        us=lsblib.lsb_userinfo()
        if us is None:
            raise_cluster_exception(lsblib.get_lsberrno(), "Unable to get list of users")

        return [cls(u) for u in us]
