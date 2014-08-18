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

.. autoclass:: cluster.openlavacluster.ExecutionHost
    :members

Client
^^^^^^

.. autoclass:: olwclient.Job
    :members:

.. autoclass:: olwclient.ExecutionHost
    :members


JavaScript
^^^^^^^^^^

.. js:class:: Job(url, job_id, array_index)

    :param url: URL of the openlava web server
    :param job_id: The job_id to load
    :param array_index: The array index to load



Exceptions
----------

NoSuchJobError

ClusterException


Host Classes
-----------

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
    :members


JavaScript
^^^^^^^^^^

.. js:class:: Host(url, host_name)

    :param url: URL of the openlava web server
    :param host_name: The name of the host to load

.. js:class:: ExecutionHost(url, host_name, num_slots_for_job)

    :param url: URL of the openlava web server
    :param host_name: The name of the host to load
    :param num_slots_for_job: The number of slots allocated to the job


