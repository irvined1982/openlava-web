Javascript API
==============

The Javascript API defines the standard API used to interface with a remote openlava web server. This is
designed to be independent of the scheduling environment, regardless of the underlying scheduling system
being used by openlava-web the returned data will be in a standard format, and have a consistent API.

The Javascript API generally mirrors that of the cluster API where possible.  As such programming one is
almost identical to programming the other.

.. contents::

Configuration
-------------

.. js:function:: olwclient.serverUrl(newUrl)

    URL to the Openlava Web Server

    :param string newUrl:

        Set the serverUrl to this url if specified, if unspecified the serverUrl is left unchanged.

    :returns: URL of server
    :rtype: string

Authentication
--------------

.. js:function:: olwclient.login(username, password, callback, errback)

    Authenticate using the provided credentials and obtain the session cookie and csrf token.

    :param string username:

        The username to use when authenticating to the openlava web server.

    :param string password:

        The password to use when authenticating to the openlava web server.

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.


Status Classes
--------------

Status Classes define statuses, which all have a standard behavior.  This may be for a host, job, queue, or
any other object that has one or more statuses.

.. js:attribute:: olwclient.status.description

        Description of the status

.. js:attribute:: olwclient.status.friendly

        Friendly name for the status

.. js:attribute:: olwclient.status.name

        Full name of the status

.. js:attribute:: olwclient.status.status

        Numeric code of the status

Cluster Resources
^^^^^^^^^^^^^^^^^

Cluster Resource classes define resources that are available on the cluster for consumption by jobs.

Resource Limit Classes
^^^^^^^^^^^^^^^^^^^^^^

Resource limits classes define resource limits that are imposed on a given job.

Consumed Resources
^^^^^^^^^^^^^^^^^^

Consumed resources represent resources that have been consumed by a given job.

Queue Classes
-------------

Queue classes represent individual queues that are configured as part of the cluster.

.. js:attribute:: olwclient.Queue.getQueue(queueName, callback, errback)

    Get a Queue object.

    :param string queueName:

        The name of the queue to get

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.Queue.getQueueList(callback, errback)

    Get all queues configured on the cluster.

    :param function callback:

        A function that will be called when the task is successfully completed. Single argument
        containing an array of queue objects.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.Queue.prototype.jobs(callback, errback, filters)

    Returns a list of jobs that match the specified criteria.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

    :param int filters.job_id:

        The numeric Job ID, if this is specified, then queue_name, host_name, user_name, and job_state are
        ignored.

    :param int filters.array_index:

        The array index of the job.  If array_index is -1, then all array tasks from the corresponding job ID are
        returned.  If array_index is not zero, then a job_id must also be specified.

    :param String filters.host_name:

        The name of the host.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are executing on the specified host.

    :param String filters.user_name:

        The name of the user.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are owned by the specified user.

    :param String filters.job_state:

        Only return jobs in this state, state can be "ACT" - all active jobs, "ALL" - All jobs, including finished
        jobs, "EXIT" - Jobs that have exited due to an error or have been killed by the user or an administator,
        "PEND" - Jobs that are in a pending state, "RUN" - Jobs that are currently running, "SUSP" Jobs that are
        currently suspended.

    :param String filters.job_name:

        Only return jobs that are named job_name.

.. js:attribute:: olwclient.Queue.prototype.close(callback, errback)

    Close the queue, the queue will no longer accept new jobs.'

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.Queue.prototype.open(callback, errback)

    Open the queue, the queue will accept new jobs.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.Queue.prototype.activate(callback, errback)

    Activate the queue, jobs will be dispatched.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.Queue.prototype.inactivate(callback, errback)

    Inactivate the queue, no more jobs will be dispatched.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

User Classes
------------

User classes represent individual users that are configured in the cluster.

.. js:attribute:: olwclient.User.Prototype.user_url

    The URL to the full user object

.. js:attribute:: olwclient.User.Prototype.job.url

    The URL to the full URL for the job

.. js:attribute:: olwclient.User.prototype.jobs(callback, errback, filters)

    Returns a list of jobs that the user owns on the cluster.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

    :param int filters.job_id:

        The numeric Job ID, if this is specified, then queue_name, host_name, user_name, and job_state are
        ignored.

    :param int filters.array_index:

        The array index of the job.  If array_index is -1, then all array tasks from the corresponding job ID are
        returned.  If array_index is not zero, then a job_id must also be specified.

    :param String filters.queue_name:

        The name of the queue.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are submitted into the named queue.

    :param String filters.host_name:

        The name of the host.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are executing on the specified host.

    :param String filters.job_state:

        Only return jobs in this state, state can be "ACT" - all active jobs, "ALL" - All jobs, including finished
        jobs, "EXIT" - Jobs that have exited due to an error or have been killed by the user or an administator,
        "PEND" - Jobs that are in a pending state, "RUN" - Jobs that are currently running, "SUSP" Jobs that are
        currently suspended.

    :param String filters.job_name:

        Only return jobs that are named job_name.

.. js:attribute:: olwclient.User.getUser(userName, callback, errback)

    :param string userName: The name of the user to retrieve.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.User.getUserList(callback, errback)

    Get a list of all users on the cluster.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.


Job Classes
-----------

Olwclient uses the RESTful interface to the olweb server to communicate with the scheduler.  Openlava-web is then
responsible for connecting to the job scheduler and retrieving job information.  This is then serialized using JSON
and sent back to the client.

.. js:function:: olwclient.Job.prototype.submit_time_datetime()

    .. note::

        Warning! Unlike ::py:attr:`olwclient.Job.reservation_time_datetime` returns a Date
        object in locale time, and not UTC.

.. js:function:: olwclient.Job.prototype.end_time_datetime()

    .. note::

        Warning! Unlike ::py:attr:`olwclient.Job.reservation_time_datetime` returns a Date
        object in locale time, and not UTC.

.. js:function:: olwclient.Job.prototype.start_time_datetime()

    .. note::

        Warning! Unlike ::py:attr:`olwclient.Job.reservation_time_datetime` returns a Date
        object in locale time, and not UTC.

.. js:function:: olwclient.Job.prototype.predicted_start_time_datetime()

    .. note::

        Warning! Unlike ::py:attr:`olwclient.Job.reservation_time_datetime` returns a Date
        object in locale time, and not UTC.

.. js:function:: olwclient.Job.prototype.reservation_time_datetime()

    .. note::

        Warning! Unlike ::py:attr:`olwclient.Job.reservation_time_datetime` returns a Date
        object in locale time, and not UTC.

.. js:attribute:: olwclient.Job.prototype.execution_hosts

.. js:attribute:: olwclient.Job.prototype.submission_host

.. js:function:: olwclient.Job.prototype.kill()

        Kills the job.  The user must be a job owner, queue or cluster administrator for this operation to succeed.

.. js:function:: olwclient.Job.prototype.requeue(hold)

        Requeues the job.  The user must be a job owner,  queue or cluster administrator for this operation to succeed.

        :param bool hold:

            When true, jobs will be held in the suspended pending state.

            .. note::

                Openlava Only! This property is specific to Openlava and is not generic to all cluster interfaces.

.. js:function:: olwclient.Job.prototype.suspend()

    Suspends the job.  The user must be a job owner, queue or cluster administrator for this operation to succeed.

.. js:function:: olwclient.Job.prototype.resume()

    Resumes the job.  The user must be a job owner, queue or cluster administrator for this operation to succeed.

.. js:function:: olwclient.executeCommand(subUrl, callback, errback)

    :param String subUrl: sub url to open.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.Job.getJob(job_id, array_index, callback, errback)

    Get a single job.

    :param job_id: Numeric Job ID.

    :param array_index: Array index of the job.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.Job.getJobList(callback, errback, filters)

    Returns a list of jobs that match the specified criteria.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

    :param int filters.job_id:

        The numeric Job ID, if this is specified, then queue_name, host_name, user_name, and job_state are
        ignored.

    :param int filters.array_index:

        The array index of the job.  If array_index is -1, then all array tasks from the corresponding job ID are
        returned.  If array_index is not zero, then a job_id must also be specified.

    :param String filters.queue_name:

        The name of the queue.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are submitted into the named queue.

    :param String filters.host_name:

        The name of the host.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are executing on the specified host.

    :param String filters.user_name:

        The name of the user.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are owned by the specified user.

    :param String filters.job_state:

        Only return jobs in this state, state can be "ACT" - all active jobs, "ALL" - All jobs, including finished
        jobs, "EXIT" - Jobs that have exited due to an error or have been killed by the user or an administator,
        "PEND" - Jobs that are in a pending state, "RUN" - Jobs that are currently running, "SUSP" Jobs that are
        currently suspended.

    :param String filters.job_name:
        Only return jobs that are named job_name.

Host Classes
------------

Host classes are used to get information about and manipulate hosts on the cluster.  Primarily this is done through the
Host() class, however when associated with a Job() they may be through ExecutionHost classes which also contain
information on the number of slots that are allocated to the job.

