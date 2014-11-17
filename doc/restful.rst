ReSTful Web Interface
=====================

Both the javascript library, and the olwclient library use the following ReSTful interface.
There is no reason however, that this can not be used by other libraries or end users directly.

Whenever a client passes the query parameter json (with a value) or uses an ajax call or accepts
application/json content types, the response will be as follows.  All responses with the exception
of job output (which return plain text.) use a standard response format as described below.

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

    Lists all host

    Example::

        {
            "data": [
                {
                    "admins": [
                        "openlava"
                    ],
                    "cluster_type": "openlava",
                    "cpu_factor": 100.0,
                    "description": "",
                    "has_checkpoint_support": true,
                    "has_kernel_checkpoint_copy": false,
                    "host_model": "IntelI5",
                    "host_name": "master",
                    "host_type": "linux",
                    "is_busy": false,
                    "is_closed": false,
                    "is_down": false,
                    "is_server": true,
                    "jobs": [],
                    "load_information": {
                        "names": [
                            "15s Load",
                            "1m Load",
                            "15m Load",
                            "Avg CPU Utilization",
                            "Paging Rate (Pages/Sec)",
                            "Disk IO Rate (MB/Sec)",
                            "Num Users",
                            "Idle Time",
                            "Tmp Space (MB)",
                            "Free Swap (MB)",
                            "Free Memory (MB)"
                        ],
                        "short_names": [
                            "r15s",
                            "r1m",
                            "r15m",
                            "ut",
                            "pg",
                            "io",
                            "ls",
                            "it",
                            "tmp",
                            "swp",
                            "mem"
                        ],
                        "values": [
                            {
                                "name": "Actual Load",
                                "values": [
                                    0.0,
                                    0.009999990463256836,
                                    0.04999995231628418,
                                    0.0,
                                    0.0,
                                    0.0,
                                    3.0,
                                    12.0,
                                    53895.0,
                                    509.48046875,
                                    578.59765625
                                ]
                            },
                            {
                                "name": "Stop Dispatching Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            },
                            {
                                "name": "Stop Executing Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            }
                        ]
                    },
                    "max_jobs": 2,
                    "max_processors": 1,
                    "max_ram": 992,
                    "max_slots": 2,
                    "max_slots_per_user": 2147483647,
                    "max_swap": 509,
                    "max_tmp": 64002,
                    "name": "master",
                    "num_disks": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "resources": [
                        {
                            "description": "Foo Variable",
                            "flags": 4,
                            "interval": 0.0,
                            "name": "foo",
                            "order": "NA",
                            "type": "Boolean"
                        }
                    ],
                    "run_windows": "-",
                    "statuses": [
                        {
                            "description": "Ready to accept and run jobs.  ",
                            "friendly": "Ok",
                            "name": "HOST_STAT_OK",
                            "status": 0,
                            "type": "HostStatus"
                        }
                    ],
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "Host"
                },
                {
                    "admins": [
                        "openlava"
                    ],
                    "cluster_type": "openlava",
                    "cpu_factor": 100.0,
                    "description": "",
                    "has_checkpoint_support": true,
                    "has_kernel_checkpoint_copy": false,
                    "host_model": "IntelI5",
                    "host_name": "comp00",
                    "host_type": "linux",
                    "is_busy": false,
                    "is_closed": false,
                    "is_down": true,
                    "is_server": true,
                    "jobs": [],
                    "load_information": {
                        "names": [
                            "15s Load",
                            "1m Load",
                            "15m Load",
                            "Avg CPU Utilization",
                            "Paging Rate (Pages/Sec)",
                            "Disk IO Rate (MB/Sec)",
                            "Num Users",
                            "Idle Time",
                            "Tmp Space (MB)",
                            "Free Swap (MB)",
                            "Free Memory (MB)"
                        ],
                        "short_names": [
                            "r15s",
                            "r1m",
                            "r15m",
                            "ut",
                            "pg",
                            "io",
                            "ls",
                            "it",
                            "tmp",
                            "swp",
                            "mem"
                        ],
                        "values": [
                            {
                                "name": "Actual Load",
                                "values": [
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0
                                ]
                            },
                            {
                                "name": "Stop Dispatching Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            },
                            {
                                "name": "Stop Executing Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            }
                        ]
                    },
                    "max_jobs": 1,
                    "max_processors": 0,
                    "max_ram": 0,
                    "max_slots": 1,
                    "max_slots_per_user": 2147483647,
                    "max_swap": 0,
                    "max_tmp": 0,
                    "name": "comp00",
                    "num_disks": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "resources": [],
                    "run_windows": "-",
                    "statuses": [
                        {
                            "description": "Ready to accept and run jobs.  ",
                            "friendly": "Ok",
                            "name": "HOST_STAT_OK",
                            "status": 0,
                            "type": "HostStatus"
                        },
                        {
                            "description": "The LIM and sbatchd on this host are unavailable.  ",
                            "friendly": "Unavailable",
                            "name": "HOST_STAT_UNAVAIL",
                            "status": 64,
                            "type": "HostStatus"
                        }
                    ],
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "Host"
                },
                {
                    "admins": [
                        "openlava"
                    ],
                    "cluster_type": "openlava",
                    "cpu_factor": 100.0,
                    "description": "",
                    "has_checkpoint_support": true,
                    "has_kernel_checkpoint_copy": false,
                    "host_model": "IntelI5",
                    "host_name": "comp01",
                    "host_type": "linux",
                    "is_busy": false,
                    "is_closed": false,
                    "is_down": true,
                    "is_server": true,
                    "jobs": [],
                    "load_information": {
                        "names": [
                            "15s Load",
                            "1m Load",
                            "15m Load",
                            "Avg CPU Utilization",
                            "Paging Rate (Pages/Sec)",
                            "Disk IO Rate (MB/Sec)",
                            "Num Users",
                            "Idle Time",
                            "Tmp Space (MB)",
                            "Free Swap (MB)",
                            "Free Memory (MB)"
                        ],
                        "short_names": [
                            "r15s",
                            "r1m",
                            "r15m",
                            "ut",
                            "pg",
                            "io",
                            "ls",
                            "it",
                            "tmp",
                            "swp",
                            "mem"
                        ],
                        "values": [
                            {
                                "name": "Actual Load",
                                "values": [
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0
                                ]
                            },
                            {
                                "name": "Stop Dispatching Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            },
                            {
                                "name": "Stop Executing Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            }
                        ]
                    },
                    "max_jobs": 1,
                    "max_processors": 0,
                    "max_ram": 0,
                    "max_slots": 1,
                    "max_slots_per_user": 2147483647,
                    "max_swap": 0,
                    "max_tmp": 0,
                    "name": "comp01",
                    "num_disks": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "resources": [],
                    "run_windows": "-",
                    "statuses": [
                        {
                            "description": "Ready to accept and run jobs.  ",
                            "friendly": "Ok",
                            "name": "HOST_STAT_OK",
                            "status": 0,
                            "type": "HostStatus"
                        },
                        {
                            "description": "The LIM and sbatchd on this host are unavailable.  ",
                            "friendly": "Unavailable",
                            "name": "HOST_STAT_UNAVAIL",
                            "status": 64,
                            "type": "HostStatus"
                        }
                    ],
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "Host"
                },
                {
                    "admins": [
                        "openlava"
                    ],
                    "cluster_type": "openlava",
                    "cpu_factor": 100.0,
                    "description": "",
                    "has_checkpoint_support": true,
                    "has_kernel_checkpoint_copy": false,
                    "host_model": "IntelI5",
                    "host_name": "comp02",
                    "host_type": "linux",
                    "is_busy": false,
                    "is_closed": false,
                    "is_down": true,
                    "is_server": true,
                    "jobs": [],
                    "load_information": {
                        "names": [
                            "15s Load",
                            "1m Load",
                            "15m Load",
                            "Avg CPU Utilization",
                            "Paging Rate (Pages/Sec)",
                            "Disk IO Rate (MB/Sec)",
                            "Num Users",
                            "Idle Time",
                            "Tmp Space (MB)",
                            "Free Swap (MB)",
                            "Free Memory (MB)"
                        ],
                        "short_names": [
                            "r15s",
                            "r1m",
                            "r15m",
                            "ut",
                            "pg",
                            "io",
                            "ls",
                            "it",
                            "tmp",
                            "swp",
                            "mem"
                        ],
                        "values": [
                            {
                                "name": "Actual Load",
                                "values": [
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0
                                ]
                            },
                            {
                                "name": "Stop Dispatching Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            },
                            {
                                "name": "Stop Executing Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            }
                        ]
                    },
                    "max_jobs": 1,
                    "max_processors": 0,
                    "max_ram": 0,
                    "max_slots": 1,
                    "max_slots_per_user": 2147483647,
                    "max_swap": 0,
                    "max_tmp": 0,
                    "name": "comp02",
                    "num_disks": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "resources": [],
                    "run_windows": "-",
                    "statuses": [
                        {
                            "description": "Ready to accept and run jobs.  ",
                            "friendly": "Ok",
                            "name": "HOST_STAT_OK",
                            "status": 0,
                            "type": "HostStatus"
                        },
                        {
                            "description": "The LIM and sbatchd on this host are unavailable.  ",
                            "friendly": "Unavailable",
                            "name": "HOST_STAT_UNAVAIL",
                            "status": 64,
                            "type": "HostStatus"
                        }
                    ],
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "Host"
                },
                {
                    "admins": [
                        "openlava"
                    ],
                    "cluster_type": "openlava",
                    "cpu_factor": 100.0,
                    "description": "",
                    "has_checkpoint_support": true,
                    "has_kernel_checkpoint_copy": false,
                    "host_model": "IntelI5",
                    "host_name": "comp03",
                    "host_type": "linux",
                    "is_busy": false,
                    "is_closed": false,
                    "is_down": true,
                    "is_server": true,
                    "jobs": [],
                    "load_information": {
                        "names": [
                            "15s Load",
                            "1m Load",
                            "15m Load",
                            "Avg CPU Utilization",
                            "Paging Rate (Pages/Sec)",
                            "Disk IO Rate (MB/Sec)",
                            "Num Users",
                            "Idle Time",
                            "Tmp Space (MB)",
                            "Free Swap (MB)",
                            "Free Memory (MB)"
                        ],
                        "short_names": [
                            "r15s",
                            "r1m",
                            "r15m",
                            "ut",
                            "pg",
                            "io",
                            "ls",
                            "it",
                            "tmp",
                            "swp",
                            "mem"
                        ],
                        "values": [
                            {
                                "name": "Actual Load",
                                "values": [
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0
                                ]
                            },
                            {
                                "name": "Stop Dispatching Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            },
                            {
                                "name": "Stop Executing Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            }
                        ]
                    },
                    "max_jobs": 1,
                    "max_processors": 0,
                    "max_ram": 0,
                    "max_slots": 1,
                    "max_slots_per_user": 2147483647,
                    "max_swap": 0,
                    "max_tmp": 0,
                    "name": "comp03",
                    "num_disks": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "resources": [],
                    "run_windows": "-",
                    "statuses": [
                        {
                            "description": "Ready to accept and run jobs.  ",
                            "friendly": "Ok",
                            "name": "HOST_STAT_OK",
                            "status": 0,
                            "type": "HostStatus"
                        },
                        {
                            "description": "The LIM and sbatchd on this host are unavailable.  ",
                            "friendly": "Unavailable",
                            "name": "HOST_STAT_UNAVAIL",
                            "status": 64,
                            "type": "HostStatus"
                        }
                    ],
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "Host"
                },
                {
                    "admins": [
                        "openlava"
                    ],
                    "cluster_type": "openlava",
                    "cpu_factor": 100.0,
                    "description": "",
                    "has_checkpoint_support": true,
                    "has_kernel_checkpoint_copy": false,
                    "host_model": "IntelI5",
                    "host_name": "comp04",
                    "host_type": "linux",
                    "is_busy": false,
                    "is_closed": false,
                    "is_down": true,
                    "is_server": true,
                    "jobs": [],
                    "load_information": {
                        "names": [
                            "15s Load",
                            "1m Load",
                            "15m Load",
                            "Avg CPU Utilization",
                            "Paging Rate (Pages/Sec)",
                            "Disk IO Rate (MB/Sec)",
                            "Num Users",
                            "Idle Time",
                            "Tmp Space (MB)",
                            "Free Swap (MB)",
                            "Free Memory (MB)"
                        ],
                        "short_names": [
                            "r15s",
                            "r1m",
                            "r15m",
                            "ut",
                            "pg",
                            "io",
                            "ls",
                            "it",
                            "tmp",
                            "swp",
                            "mem"
                        ],
                        "values": [
                            {
                                "name": "Actual Load",
                                "values": [
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0,
                                    2147483648.0
                                ]
                            },
                            {
                                "name": "Stop Dispatching Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            },
                            {
                                "name": "Stop Executing Load",
                                "values": [
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1,
                                    -1
                                ]
                            }
                        ]
                    },
                    "max_jobs": 1,
                    "max_processors": 0,
                    "max_ram": 0,
                    "max_slots": 1,
                    "max_slots_per_user": 2147483647,
                    "max_swap": 0,
                    "max_tmp": 0,
                    "name": "comp04",
                    "num_disks": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "resources": [],
                    "run_windows": "-",
                    "statuses": [
                        {
                            "description": "Ready to accept and run jobs.  ",
                            "friendly": "Ok",
                            "name": "HOST_STAT_OK",
                            "status": 0,
                            "type": "HostStatus"
                        },
                        {
                            "description": "The LIM and sbatchd on this host are unavailable.  ",
                            "friendly": "Unavailable",
                            "name": "HOST_STAT_UNAVAIL",
                            "status": 64,
                            "type": "HostStatus"
                        }
                    ],
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "Host"
                }
            ],
            "message": "",
            "status": "OK"
        }

Getting information on a Host
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: hosts/(string:host_name)

    Provides detailed information on a host

    :param string host_name: The name of the host view

    Example::

        {
            "data": {
                "admins": [
                    "openlava"
                ],
                "cluster_type": "openlava",
                "cpu_factor": 100.0,
                "description": "",
                "has_checkpoint_support": true,
                "has_kernel_checkpoint_copy": false,
                "host_model": "IntelI5",
                "host_name": "comp01",
                "host_type": "linux",
                "is_busy": false,
                "is_closed": false,
                "is_down": true,
                "is_server": true,
                "jobs": [],
                "load_information": {
                    "names": [
                        "15s Load",
                        "1m Load",
                        "15m Load",
                        "Avg CPU Utilization",
                        "Paging Rate (Pages/Sec)",
                        "Disk IO Rate (MB/Sec)",
                        "Num Users",
                        "Idle Time",
                        "Tmp Space (MB)",
                        "Free Swap (MB)",
                        "Free Memory (MB)"
                    ],
                    "short_names": [
                        "r15s",
                        "r1m",
                        "r15m",
                        "ut",
                        "pg",
                        "io",
                        "ls",
                        "it",
                        "tmp",
                        "swp",
                        "mem"
                    ],
                    "values": [
                        {
                            "name": "Actual Load",
                            "values": [
                                2147483648.0,
                                2147483648.0,
                                2147483648.0,
                                2147483648.0,
                                2147483648.0,
                                2147483648.0,
                                2147483648.0,
                                2147483648.0,
                                2147483648.0,
                                2147483648.0,
                                2147483648.0
                            ]
                        },
                        {
                            "name": "Stop Dispatching Load",
                            "values": [
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1
                            ]
                        },
                        {
                            "name": "Stop Executing Load",
                            "values": [
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1,
                                -1
                            ]
                        }
                    ]
                },
                "max_jobs": 1,
                "max_processors": 0,
                "max_ram": 0,
                "max_slots": 1,
                "max_slots_per_user": 2147483647,
                "max_swap": 0,
                "max_tmp": 0,
                "name": "comp01",
                "num_disks": 0,
                "num_reserved_slots": 0,
                "num_running_jobs": 0,
                "num_running_slots": 0,
                "num_suspended_jobs": 0,
                "num_suspended_slots": 0,
                "num_system_suspended_jobs": 0,
                "num_system_suspended_slots": 0,
                "num_user_suspended_jobs": 0,
                "num_user_suspended_slots": 0,
                "resources": [],
                "run_windows": "-",
                "statuses": [
                    {
                        "description": "Ready to accept and run jobs.  ",
                        "friendly": "Ok",
                        "name": "HOST_STAT_OK",
                        "status": 0,
                        "type": "HostStatus"
                    },
                    {
                        "description": "The LIM and sbatchd on this host are unavailable.  ",
                        "friendly": "Unavailable",
                        "name": "HOST_STAT_UNAVAIL",
                        "status": 64,
                        "type": "HostStatus"
                    }
                ],
                "total_jobs": 0,
                "total_slots": 0,
                "type": "Host"
            },
            "message": "",
            "status": "OK"
        }

Opening and Closing a Host
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: hosts/(string:host_name)/open

    Opens a host

    :param string host_name: The name of the host to open

    Example::

        {
            "data": {
                "exception_class": "PermissionDeniedError",
                "message": "Unable to open host: comp01: User permission denied"
            },
            "message": "Unable to open host: comp01: User permission denied",
            "status": "FAIL"
        }

.. http:get:: hosts/(string:host_name)/close

    Closes a host

    :param string host_name: The name of the host to close

    Example::

        {
            "data": {
                "exception_class": "PermissionDeniedError",
                "message": "Unable to close host: comp01: User permission denied"
            },
            "message": "Unable to close host: comp01: User permission denied",
            "status": "FAIL"
        }

Queue Operations
----------------

Queue List
^^^^^^^^^^

.. http:get:: queues/

    Lists all queues

    Example::

        {
            "data": [
                {
                    "accept_interval": 0,
                    "admins": [
                        "openlava"
                    ],
                    "allowed_hosts": [],
                    "allowed_users": [],
                    "attributes": [
                        {
                            "description": "This queue is a default LSF queue. ",
                            "friendly": "Default Queue",
                            "name": "Q_ATTRIB_DEFAULT",
                            "status": 2,
                            "type": "QueueAttribute"
                        }
                    ],
                    "checkpoint_data_directory": "",
                    "checkpoint_period": -1,
                    "cluster_type": "openlava",
                    "default_slots_per_job": -1,
                    "description": "For normal low priority jobs, running only if hosts are lightly loaded.",
                    "dispatch_windows": "",
                    "host_specification": "",
                    "is_accepting_jobs": true,
                    "is_dispatching_jobs": true,
                    "job_starter_command": "",
                    "jobs": [],
                    "max_jobs": 2147483647,
                    "max_jobs_per_host": 2147483647,
                    "max_jobs_per_processor": 2147483648.0,
                    "max_jobs_per_user": 2147483647,
                    "max_slots": 2147483647,
                    "max_slots_per_host": 2147483647,
                    "max_slots_per_job": -1,
                    "max_slots_per_processor": 2147483648.0,
                    "max_slots_per_user": 2147483647,
                    "migration_threshold": 2147483647,
                    "min_slots_per_job": -1,
                    "name": "normal",
                    "nice": 20,
                    "num_pending_jobs": 0,
                    "num_pending_slots": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "post_execution_command": "",
                    "pre_execution_command": "",
                    "pre_post_user_name": "",
                    "priority": 30,
                    "requeue_exit_values": [],
                    "resource_requirements": "",
                    "resume_action_command": "",
                    "resume_condition": "",
                    "run_windows": " ",
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "scheduling_delay": 2147483647,
                    "slot_hold_time": 0,
                    "statuses": [
                        {
                            "description": "The queue is open to accept newly submitted jobs.",
                            "friendly": "Open",
                            "name": "QUEUE_STAT_OPEN",
                            "status": 1,
                            "type": "QueueStatus"
                        },
                        {
                            "description": "The queue is actively dispatching jobs. The queue can be inactivated and reactivated by             the LSF administrator using lsb_queuecontrol. The queue will also be inactivated when its run or dispatch             window is closed. In this case it cannot be reactivated manually; it will be reactivated by the LSF system             when its run and dispatch windows reopen.",
                            "friendly": "Active",
                            "name": "QUEUE_STAT_ACTIVE",
                            "status": 2,
                            "type": "QueueStatus"
                        },
                        {
                            "description": "The queue run and dispatch windows are open. The initial state of a queue at LSF boot time             is open and either active or inactive, depending on its run and dispatch windows.",
                            "friendly": "Run windows open",
                            "name": "QUEUE_STAT_RUN",
                            "status": 4,
                            "type": "QueueStatus"
                        }
                    ],
                    "stop_condition": "",
                    "suspend_action_command": "",
                    "terminate_action_command": "",
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "Queue"
                }
            ],
            "message": "",
            "status": "OK"
        }

Getting information on a Queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: queues/(string:queue_name)

    Details information on a queue

    :param string queue_name: The name of queue

    Example::

        {
            "data": {
                "accept_interval": 0,
                "admins": [
                    "openlava"
                ],
                "allowed_hosts": [],
                "allowed_users": [],
                "attributes": [
                    {
                        "description": "This queue is a default LSF queue. ",
                        "friendly": "Default Queue",
                        "name": "Q_ATTRIB_DEFAULT",
                        "status": 2,
                        "type": "QueueAttribute"
                    }
                ],
                "checkpoint_data_directory": "",
                "checkpoint_period": -1,
                "cluster_type": "openlava",
                "default_slots_per_job": -1,
                "description": "For normal low priority jobs, running only if hosts are lightly loaded.",
                "dispatch_windows": "",
                "host_specification": "",
                "is_accepting_jobs": true,
                "is_dispatching_jobs": true,
                "job_starter_command": "",
                "jobs": [],
                "max_jobs": 2147483647,
                "max_jobs_per_host": 2147483647,
                "max_jobs_per_processor": 2147483648.0,
                "max_jobs_per_user": 2147483647,
                "max_slots": 2147483647,
                "max_slots_per_host": 2147483647,
                "max_slots_per_job": -1,
                "max_slots_per_processor": 2147483648.0,
                "max_slots_per_user": 2147483647,
                "migration_threshold": 2147483647,
                "min_slots_per_job": -1,
                "name": "normal",
                "nice": 20,
                "num_pending_jobs": 0,
                "num_pending_slots": 0,
                "num_reserved_slots": 0,
                "num_running_jobs": 0,
                "num_running_slots": 0,
                "num_suspended_jobs": 0,
                "num_suspended_slots": 0,
                "num_system_suspended_jobs": 0,
                "num_system_suspended_slots": 0,
                "num_user_suspended_jobs": 0,
                "num_user_suspended_slots": 0,
                "post_execution_command": "",
                "pre_execution_command": "",
                "pre_post_user_name": "",
                "priority": 30,
                "requeue_exit_values": [],
                "resource_requirements": "",
                "resume_action_command": "",
                "resume_condition": "",
                "run_windows": " ",
                "runtime_limits": [
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "CPU Time",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "File Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Data Segment Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Stack Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Core Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "RSS Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Num Files",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Max Open Files",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Swap Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Run Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Process Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    }
                ],
                "scheduling_delay": 2147483647,
                "slot_hold_time": 0,
                "statuses": [
                    {
                        "description": "The queue is open to accept newly submitted jobs.",
                        "friendly": "Open",
                        "name": "QUEUE_STAT_OPEN",
                        "status": 1,
                        "type": "QueueStatus"
                    },
                    {
                        "description": "The queue is actively dispatching jobs. The queue can be inactivated and reactivated by             the LSF administrator using lsb_queuecontrol. The queue will also be inactivated when its run or dispatch             window is closed. In this case it cannot be reactivated manually; it will be reactivated by the LSF system             when its run and dispatch windows reopen.",
                        "friendly": "Active",
                        "name": "QUEUE_STAT_ACTIVE",
                        "status": 2,
                        "type": "QueueStatus"
                    },
                    {
                        "description": "The queue run and dispatch windows are open. The initial state of a queue at LSF boot time             is open and either active or inactive, depending on its run and dispatch windows.",
                        "friendly": "Run windows open",
                        "name": "QUEUE_STAT_RUN",
                        "status": 4,
                        "type": "QueueStatus"
                    }
                ],
                "stop_condition": "",
                "suspend_action_command": "",
                "terminate_action_command": "",
                "total_jobs": 0,
                "total_slots": 0,
                "type": "Queue"
            },
            "message": "",
            "status": "OK"
        }

Opening and Closing a Queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: queues/(string:queue_name)/close

    Closes a queue

    :param string queue_name: The name of queue

    Example::

        {
            "data": {
                "exception_class": "PermissionDeniedError",
                "message": "Unable to close queue: normal: User permission denied"
            },
            "message": "Unable to close queue: normal: User permission denied",
            "status": "FAIL"
        }

.. http:get:: queues/(string:queue_name)/open

    Opens a queue

    :param string queue_name: The name of queue

    Example::

        {
            "data": {
                "exception_class": "PermissionDeniedError",
                "message": "Unable to open queue: normal: User permission denied"
            },
            "message": "Unable to open queue: normal: User permission denied",
            "status": "FAIL"
        }

Inactivating and Activating a Queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: queues/(string:queue_name)/inactivate

    Inactivates a queue

    :param string queue_name: The name of queue

    Example::

        {
            "data": {
                "exception_class": "PermissionDeniedError",
                "message": "Unable to inactivate queue: normal: User permission denied"
            },
            "message": "Unable to inactivate queue: normal: User permission denied",
            "status": "FAIL"
        }

.. http:get:: queues/(string:queue_name)/activate

    Activates a queue.

    :param string queue_name: The name of queue

    Example::

        {
            "data": {
                "exception_class": "PermissionDeniedError",
                "message": "Unable to activate queue: normal: User permission denied"
            },
            "message": "Unable to activate queue: normal: User permission denied",
            "status": "FAIL"
        }

User Operations
---------------

User List
^^^^^^^^^

.. http:get:: users/

    Lists all users

    Example::

        {
            "data": [
                {
                    "cluster_type": "openlava",
                    "jobs": [],
                    "max_jobs": 2147483647,
                    "max_jobs_per_processor": 2147483648.0,
                    "max_slots": 2147483647,
                    "name": "default",
                    "num_pending_jobs": 0,
                    "num_pending_slots": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "User"
                },
                {
                    "cluster_type": "openlava",
                    "jobs": [],
                    "max_jobs": 2147483647,
                    "max_jobs_per_processor": 2147483648.0,
                    "max_slots": 2147483647,
                    "name": "irvined",
                    "num_pending_jobs": 0,
                    "num_pending_slots": 0,
                    "num_reserved_slots": 0,
                    "num_running_jobs": 0,
                    "num_running_slots": 0,
                    "num_suspended_jobs": 0,
                    "num_suspended_slots": 0,
                    "num_system_suspended_jobs": 0,
                    "num_system_suspended_slots": 0,
                    "num_user_suspended_jobs": 0,
                    "num_user_suspended_slots": 0,
                    "total_jobs": 0,
                    "total_slots": 0,
                    "type": "User"
                }
            ],
            "message": "",
            "status": "OK"
        }

Getting information on a User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: users/(string:user_name)

    Gets information on a specific user

    :param string user_name: The name of user

    Example::

        {
            "data": {
                "cluster_type": "openlava",
                "jobs": [],
                "max_jobs": 2147483647,
                "max_jobs_per_processor": 2147483648.0,
                "max_slots": 2147483647,
                "name": "default",
                "num_pending_jobs": 0,
                "num_pending_slots": 0,
                "num_reserved_slots": 0,
                "num_running_jobs": 0,
                "num_running_slots": 0,
                "num_suspended_jobs": 0,
                "num_suspended_slots": 0,
                "num_system_suspended_jobs": 0,
                "num_system_suspended_slots": 0,
                "num_user_suspended_jobs": 0,
                "num_user_suspended_slots": 0,
                "total_jobs": 0,
                "total_slots": 0,
                "type": "User"
            },
            "message": "",
            "status": "OK"
        }

Jobs
----

Getting information on a Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: jobs/(int:job_id)/$'

    Lists all array tasks for the specified job id

    :param int job_id: Numerical ID of the job

    Example::

        {
            "data": [
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 2,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "2532"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "34304"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "3"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 1415979417,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "/home/irvined",
                    "execution_home_directory": "/home/irvined",
                    "execution_hosts": [
                        {
                            "name": "master",
                            "num_slots": 1,
                            "type": "ExecutionHost",
                            "url": "/olweb/olw/hosts/master"
                        }
                    ],
                    "execution_user_id": 1000,
                    "execution_user_name": "irvined",
                    "host_specification": "master",
                    "input_file_name": "/dev/null",
                    "is_completed": true,
                    "is_failed": false,
                    "is_pending": false,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10289,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_a[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": "",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": 31241,
                    "processes": [
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31241,
                            "process_id": 31241,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31241,
                            "process_id": 31241,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31241,
                            "process_id": 31241,
                            "type": "Process"
                        }
                    ],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 1415979413,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 1415979403,
                    "status": {
                        "description": "The job has terminated with status 0.",
                        "friendly": "Completed",
                        "name": "JOB_STAT_DONE",
                        "status": 64,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979401,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 1,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "2532"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "34304"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "3"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 1415979417,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "/home/irvined",
                    "execution_home_directory": "/home/irvined",
                    "execution_hosts": [
                        {
                            "name": "master",
                            "num_slots": 1,
                            "type": "ExecutionHost",
                            "url": "/olweb/olw/hosts/master"
                        }
                    ],
                    "execution_user_id": 1000,
                    "execution_user_name": "irvined",
                    "host_specification": "master",
                    "input_file_name": "/dev/null",
                    "is_completed": true,
                    "is_failed": false,
                    "is_pending": false,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10289,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_a[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": "",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": 31240,
                    "processes": [
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31240,
                            "process_id": 31240,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31240,
                            "process_id": 31240,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31240,
                            "process_id": 31240,
                            "type": "Process"
                        }
                    ],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 1415979417,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 1415979403,
                    "status": {
                        "description": "The job has terminated with status 0.",
                        "friendly": "Completed",
                        "name": "JOB_STAT_DONE",
                        "status": 64,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979401,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 3,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "2524"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "34304"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "3"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 1415979433,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "/home/irvined",
                    "execution_home_directory": "/home/irvined",
                    "execution_hosts": [
                        {
                            "name": "master",
                            "num_slots": 1,
                            "type": "ExecutionHost",
                            "url": "/olweb/olw/hosts/master"
                        }
                    ],
                    "execution_user_id": 1000,
                    "execution_user_name": "irvined",
                    "host_specification": "master",
                    "input_file_name": "/dev/null",
                    "is_completed": true,
                    "is_failed": false,
                    "is_pending": false,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10289,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_a[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": "",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": 31293,
                    "processes": [
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31293,
                            "process_id": 31293,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31293,
                            "process_id": 31293,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31293,
                            "process_id": 31293,
                            "type": "Process"
                        }
                    ],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 1415979433,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 1415979423,
                    "status": {
                        "description": "The job has terminated with status 0.",
                        "friendly": "Completed",
                        "name": "JOB_STAT_DONE",
                        "status": 64,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979401,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 4,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "2528"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "34304"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "3"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 1415979433,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "/home/irvined",
                    "execution_home_directory": "/home/irvined",
                    "execution_hosts": [
                        {
                            "name": "master",
                            "num_slots": 1,
                            "type": "ExecutionHost",
                            "url": "/olweb/olw/hosts/master"
                        }
                    ],
                    "execution_user_id": 1000,
                    "execution_user_name": "irvined",
                    "host_specification": "master",
                    "input_file_name": "/dev/null",
                    "is_completed": true,
                    "is_failed": false,
                    "is_pending": false,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10289,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_a[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": "",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": 31294,
                    "processes": [
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31294,
                            "process_id": 31294,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31294,
                            "process_id": 31294,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31294,
                            "process_id": 31294,
                            "type": "Process"
                        }
                    ],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 1415979433,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 1415979423,
                    "status": {
                        "description": "The job has terminated with status 0.",
                        "friendly": "Completed",
                        "name": "JOB_STAT_DONE",
                        "status": 64,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979401,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 5,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "2528"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "34304"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "3"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 1415979453,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "/home/irvined",
                    "execution_home_directory": "/home/irvined",
                    "execution_hosts": [
                        {
                            "name": "master",
                            "num_slots": 1,
                            "type": "ExecutionHost",
                            "url": "/olweb/olw/hosts/master"
                        }
                    ],
                    "execution_user_id": 1000,
                    "execution_user_name": "irvined",
                    "host_specification": "master",
                    "input_file_name": "/dev/null",
                    "is_completed": true,
                    "is_failed": false,
                    "is_pending": false,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10289,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_a[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": "",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": 31330,
                    "processes": [
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31330,
                            "process_id": 31330,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31330,
                            "process_id": 31330,
                            "type": "Process"
                        },
                        {
                            "cray_job_id": 0,
                            "hostname": null,
                            "parent_process_id": 1033,
                            "process_group_id": 31330,
                            "process_id": 31330,
                            "type": "Process"
                        }
                    ],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 1415979453,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 1415979443,
                    "status": {
                        "description": "The job has terminated with status 0.",
                        "friendly": "Completed",
                        "name": "JOB_STAT_DONE",
                        "status": 64,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979401,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                }
            ],
            "message": "",
            "status": "OK"
        }

.. http:get:: job/(int:job_id)/(int:array_index)

    Gets information about a specific job.

    :param int job_id: Numerical ID of the job

    :param int array_index: Array index of the job.

    Example::

        {
            "data": {
                "admins": [
                    "irvined",
                    "openlava"
                ],
                "array_index": 2,
                "begin_time": 0,
                "checkpoint_directory": "",
                "checkpoint_period": 0,
                "cluster_type": "openlava",
                "command": "sleep 10",
                "consumed_resources": [
                    {
                        "limit": "-1",
                        "name": "Resident Memory",
                        "type": "ConsumedResource",
                        "unit": "KB",
                        "value": "2532"
                    },
                    {
                        "limit": "-1",
                        "name": "Virtual Memory",
                        "type": "ConsumedResource",
                        "unit": "KB",
                        "value": "34304"
                    },
                    {
                        "limit": "-1",
                        "name": "User Time",
                        "type": "ConsumedResource",
                        "unit": "None",
                        "value": "0:00:00"
                    },
                    {
                        "limit": "None",
                        "name": "System Time",
                        "type": "ConsumedResource",
                        "unit": "None",
                        "value": "0:00:00"
                    },
                    {
                        "limit": "None",
                        "name": "Num Active Processes",
                        "type": "ConsumedResource",
                        "unit": "Processes",
                        "value": "3"
                    }
                ],
                "cpu_factor": 0.0,
                "cpu_time": 0.0,
                "cwd": "",
                "dependency_condition": "",
                "email_user": "",
                "end_time": 1415979417,
                "error_file_name": "/dev/null",
                "execution_cwd": "/home/irvined",
                "execution_home_directory": "/home/irvined",
                "execution_hosts": [
                    {
                        "name": "master",
                        "num_slots": 1,
                        "type": "ExecutionHost",
                        "url": "/olweb/olw/hosts/master"
                    }
                ],
                "execution_user_id": 1000,
                "execution_user_name": "irvined",
                "host_specification": "master",
                "input_file_name": "/dev/null",
                "is_completed": true,
                "is_failed": false,
                "is_pending": false,
                "is_running": false,
                "is_suspended": false,
                "job_id": 10289,
                "login_shell": "",
                "max_requested_slots": 1,
                "name": "job_test_a[1-5]",
                "options": [
                    {
                        "description": "Submitted with a job name",
                        "friendly": "Job submitted with name",
                        "name": "SUB_JOB_NAME",
                        "status": 1,
                        "type": "SubmitOption"
                    },
                    {
                        "description": "",
                        "friendly": "Job submitted with queue",
                        "name": "SUB_QUEUE",
                        "status": 2,
                        "type": "SubmitOption"
                    },
                    {
                        "description": "",
                        "friendly": "Job submitted to project",
                        "name": "SUB_PROJECT_NAME",
                        "status": 33554432,
                        "type": "SubmitOption"
                    },
                    {
                        "description": "",
                        "friendly": "SUB_RESTART_FORCE",
                        "name": "SUB_RESTART_FORCE",
                        "status": 4096,
                        "type": "SubmitOption"
                    },
                    {
                        "description": "",
                        "friendly": "Job submitted with output file",
                        "name": "SUB_OUT_FILE",
                        "status": 16,
                        "type": "SubmitOption"
                    },
                    {
                        "description": "",
                        "friendly": "Job submitted with checkpoint period",
                        "name": "SUB_CHKPNT_PERIOD",
                        "status": 1024,
                        "type": "SubmitOption"
                    }
                ],
                "output_file_name": "/dev/null",
                "parent_group": "/",
                "pending_reasons": "",
                "pre_execution_command": "",
                "predicted_start_time": 0,
                "priority": -1,
                "process_id": 31241,
                "processes": [
                    {
                        "cray_job_id": 0,
                        "hostname": null,
                        "parent_process_id": 1033,
                        "process_group_id": 31241,
                        "process_id": 31241,
                        "type": "Process"
                    },
                    {
                        "cray_job_id": 0,
                        "hostname": null,
                        "parent_process_id": 1033,
                        "process_group_id": 31241,
                        "process_id": 31241,
                        "type": "Process"
                    },
                    {
                        "cray_job_id": 0,
                        "hostname": null,
                        "parent_process_id": 1033,
                        "process_group_id": 31241,
                        "process_id": 31241,
                        "type": "Process"
                    }
                ],
                "project_names": [
                    "default"
                ],
                "queue": {
                    "name": "normal",
                    "type": "Queue",
                    "url": "/olweb/olw/queues/normal"
                },
                "requested_hosts": [],
                "requested_resources": "",
                "requested_slots": 1,
                "reservation_time": 0,
                "resource_usage_last_update_time": 1415979413,
                "runtime_limits": [
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "CPU Time",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "File Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Data Segment Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Stack Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Core Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "RSS Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Num Files",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Max Open Files",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Swap Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Run Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Process Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    }
                ],
                "service_port": 0,
                "start_time": 1415979403,
                "status": {
                    "description": "The job has terminated with status 0.",
                    "friendly": "Completed",
                    "name": "JOB_STAT_DONE",
                    "status": 64,
                    "type": "JobStatus"
                },
                "submission_host": {
                    "name": "master",
                    "type": "Host",
                    "url": "/olweb/olw/hosts/master"
                },
                "submit_home_directory": "/home/irvined",
                "submit_time": 1415979401,
                "suspension_reasons": " Unknown suspending reason code: 0",
                "termination_signal": 0,
                "termination_time": 0,
                "type": "Job",
                "user_name": "irvined",
                "user_priority": -1,
                "was_killed": false
            },
            "message": "",
            "status": "OK"
        }

.. http:get:: job/(int:job_id)/(int:array_index)/output

    Returns the output of the job as plain text. If there is no output returns Not Available.

    :param int job_id: Numerical ID of the job

    :param int array_index: Array index of the job.

    Example::

        Rank: 0: Hello World!
        Rank: 2: Hello World!
        Rank: 1: Hello World!

.. http:get:: job/(int:job_id)/(int:array_index)/error

    Returns the standard error output from the job

    :param int job_id: Numerical ID of the job

    :param int array_index: Array index of the job.

    Example::

        Not Available

Listing all jobs
^^^^^^^^^^^^^^^^

.. http:get:: jobs/

    Lists all jobs

    Example::

        {
            "data": [
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 3,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10289,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_a[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979401,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 4,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10289,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_a[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979401,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 5,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10289,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_a[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979401,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 1,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10290,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_b[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979404,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 2,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10290,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_b[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979404,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 3,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10290,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_b[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979404,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 4,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10290,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_b[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979404,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 5,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10290,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_b[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979404,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 1,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10291,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_c[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979407,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 2,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10291,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_c[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979407,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 3,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10291,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_c[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979407,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 4,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10291,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_c[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979407,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                },
                {
                    "admins": [
                        "irvined",
                        "openlava"
                    ],
                    "array_index": 5,
                    "begin_time": 0,
                    "checkpoint_directory": "",
                    "checkpoint_period": 0,
                    "cluster_type": "openlava",
                    "command": "sleep 10",
                    "consumed_resources": [
                        {
                            "limit": "-1",
                            "name": "Resident Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "Virtual Memory",
                            "type": "ConsumedResource",
                            "unit": "KB",
                            "value": "0"
                        },
                        {
                            "limit": "-1",
                            "name": "User Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "System Time",
                            "type": "ConsumedResource",
                            "unit": "None",
                            "value": "0:00:00"
                        },
                        {
                            "limit": "None",
                            "name": "Num Active Processes",
                            "type": "ConsumedResource",
                            "unit": "Processes",
                            "value": "0"
                        }
                    ],
                    "cpu_factor": 0.0,
                    "cpu_time": 0.0,
                    "cwd": "",
                    "dependency_condition": "",
                    "email_user": "",
                    "end_time": 0,
                    "error_file_name": "/dev/null",
                    "execution_cwd": "",
                    "execution_home_directory": "",
                    "execution_hosts": [],
                    "execution_user_id": -1,
                    "execution_user_name": "",
                    "host_specification": "",
                    "input_file_name": "/dev/null",
                    "is_completed": false,
                    "is_failed": false,
                    "is_pending": true,
                    "is_running": false,
                    "is_suspended": false,
                    "job_id": 10291,
                    "login_shell": "",
                    "max_requested_slots": 1,
                    "name": "job_test_c[1-5]",
                    "options": [
                        {
                            "description": "Submitted with a job name",
                            "friendly": "Job submitted with name",
                            "name": "SUB_JOB_NAME",
                            "status": 1,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with queue",
                            "name": "SUB_QUEUE",
                            "status": 2,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted to project",
                            "name": "SUB_PROJECT_NAME",
                            "status": 33554432,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "SUB_RESTART_FORCE",
                            "name": "SUB_RESTART_FORCE",
                            "status": 4096,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with output file",
                            "name": "SUB_OUT_FILE",
                            "status": 16,
                            "type": "SubmitOption"
                        },
                        {
                            "description": "",
                            "friendly": "Job submitted with checkpoint period",
                            "name": "SUB_CHKPNT_PERIOD",
                            "status": 1024,
                            "type": "SubmitOption"
                        }
                    ],
                    "output_file_name": "/dev/null",
                    "parent_group": "/",
                    "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                    "pre_execution_command": "",
                    "predicted_start_time": 0,
                    "priority": -1,
                    "process_id": -1,
                    "processes": [],
                    "project_names": [
                        "default"
                    ],
                    "queue": {
                        "name": "normal",
                        "type": "Queue",
                        "url": "/olweb/olw/queues/normal"
                    },
                    "requested_hosts": [],
                    "requested_resources": "",
                    "requested_slots": 1,
                    "reservation_time": 0,
                    "resource_usage_last_update_time": 0,
                    "runtime_limits": [
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "CPU Time",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "File Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Data Segment Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Stack Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Core Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "RSS Size",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Num Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Max Open Files",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Swap Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "KB"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Run Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        },
                        {
                            "description": "None",
                            "hard_limit": "-1",
                            "name": "Process Limit",
                            "soft_limit": "-1",
                            "type": "ResourceLimit",
                            "unit": "None"
                        }
                    ],
                    "service_port": 0,
                    "start_time": 0,
                    "status": {
                        "description": "The job is pending, i.e., it has not been dispatched yet.",
                        "friendly": "Pending",
                        "name": "JOB_STAT_PEND",
                        "status": 1,
                        "type": "JobStatus"
                    },
                    "submission_host": {
                        "name": "master",
                        "type": "Host",
                        "url": "/olweb/olw/hosts/master"
                    },
                    "submit_home_directory": "/home/irvined",
                    "submit_time": 1415979407,
                    "suspension_reasons": " Unknown suspending reason code: 0",
                    "termination_signal": 0,
                    "termination_time": 0,
                    "type": "Job",
                    "user_name": "irvined",
                    "user_priority": -1,
                    "was_killed": false
                }
            ],
            "message": "",
            "status": "OK"
        }
Submitting a new job
^^^^^^^^^^^^^^^^^^^^

.. http:post:: job/submit/(string:form_class)

    Submits a new job.

    :param string form_class:

        The name of an optional submit form processing class.

    :jsonparam options:

        Numeric value to pass to the options of the scheduler.

    :jsonparam options2:

        Numeric value to pass to the options2 field of the scheduler.

    :jsonparam requested_slots:

        The number of slots to use (Minimum value.) Default is 1.

    :jsonparam command:

        The command to execute

    :jsonparam job_name:

        The name of the job.  If none, then no name is used.

    :jsonparam queue_name:

        The name of the queue to submit the job into, if none, the default queue is used.

    :jsonparam requested_hosts:

        A string containing the list of hosts separated by a space that the user wishes the job to run on.

    :jsonparam resource_request:

        A string containing the resource request criteria.

    :jsonparam host_specification:

        A string defining the host specification that must be used

    :jsonparam dependency_conditions:

        A string defining the dependency conditions

    :jsonparam signal_value:

        The signal value to send to the job when its termination deadline is reached.

    :jsonparam input_file:

        Job input file to use.

    :jsonparam output_file:

        Job output file to use.

    :jsonparam error_file:

        Job error file to use.

    :jsonparam checkpoint_period:

        Number of seconds in between checkpoint operations

    :jsonparam checkpoint_directory:

        Directory to store checkpoint data

    :jsonparam email_user:

        Email address to send job updates to.

    :jsonparam project_name:

        Name of project to submit to

    :jsonparam max_requested_slots:

        Max number of slots to use

    :jsonparam login_shell:

        Login shell to use

    :jsonparam user_priority:

        User given priority for the job.

    Example POST data::

        {
            "command": "sleep 100",
            "max_requested_slots": 1,
            "options": 0,
            "options2": 0,
            "requested_slots": 1
        }

    Example Response::

        [
            {
                "admins": [
                    "irvined",
                    "openlava"
                ],
                "array_index": 0,
                "begin_time": 0,
                "checkpoint_directory": "",
                "checkpoint_period": 0,
                "cluster_type": "openlava",
                "command": "sleep 100",
                "consumed_resources": [
                    {
                        "limit": "-1",
                        "name": "Resident Memory",
                        "type": "ConsumedResource",
                        "unit": "KB",
                        "value": "0"
                    },
                    {
                        "limit": "-1",
                        "name": "Virtual Memory",
                        "type": "ConsumedResource",
                        "unit": "KB",
                        "value": "0"
                    },
                    {
                        "limit": "-1",
                        "name": "User Time",
                        "type": "ConsumedResource",
                        "unit": "None",
                        "value": "0:00:00"
                    },
                    {
                        "limit": "None",
                        "name": "System Time",
                        "type": "ConsumedResource",
                        "unit": "None",
                        "value": "0:00:00"
                    },
                    {
                        "limit": "None",
                        "name": "Num Active Processes",
                        "type": "ConsumedResource",
                        "unit": "Processes",
                        "value": "0"
                    }
                ],
                "cpu_factor": 0.0,
                "cpu_time": 0.0,
                "cwd": "development",
                "dependency_condition": "",
                "email_user": "",
                "end_time": 0,
                "error_file_name": "/dev/null",
                "execution_cwd": "",
                "execution_home_directory": "",
                "execution_hosts": [],
                "execution_user_id": -1,
                "execution_user_name": "",
                "host_specification": "",
                "input_file_name": "/dev/null",
                "is_completed": false,
                "is_failed": false,
                "is_pending": true,
                "is_running": false,
                "is_suspended": false,
                "job_id": 10410,
                "login_shell": "",
                "max_requested_slots": 1,
                "name": "sleep 100",
                "options": [
                    {
                        "description": "",
                        "friendly": "Job submitted with queue",
                        "name": "SUB_QUEUE",
                        "status": 2,
                        "type": "SubmitOption"
                    },
                    {
                        "description": "",
                        "friendly": "Job submitted to project",
                        "name": "SUB_PROJECT_NAME",
                        "status": 33554432,
                        "type": "SubmitOption"
                    },
                    {
                        "description": "",
                        "friendly": "Job submitted with output file",
                        "name": "SUB_OUT_FILE",
                        "status": 16,
                        "type": "SubmitOption"
                    }
                ],
                "output_file_name": "/dev/null",
                "parent_group": "/",
                "pending_reasons": " Load information unavailable: 5 hosts;  Job slot limit reached: 1 host;",
                "pre_execution_command": "",
                "predicted_start_time": 0,
                "priority": -1,
                "process_id": -1,
                "processes": [],
                "project_names": [
                    "default"
                ],
                "queue": {
                    "name": "normal",
                    "type": "Queue",
                    "url": "/olweb/olw/queues/normal"
                },
                "requested_hosts": [],
                "requested_resources": "",
                "requested_slots": 1,
                "reservation_time": 0,
                "resource_usage_last_update_time": 0,
                "runtime_limits": [
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "CPU Time",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "File Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Data Segment Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Stack Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Core Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "RSS Size",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Num Files",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Max Open Files",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Swap Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "KB"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Run Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    },
                    {
                        "description": "None",
                        "hard_limit": "-1",
                        "name": "Process Limit",
                        "soft_limit": "-1",
                        "type": "ResourceLimit",
                        "unit": "None"
                    }
                ],
                "service_port": 0,
                "start_time": 0,
                "status": {
                    "description": "The job is pending, i.e., it has not been dispatched yet.",
                    "friendly": "Pending",
                    "name": "JOB_STAT_PEND",
                    "status": 1,
                    "type": "JobStatus"
                },
                "submission_host": {
                    "name": "master",
                    "type": "Host",
                    "url": "/olweb/olw/hosts/master"
                },
                "submit_home_directory": "/home/irvined",
                "submit_time": 1416128839,
                "suspension_reasons": " Unknown suspending reason code: 0",
                "termination_signal": 0,
                "termination_time": 0,
                "type": "Job",
                "user_name": "irvined",
                "user_priority": -1,
                "was_killed": false
            }
        ]


Killing an existing job
^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: job/(int:job_id)/(int:array_index)/kill

    Kills the job

    :param int job_id: Numerical ID of the job

    :param int array_index: Array index of the job.

    Example::

        {
            "data": {
                "exception_class": "ClusterException",
                "message": "Unable to kill job: 10399[0]: Job has already finished"
            },
            "message": "Unable to kill job: 10399[0]: Job has already finished",
            "status": "FAIL"
        }

Suspending and Resuming Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: job/(int:job_id)/(int:array_index)/suspend

    Suspends the job

    :param int job_id: Numerical ID of the job

    :param int array_index: Array index of the job.

    Example::

        {
            "data": null,
            "message": "Job suspended",
            "status": "OK"
        }

.. http:get:: job/(int:job_id)/(int:array_index)/resume

    Resumes the job

    :param int job_id: Numerical ID of the job

    :param int array_index: Array index of the job.

    Example::

        {
            "data": null,
            "message": "Job Resumed",
            "status": "OK"
        }

Requeing a job
^^^^^^^^^^^^^^

.. http:get:: job/(int:job_id)/(int:array_index)/requeue

    Requeues the job

    :param int job_id: Numerical ID of the job

    :param int array_index: Array index of the job.

    :query bool hold: If true, the job will be held in the pending state.

    Example::

        {
            "data": null,
            "message": "Job Requeued",
            "status": "OK"
        }

Overviews
---------

Host State
^^^^^^^^^^

.. http:get:: overview/hosts

Returns an overview of host state.  The format is designed with [nv]d3 in mind, and can easily be used to create
a chart of the data.

Only data fields that are in use are returned.

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

Returns an overview of job utilization.  The format is designed with [nv]d3 in mind, and can easily be used to create
a chart of the data.

Only data fields that are in use are returned.

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

Returns an overview of slot utilization.  The format is designed with [nv]d3 in mind, and can easily be used to create
a chart of the data.

Only data fields that are in use are returned.

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

