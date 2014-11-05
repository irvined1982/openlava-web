Cluster API
===========

The Olwclient API defines the standard API used to interface with a remote openlava web server. This is
designed to be independent of the scheduling environment, regardless of the underlying scheduling system
being used by openlava-web the returned data will be in a standard format, and have a consistent API.

The olwclient API generally mirrors that of the cluster API where possible.  As such programming one is
almost identical to programming the other.

.. contents::

Status Classes
---------------

Status Classes define statuses, which all have a standard behavior.  This may be for a host, job, queue, or
any other object that has one or more statuses.

.. autoclass:: olwclient.Status
    :members:

Cluster Resources
^^^^^^^^^^^^^^^^^

.. autoclass:: cluster.openlavacluster.Resource
    :members:
    :inherited-members:

Resource Limit Classes
^^^^^^^^^^^^^^^^^^^^^^

Resource limits classes define resource limits that are imposed on a given job.

.. autoclass:: olwclient.ResourceLimit
    :members:

Consumed Resources
^^^^^^^^^^^^^^^^^^

Consumed resources represent resources that have been consumed by a given job.

.. autoclass:: olwclient.ConsumedResource
    :members:

Job Classes
-----------

Olwclient uses the RESTful interface to the olweb server to communicate with the scheduler.  Openlava-web is then
responsible for connecting to the job scheduler and retrieving job information.  This is then serialized using JSON
and sent back to the client.

.. autoclass:: olwclient.Job
    :members:

Host Classes
------------

Host classes are used to get information about and manipulate hosts on the cluster.  Primarily this is done through the
Host() class, however when associated with a Job() they may be through ExecutionHost classes which also contain
information on the number of slots that are allocated to the job.

.. autoclass:: olwclient.Host
    :members:

.. autoclass:: olwclient.ExecutionHost
    :members:

Queue Classes
-------------

Queue classes represent individual queues that are configured as part of the cluster.

.. autoclass:: olwclient.Queue
    :members:

Exceptions
----------

The following exceptions are defined when using the olwclient interface.

.. autoclass:: olwclient.RemoteServerError
    :members:
    :inherited-members:

.. autoclass:: olwclient.AuthenticationError
    :members:
    :inherited-members:

.. autoclass:: olwclient.ClusterException
    :members:

.. autoclass:: olwclient.NoSuchHostError
    :members:

.. autoclass:: olwclient.NoSuchJobError
    :members:

.. autoclass:: olwclient.NoSuchQueueError
    :members:

.. autoclass:: olwclient.NoSuchUserError
    :members:

.. autoclass:: olwclient.ResourceDoesntExistError
    :members:

.. autoclass:: olwclient.ClusterInterfaceError
    :members:

.. autoclass:: olwclient.PermissionDeniedError
    :members:

.. autoclass:: olwclient.JobSubmitError
    :members:

.. autoclass:: olwclient.ClusterException
    :members:
