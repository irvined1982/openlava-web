Javascript API
==============

The Javascript API defines the standard API used to interface with a remote openlava web server. This is
designed to be independent of the scheduling environment, regardless of the underlying scheduling system
being used by openlava-web the returned data will be in a standard format, and have a consistent API.

The Javascript API generally mirrors that of the cluster API where possible.  As such programming one is
almost identical to programming the other.

.. contents::

.. js:data:: olwclient.serverUrl

    URL to the Openlava Web Server

Authentication
--------------

.. js:func:: olwclient.login(username, password, callback, errback)

    Authenticate using the provided credentials and obtain the session cookie and csrf token.

    :param string olwclient.username:

        The username to use when authenticating to the openlava web server.

    :param string password:

        The password to use when authenticating to the openlava web server.

    :param callback callback:

        A callback to execute on success, no args.

    :param callback errback:

        A callback to execute on failure, args: str errType, str: message.

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

Job Classes
-----------

Olwclient uses the RESTful interface to the olweb server to communicate with the scheduler.  Openlava-web is then
responsible for connecting to the job scheduler and retrieving job information.  This is then serialized using JSON
and sent back to the client.

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

        A callback to execute on failure, args: str errType, str: message.

    :param object data:

        Data object to use to fill data structures.  If data is provided, then all other args are ignored
        and the object is returned.


Queue Classes
-------------

Queue classes represent individual queues that are configured as part of the cluster.

User Classes
------------

User classes represent individual users that are configured in the cluster.
