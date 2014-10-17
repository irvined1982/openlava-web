API Documentation
=================

Job Classes
-----------

Job classes are used to get information about, and manipulate jobs on the scheduler.  Each class, whether local,
remote client, or javascript implements the same interface, albeit with slightly different arguments where required.

Local
^^^^^

.. autoclass:: cluster.openlavacluster.Job
    :members:

Client
^^^^^^

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

.. autoclass:: cluster.Process

Resource Limit Classes
----------------------

Resource limits classes define resource limits that are imposed on a given job.

.. autoclass:: cluster.ResourceLimit

Consumed Resources
------------------

Consumed resources represent resources that have been consumed by a given job.

.. autoclass:: cluster.ConsumedResource

Job Status
----------

.. autoclass:: cluster.openlavacluster.JobStatus




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

Client
^^^^^^

.. autoclass:: olwclient.Host
    :members:

.. autoclass:: olwclient.ExecutionHost
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


Exceptions
----------

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