.. js:class:: olwclient.Host.getHost(hostname, callback, errback, data)

    :param string hostname:

        Hostname of host

    :param callback callback:

        A callback to execute on success, single host arg.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.Host.prototype.jobs(callback, errback, filters)

    Get all jobs that are running on the host.

    :param callback callback:

        A callback to execute on success, single jobs arg.  See ::js:func:`olwclient.Job.getJobList`.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

    :param int filters.job_id:

        The numeric Job ID, if this is specified, then queue_name, host_name, user_name, and job_state are
        ignored.

    :param int filters.array_index:

        The array index of the job.  If array_index is -1, then all array tasks from the corresponding job ID are
        returned.  If array_index is not zero, then a job_id must also be specified.

    :param String filters.queue_name:

        The name of the queue.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are submitted into the named queue.

    :param String filters.user_name:

        The name of the user.  If specified, implies that job_id and array_index are set to default.  Only returns
        jobs that are owned by the specified user.

    :param String filters.job_state:

        Only return jobs in this state, state can be "ACT" - all active jobs, "ALL" - All jobs, including finished
        jobs, "EXIT" - Jobs that have exited due to an error or have been killed by the user or an administator,
        "PEND" - Jobs that are in a pending state, "RUN" - Jobs that are currently running, "SUSP" Jobs that are
        currently suspended.

    :param String filters.job_name:
        Only return jobs that are named job_name.

.. js:function:: olwclient.Host.getHostList(callback, errback)

    Get a list of all hosts that are part of the cluster.

    :param callback callback:

        A callback to execute on success, single hosts arg.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.Host.prototype.close(callback, errback)

    Close the host, no new jobs will be dispatched.

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.


.. js:function:: olwclient.Host.prototype.open(callback, errback)

    Open the host to accept new jobs.

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

Convenience Functions
---------------------

The following functions are available to reduce the need to load the object form the server when
it is only required to perform an action. (Such as job kill, etc.)

Jobs
^^^^

.. js:function:: olwclient.killJob(job_id, array_index, callback, errback)

        Kills the job.  The user must be a job owner, queue or cluster administrator for this operation to succeed.

    :param job_id: Numeric Job ID.

    :param array_index: Array index of the job.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.requeueJob(job_id, array_index, hold, callback, errback)

        Requeues the job.  The user must be a job owner,  queue or cluster administrator for this operation to succeed.

    :param job_id: Numeric Job ID.

    :param array_index: Array index of the job.

    :param bool hold:

        When true, jobs will be held in the suspended pending state.

        .. note::

            Openlava Only! This property is specific to Openlava and is not generic to all cluster interfaces.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.suspendJob(job_id, array_index, callback, errback)

    Suspends the job.  The user must be a job owner, queue or cluster administrator for this operation to succeed.

    :param job_id: Numeric Job ID.

    :param array_index: Array index of the job.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.resumeJob(job_id, array_index, callback, errback)

    Resumes the job.  The user must be a job owner, queue or cluster administrator for this operation to succeed.

    :param job_id: Numeric Job ID.

    :param array_index: Array index of the job.

    :param function callback:
        A function that will be called when the task is successfully completed. No arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

Hosts
^^^^^

.. js:function:: olwclient.openHost(hostName, callback, errback)

    Open a specified host without retrieving the host object.

    :param string hostname:

        Hostname of host

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.closeHost(hostName, callback, errback)

    Close a specified host without retrieving the host object.

    :param string hostname:

        Hostname of host

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

Queue
^^^^^

.. js:attribute:: olwclient.closeQueue(queueName, callback, errback)

    Close the specified queue.

    :param string queueName:

        The name of the queue.

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.openQueue(queueName, callback, errback)

    Open the specified queue.

    :param string queueName:

        The name of the queue.

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.activateQueue(queueName, callback, errback)

    Activate the specified queue.

    :param string queueName:

    The name of the queue.

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:attribute:: olwclient.inactivateQueue(queueName, callback, errback)

    Inactivate the queue.

    :param string queueName:

        The name of the queue.

    :param callback callback:

        A callback to execute on success, no arguments.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

Error Callback
--------------

This function is called when an operation on the remote server failed.  In most circumstances
it will be based on an error returned by the remote server, however if the server is unavailable
or the AJAX call fails, then the error will also be set accordingly.

.. js:function:: olwclient.errBack(errType, message)

    When error handling is needed, a callback should be specified that accepts the following arguments.

    :param string errType: The type of error raised, it is the name of a ClusterException class.

    :param string message: A description of the error raised.

Overview Functions
------------------

.. js:function:: olwclient.getHostOverview(callback, errback)

    Gets an overview of host states.

    :param callback callback:

        A callback to execute on success, host overview as single object argument.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.getJobOverview(callback, errback)

    Gets an overview of job states

    :param callback callback:

        A callback to execute on success, job overview as single object.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

.. js:function:: olwclient.getSlotsOverview(callback, errback)

    Gets an overview of slot states

    :param callback callback:

        A callback to execute on success, slot overview as single object argument.

    :param callback errback:

        A callback to an ..js:function::`.errBack`  to execute on failure.

