API Documentation
=================

JOB Classes
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



Exceptions
----------

NoSuchJobError

ClusterException
