Cluster API
===========

The Cluster API defines the standard API used to interface with the local scheduling system, this is designed to be
independent of the scheduling environment, currently a reference implementation exists for Openlava only.

The Cluster API is mirrored in the client API, which is designed to be accessed via the olwclient python
library.

A third, Javascript library exists for accessing Openlava-Web from within a web browser.

.. contents::

Process Classes
---------------

Process classes represent individual processes that are executing on a given host.

.. autoclass:: cluster.Process
    :members:

Resource Limit Classes
----------------------

Resource limits classes define resource limits that are imposed on a given job.

.. autoclass:: cluster.ResourceLimit
    :members:

Consumed Resources
------------------

Consumed resources represent resources that have been consumed by a given job.

.. autoclass:: cluster.ConsumedResource
    :members:

Cluster Resources
-----------------

.. autoclass:: cluster.openlavacluster.Resource
    :members:
    :inherited-members:

Job Classes
-----------

Job classes are used to get information about, and manipulate jobs on the scheduler.  Each class, whether local,
remote client, or javascript implements the same interface, albeit with slightly different arguments where required.

The local Job class uses openlava.lsblib to communicate with the Openlava Job Scheduler.  The current host must be
part of an openlava cluster, although it does not need to be a job server.  cluster.openlavacluster.Job implements the
cluster.JobBase interface.

.. autoclass:: cluster.openlavacluster.Job
    :members:

Job Status
^^^^^^^^^^

Job Status classes are used to define the current status of a job.

.. autoclass:: cluster.openlavacluster.JobStatus
    :members:
    :inherited-members:

Job Options
^^^^^^^^^^^

Job Option classes define options that were specified for a job.

.. autoclass:: cluster.openlavacluster.SubmitOption
    :members:
    :inherited-members:

.. autoclass:: cluster.openlavacluster.Submit2Option
    :members:
    :inherited-members:

Host Classes
------------

Host classes are used to get information about and manipulate hosts on the cluster.  Primarily this is done through the
Host() class, however when associated with a Job() they may be through ExecutionHost classes which also contain
information on the number of slots that are allocated to the job.

.. autoclass:: cluster.openlavacluster.Host
    :members:

.. autoclass:: cluster.openlavacluster.ExecutionHost
    :members:
    :inherited-members:

Host Statuses
^^^^^^^^^^^^^

Host Statuses define the status of an individual host.

.. autoclass:: cluster.openlavacluster.HostStatus
    :members:
    :inherited-members:

Queue Classes
-------------

Queue classes represent individual queues that are configured as part of the cluster.

.. autoclass:: cluster.openlavacluster.Queue
    :members:

Queue Statuses
^^^^^^^^^^^^^^

.. autoclass:: cluster.openlavacluster.QueueStatus

Queue Attributes
^^^^^^^^^^^^^^^^

.. autoclass:: cluster.openlavacluster.QueueAttribute

user Classes
------------

User classes represent individual users that are part of the cluster configuration.

.. autoclass:: cluster.openlavacluster.User
    :members:

Exceptions
----------

The following exceptions are defined when using the Local interface.

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

