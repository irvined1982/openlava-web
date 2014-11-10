ReSTful Web Interface
=====================

Both the javascript library, and the olwclient library use the following ReSTful interface.

.. contents::

Standard Response Format
------------------------

The standard JSON response is a JSON object containing three attributes:

Status
^^^^^^

A string, either OK, or FAIL.  OK indicates that the request was successfully executed without error.
Fail indicates that the request was not successful, this can be either due to an unexpected error, or
because the request was not valid or appropriate.

Message
^^^^^^^

An optional string containing a message describing the response, this can be left Null, empty, or set
to a string.

Data
^^^^

An optional object that is returned to the client.

::

    {
        "status": "OK|FAIL",
        "message": "Optional Message",
        "data": object
    }

Logging In
----------

.. http:post:: accounts/ajax_login

    Logs in an ajax client by allowing the client to upload the username/password combination.

    .. todo: Check if this is a REALLY BAD IDEA?!?!?

    The username password combo should be JSON serialized and sent as the POST data.

    Example POST data::

        {
            "password": "topsecret",
            "username": "bob"
        }


    On success, returns a JSON serialized response with no data, and the message set to "User logged in"

    Example Success Response::

        {
            "data": null,
            "message": "User logged in",
            "status": "OK"
        }

    On failure to authenticate, returns HTTP Error 403 not authenticated, the reason for the failure is specified
    in the message.

    Example Failure Response::

        {
            "data": null,
            "message": "Invalid username or password",
            "status": "FAIL"
        }

    :statuscode 200: no error
    :statuscode 403: Unable to authenticate user

CSRF Token
----------

.. http:get:: get_token

    The CSRF token is required to be sent to the server whenever the client uses a HTTP POST request.
    See: `Django CSRF Guide <https://docs.djangoproject.com/en/dev/ref/contrib/csrf/>`_

    Returns a JSON serialized dictionary containing a single item, called cookie, the value of which
    is set to the CSRF token.

    Example response::

        {
            "data": {
                "cookie": "Ca7mCejV7LKu1LN13bGtSaKZqCtHYGTp"
            },
            "message": "",
            "status": "OK"
        }

Host Operations
---------------

Host List
^^^^^^^^^

.. http:get:: hosts/

Opening a Host
^^^^^^^^^^^^^^

.. http:get:: hosts/(?P<host_name>.+?)/open

Closing a Host
^^^^^^^^^^^^^^

.. http:get:: hosts/(?P<host_name>.+?)/close

Getting information on a Host
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: hosts/(.+?)

Queue Operations
----------------

Queue List
^^^^^^^^^^

.. http:get:: queues/

Getting information on a Queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: queues/(.+?)

Closing a Queue
^^^^^^^^^^^^^^^

.. http:get:: queues/(?P<queue_name>.+?)/close

Opening a Queue
^^^^^^^^^^^^^^^

.. http:get:: queues/(?P<queue_name>.+?)/open

Inactivating a Queue
^^^^^^^^^^^^^^^^^^^^

.. http:get:: queues/(?P<queue_name>.+?)/inactivate

Activating a Queue
^^^^^^^^^^^^^^^^^^
.. http:get:: queues/(?P<queue_name>.+?)/activate

User Operations
---------------

User List
^^^^^^^^^

.. http:get:: users/

Getting information on a User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: users/(.+?)

Jobs
----

.. http:get:: jobs/(?P<job_id>\d+)/$', 'openlavaweb.views.get_job_list', name="olw_job_list"),

.. http:get:: jobs/$', 'openlavaweb.views.get_job_list', name="olw_job_list"),

.. http:post:: job/submit

.. http:post:: job/submit/(?P<form_class>.+)

.. http:get:: job/(\d+)/(\d+)

.. http:get:: job/(\d+)/(\d+)/output

.. http:get:: job/(\d+)/(\d+)/error

.. http:get:: job/(\d+)/(\d+)/kill

.. http:get:: job/(\d+)/(\d+)/suspend

.. http:get:: job/(\d+)/(\d+)/resume

.. http:get:: job/(\d+)/(\d+)/requeue

Overviews
---------

Host State
^^^^^^^^^^

.. http:get:: overview/hosts

Example response::

    {
        "data": [
            {
                "label": "Down",
                "value": 4
            },
            {
                "label": "In Use",
                "value": 0
            },
            {
                "label": "Full",
                "value": 2
            },
            {
                "label": "Closed",
                "value": 0
            },
            {
                "label": "Empty",
                "value": 0
            }
        ],
        "message": "",
        "status": "OK"
    }

Job State
^^^^^^^^^

.. http:get:: overview/jobs


Example response::

    {
        "data": [
            {
                "label": "Running",
                "value": 3
            },
            {
                "label": "Pending",
                "value": 256
            }
        ],
        "message": "",
        "status": "OK"
    }

Slot State
^^^^^^^^^^

.. http:get:: overview/slots

Example response::

    {
        "data": [
            {
                "label": "Running",
                "value": 2
            },
            {
                "label": "Pending",
                "value": 255
            }
        ],
        "message": "",
        "status": "OK"
    }

