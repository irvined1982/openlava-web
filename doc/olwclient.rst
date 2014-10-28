API Documentation
=================

.. contents::

Job Classes
-----------

Job classes are used to get information about, and manipulate jobs on the scheduler.  Each class, whether local,
remote client, or javascript implements the same interface, albeit with slightly different arguments where required.

Local
^^^^^

The local Job class uses openlava.lsblib to communicate with the Openlava Job Scheduler.  The current host must be
part of an openlava cluster, although it does not need to be a job server.  cluster.openlavacluster.Job implements the
cluster.JobBase interface.

.. autoclass:: cluster.openlavacluster.Job
    :members:

Olwclient
^^^^^^^^^

Olwclient uses the RESTful interface to the olweb server to communicate with the scheduler.  Openlava-web is then
responsible for connecting to the job scheduler and retrieving job information.  This is then serialized using JSON
and sent back to the client.

.. autoclass:: olwclient.Job
    :members:

JavaScript
^^^^^^^^^^

.. js:class:: Job(url, job_id, array_index)

    :param url: URL of the openlava web server
    :param job_id: The job_id to load
    :param array_index: The array index to load

Process Classes
---------------

Process classes represent individual processes that are executing on a given host.

Local
^^^^^
.. autoclass:: cluster.Process

Olwclient
^^^^^^^^^

.. autoclass:: olwclient.Process

Resource Limit Classes
----------------------

Resource limits classes define resource limits that are imposed on a given job.

Local
^^^^^

.. autoclass:: cluster.ResourceLimit
    :members:

Olwclient
^^^^^^^^^

.. autoclass:: olwclient.ResourceLimit
    :members:

Consumed Resources
------------------

Consumed resources represent resources that have been consumed by a given job.

Local
^^^^^

.. autoclass:: cluster.ConsumedResource
    :members:

Olwclient
^^^^^^^^^
.. autoclass:: olwclient.ConsumedResource
    :members:

Processees
----------

Local
^^^^^
.. autoclass:: cluster.Process
    :members:

Olwclient
^^^^^^^^^

.. autoclass:: olwclient.Process
    :members:

Job Status
----------

Local
^^^^^

.. autoclass:: cluster.openlavacluster.JobStatus
    :members:
    :inherited-members:

Olwclient
^^^^^^^^^

.. autoclass:: olwclient.JobStatus
    :members:
    :inherited-members:

Job Options
-----------

Local
^^^^^

.. autoclass:: cluster.openlavacluster.SubmitOption
    :members:
    :inherited-members:

.. autoclass:: cluster.openlavacluster.Submit2Option
    :members:
    :inherited-members:

Olwclient
^^^^^^^^^

.. autoclass:: olwclient.JobOption
    :members:
    :inherited-members:

Host Classes
------------

Host classes are used to get information about and manipulate hosts on the cluster.  Primarily this is done through the
Host() class, however when associated with a Job() they may be through ExecutionHost classes which also contain
information on the number of slots that are allocated to the job.

Local
^^^^^

.. autoclass:: cluster.openlavacluster.Host
    :members:

.. autoclass:: cluster.openlavacluster.ExecutionHost
    :members:
    :inherited-members:

Client
^^^^^^

.. autoclass:: olwclient.Host
    :members:


JavaScript
^^^^^^^^^^

.. js:class:: Host(url, host_name)

    :param url: URL of the openlava web server
    :param host_name: The name of the host to load

.. js:class:: ExecutionHost(url, host_name, num_slots_for_job)

    :param url: URL of the openlava web server
    :param host_name: The name of the host to load
    :param num_slots_for_job: The number of slots allocated to the job

Host Statuses
-------------

.. autoclass:: cluster.openlavacluster.HostStatus
    :members:
    :inherited-members:

Cluster Resources
-----------------

.. autoclass:: cluster.openlavacluster.Resource
    :members:
    :inherited-members:

Exceptions
----------

Local
^^^^^

.. autoclass:: cluster.ClusterException
    :members:

.. autoclass:: cluster.NoSuchHostError
    :members:

.. autoclass:: cluster.NoSuchJobError
    :members:

.. autoclass:: cluster.NoSuchQueueError
    :members:

.. autoclass:: cluster.NoSuchUserError
    :members:

.. autoclass:: cluster.ResourceDoesntExistError
    :members:

.. autoclass:: cluster.ClusterInterfaceError
    :members:

.. autoclass:: cluster.PermissionDeniedError
    :members:

.. autoclass:: cluster.JobSubmitError
    :members:

.. autoclass:: cluster.openlavacluster.ClusterException
    :members:


Client
^^^^^^

.. autoclass:: olwclient.RemoteServerError
    :members:
    :inherited-members:

.. autoclass:: olwclient.AuthenticationError
    :members:
    :inherited-members:
