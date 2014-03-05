Command Line Tools
==================

The following command line tools have been created based on the syntax of the openlava command line utilities to demonstrate how to perform tasks using the API.

badmin.py
---------

.. program:: badmin.py

Provides similar functionality and syntax to the OpenLava badmin command.  Queue and host maintenance.

This is not meant to be a like for like replacement for badmin, but an example of how to use the API.

.. option:: hopen [host_name ... | host_group ... | all]

Opens  batch server hosts. Specify the names of any server hosts or host groups (see bmgroup(1)). All batch server hosts will be opened if the reserved word all is specified. If no host or host group is specified, the local host is assumed. A host accepts batch jobs if it is open.

.. option:: hclose [host_name ... | host_group ... | all]

Closes batch server hosts. Specify the names of any server hosts or host groups (see bmgroup(1)). All batch server hosts will be closed if the reserved word all is specified. If no argument is specified, the local host is assumed. A closed host will not accept any new job, but jobs already dispatched to the host will not be affected. Note that this is different from a host closed by a window - all jobs on it are suspended in that case.

.. option:: qopen [queue_name ... | all]

Opens specified queues, or all queues if the reserved word all is  specified

.. option:: qclose [queue_name ... | all]

Closes  specified  queues,  or all queues if the reserved word all is specified. If no queue is specified, the system default queue is assumed.

.. option:: qact [queue_name ... | all]

Activates specified queues, or all queues if the reserved word all is specified.

.. option:: qinact [queue_name ... | all]

Inactivates  specified queues, or all queues if the reserved word all is specified.

bhosts.py
---------

.. program:: bhosts.py

Provides similar functionality and syntax to the OpenLava bhosts command.  Displays hosts and their static and dynamic resource.

This is not meant to be a like for like replacement for bhosts, but an example of how to use the API.

By default, returns the following information about all hosts: host name, host status, job slot limits, and job state statistics.

.. option:: -w

Displays host information in wide format. Fields are displayed without truncation.

.. option:: -l

Displays host information in a (long) multi-line format. In addition to the default fields, displays information about the CPU factor, the dispatch windows, the current load, and the load thresholds.

.. option:: host_name ... | host_group ...

Only  displays information about the specified hosts or host groups. For host groups, the names of the hosts belonging to the group are displayed instead of the name of the host group. Do not use quotes when specifying multiple hosts or host groups.


bjobs.py
--------

.. program:: bjobs.py

Provides similar functionality and syntax to the OpenLava bjobs command.  Displays information about jobs.  By default, displays information about your own pending, running and suspended jobs.

This is not meant to be a like for like replacement for bjobs, but an example of how to use the API.

.. option:: -a

Displays  information  about  jobs in all states, including finished jobs that finished recently, within an interval specified by CLEAN_PERIOD in lsb.params (the default period is 1 hour).

.. option:: -d

Displays information about jobs that finished recently, within an interval specified by CLEAN_PERIOD in lsb.params (the default period is 1 hour).

.. option:: -p

Displays  pending  jobs, together with the pending reasons that caused each job not to be dispatched during the last dispatch turn. The pending reason shows the number of hosts for that reason, or names the hosts if -l is also specified.

Each pending reason is associated with one or more hosts and it states the cause why these hosts are not allocated to run the job.  In situations where the job  requests  specific hosts (using bsub -m), users may see reasons for unrelated hosts also being displayed, together with the reasons associated with the requested hosts. The life cycle of a pending reason ends after a new dispatch turn starts. The reason may not reflect the current load situation because  it could last as long as the interval specified by MBD_SLEEP_TIME in lsb.params.

When the job slot limit is reached for a job array (bsub -J "jobArray[indexList]%job_slot_limit") the following message is displayed:

The job array has reached its job slot limit.

.. option:: -r

Displays running jobs.

.. option:: -s

Displays suspended jobs, together with the suspending reason that caused each job to become suspended.

The  suspending  reason  may not remain the same while the job stays suspended. For example, a job may have been suspended due to the paging rate, but after the paging rate dropped another load index could prevent the job from being resumed. The suspending reason will be updated according to the load index.  The reasons could be as old as the time interval specified by SBD_SLEEP_TIME in lsb.params. So the reasons shown may not reflect the current load situation.

.. option:: -l

Long format. Displays detailed information for each job in a multi-line format.

The  -l  option displays the following additional information: project name, job command, current working directory on the submission host, pending and sus‐pending reasons, job status, resource usage, resource limits information.

.. option:: -u user_name | -u user_group | -u all

Only displays jobs that have been submitted by the specified users. The keyword all specifies all users.

.. option:: job_ID

Displays information about the specified jobs or job arrays.

.. option:: -m

Only displays jobs dispatched to the specified hosts.

.. option:: -q queue_name

Only displays jobs in the specified queue.

The command bqueues.py returns a list of queues configured in the system, and information about the configurations of these queues.

.. option:: -J job_name

Displays information about the specified jobs or job arrays.

bkill.py
--------

.. program:: bkill.py

Provides similar functionality and syntax to the OpenLava bkill command.  Sends signals to kill, suspend, or resume unfinished jobs.

This is not meant to be a like for like replacement for bkill, but an example of how to use the API.

.. option:: -J job_name

Operates only on jobs with the specified job_name. The -J option is ignored if a job ID other than 0 is specified in the job_ID option.

.. option:: -m host_name | -m host_group

Operates only on jobs dispatched to the specified host or host group.

.. option:: -q queue_name

Operates only on jobs in the specified queue.

.. option:: -u user_name | -u user_group | -u all

Operates only on jobs submitted by the specified user or user group (see bugroup(1)), or by all users if the reserved user name all is specified.

.. option::  job_ID ... | 0 | "job_ID[index]" ...

Operates only on jobs that are specified by job_ID or "job_ID[index]", where "job_ID[index]" specifies selected job array elements (see bjobs(1)). For job arrays, quotation marks must enclose the job ID and index, and index must be enclosed in square brackets.

Jobs submitted by any user can be specified here without using the -u option. If you use the reserved job ID 0, all the  jobs  that  satisfy  other  options (that is, -m, -q, -u and -J) are operated on; all other job IDs are ignored.

The  options  -u,  -q,  -m and -J have no effect if a job ID other than 0 is specified. Job IDs are returned at job submission time (see bsub(1)) and may be obtained with the bjobs command (see bjobs(1)).

bqueues.py
----------

.. program:: bqueues.py

Provides similar functionality and syntax to the OpenLava bqueues command.  Displays information about queues.

This is not meant to be a like for like replacement for bqueues, but an example of how to use the API.

.. option:: -w

Displays queue information in a wide format. Fields are displayed without truncation.

.. option:: -l

Displays  queue  information in a long multi-line format. The -l option displays the following additional information: queue description, queue characteristics and statistics, scheduling parameters, resource limits, scheduling policies, users, hosts, user shares, windows, associated commands, and job controls.

.. option:: -m host_name | -m host_group | -m all

Displays the queues that can run jobs on the specified host or host group. If the keyword all is specified, displays the queues that can  run  jobs  on  all hosts . For a list of host groups see bmgroup(1).

.. option:: -u user_name | -u user_group | -u all

Displays  the  queues  that can accept jobs from the specified user or user group (For a list of user groups see bugroup(1).) If the keyword all is specified, displays the queues that can accept jobs from all users.

.. option:: queue_name ...

Displays information about the specified queues...

bsub.py
-------

program:: bsub.py

Provides similar functionality and syntax to the OpenLava bsub command.  Submits a batch job using the API.

This is not meant to be a like for like replacement for bsub, but an example of how to use the API.

Submits a job for batch execution and assigns it a unique numerical job ID.

Runs  the  job on a host that satisfies all requirements of the job, when all conditions on the job, host, queue, and cluster are satisfied.  If the scheduler cannot run all jobs immediately, scheduling policies determine the order of dispatch. Jobs are started and suspended according to the current system load.

Sets the user's execution environment for the job, including the current working directory, file creation mask, and all environment variables,  and  sets scheduling system environment variables before starting the job.

.. option:: -B

Sends mail to you when the job is dispatched and begins execution.

.. option:: -H

Holds the job in the PSUSP state when the job is submitted. The job will not be scheduled until you tell the system to resume the job.

.. option:: -N

Sends the job report to you by mail when the job finishes. When used without any other options, behaves the same as the default.

.. option:: -r

If  the  execution host becomes unavailable while a job is running, specifies that the job will rerun on another host. openlava requeues the job in the same job queue with the same job ID. When an available execution host is found, reruns the job as if it were submitted new. You receive a mail message  informing you of the host failure and requeuing of the job.

If the system goes down while a job is running, specifies that the job will be requeued when the system restarts.

Reruns a job if the execution host or the system fails; it does not rerun a job if the job itself fails.

.. option:: -x

Puts the host running your job into exclusive execution mode.

In  exclusive  execution mode, your job runs by itself on a host. It is dispatched only to a host with no other jobs running, and openlava does not send any other jobs to the host until the job completes.

To submit a job in exclusive execution mode, the queue must be configured to allow exclusive jobs.

.. option:: -n min_proc[,max_proc]

Submits a parallel job and specifies the minimum and maximum numbers of processors required to run the job (some of the processors may be on the same multi‐processor host). If you do not specify a maximum, the number you specify represents the exact number of processors to use.

.. option:: -J "job_name[index_list]%job_slot_limit"

Assigns the specified name to the job, and, for job arrays, specifies the indices of the job array and optionally the maximum number of jobs that can run at any given time.

The job name need not be unique.

To specify a job array, enclose the index list in square brackets, as shown, and enclose the entire job array specification in quotation  marks,  as  shown.  The  index  list is a comma-separated list whose elements have the syntax start[-end[:step]] where start, end and step are positive integers. If the step is omitted, a step of one is assumed. The job array index starts at one. By default, the maximum job array index is 2.00.

You may also use a positive integer to specify the system-wide job slot limit (the maximum number of jobs that can run at  any  given  time)  for  this  job array.

All jobs in the array share the same job ID and parameters. Each element of the array is distinguished by its array index.

.. option:: command [argument]

The  job  can  be specified by a command line argument command, or through the standard input if the command is not present on the command line. The command can be anything that is provided to a UNIX Bourne shell (see sh(1)). command is assumed to begin with the first word that is not part of a bsub option.  All arguments that follow command are provided as the arguments to the command.

If  the  batch  job  is not given on the command line, bsub reads the job commands from standard input. If the standard input is a controlling terminal, the user is prompted with "bsub>" for the commands of the job. The input is terminated by entering CTRL-D on a  new  line.  You  can  submit  multiple  commands through standard input. The commands are executed in the order in which they are given. bsub options can also be specified in the standard input if the line begins with #BSUB; e.g., "#BSUB -x". If an option is given on both the bsub command line, and in the standard input, the command line option  overrides  the option  in the standard input. The user can specify the shell to run the commands by specifying the shell path name in the first line of the standard input, such as "#!/bin/csh". If the shell is not given in the first line, the Bourne shell is used. The standard input facility can be used to spool a  user's  job script; such as "bsub < script". See EXAMPLES below for examples of specifying commands through standard input.

