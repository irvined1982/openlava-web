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

        [    0.000000] Initializing cgroup subsys cpuset
        [    0.000000] Initializing cgroup subsys cpu
        [    0.000000] Linux version 3.2.0-53-generic (buildd@allspice) (gcc version 4.6.3 (Ubuntu/Linaro 4.6.3-1ubuntu5) ) #81-Ubuntu SMP Thu Aug 22 21:01:03 UTC 2013 (Ubuntu 3.2.0-53.81-generic 3.2.50)
        [    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-3.2.0-53-generic root=UUID=fba50614-f422-4d4d-8603-132359ae7971 ro splash quiet vt.handoff=7
        [    0.000000] KERNEL supported cpus:
        [    0.000000]   Intel GenuineIntel
        [    0.000000]   AMD AuthenticAMD
        [    0.000000]   Centaur CentaurHauls
        [    0.000000] Disabled fast string operations
        [    0.000000] BIOS-provided physical RAM map:
        [    0.000000]  BIOS-e820: 0000000000000000 - 000000000009fc00 (usable)
        [    0.000000]  BIOS-e820: 000000000009fc00 - 00000000000a0000 (reserved)
        [    0.000000]  BIOS-e820: 00000000000dc000 - 0000000000100000 (reserved)
        [    0.000000]  BIOS-e820: 0000000000100000 - 000000003fff0000 (usable)
        [    0.000000]  BIOS-e820: 000000003fff0000 - 000000003ffff000 (ACPI data)
        [    0.000000]  BIOS-e820: 000000003ffff000 - 0000000040000000 (ACPI NVS)
        [    0.000000]  BIOS-e820: 00000000fd000000 - 00000000fd800000 (reserved)
        [    0.000000]  BIOS-e820: 00000000fec00000 - 00000000fec01000 (reserved)
        [    0.000000]  BIOS-e820: 00000000fee00000 - 00000000fee01000 (reserved)
        [    0.000000]  BIOS-e820: 00000000ffc00000 - 0000000100000000 (reserved)
        [    0.000000] NX (Execute Disable) protection: active
        [    0.000000] SMBIOS 2.7 present.
        [    0.000000] DMI: Parallels Software International Inc. Parallels Virtual Platform/Parallels Virtual Platform, BIOS 9.0.24251.1052177 Thu, 28 Aug 2014 15:04:13
        [    0.000000] e820 update range: 0000000000000000 - 0000000000010000 (usable) ==> (reserved)
        [    0.000000] e820 remove range: 00000000000a0000 - 0000000000100000 (usable)
        [    0.000000] No AGP bridge found
        [    0.000000] last_pfn = 0x3fff0 max_arch_pfn = 0x400000000
        [    0.000000] MTRR default type: uncachable
        [    0.000000] MTRR fixed ranges enabled:
        [    0.000000]   00000-9FFFF write-back
        [    0.000000]   A0000-BFFFF uncachable
        [    0.000000]   C0000-C7FFF write-protect
        [    0.000000]   C8000-EFFFF uncachable
        [    0.000000]   F0000-FFFFF write-protect
        [    0.000000] MTRR variable ranges enabled:
        [    0.000000]   0 base 000000000 mask FC0000000 write-back
        [    0.000000]   1 disabled
        [    0.000000]   2 disabled
        [    0.000000]   3 disabled
        [    0.000000]   4 disabled
        [    0.000000]   5 disabled
        [    0.000000]   6 disabled
        [    0.000000]   7 disabled
        [    0.000000] x86 PAT enabled: cpu 0, old 0x7040600070406, new 0x7010600070106
        [    0.000000] found SMP MP-table at [ffff8800000ff100] ff100
        [    0.000000] initial memory mapped : 0 - 20000000
        [    0.000000] Base memory trampoline at [ffff88000009a000] 9a000 size 20480
        [    0.000000] init_memory_mapping: 0000000000000000-000000003fff0000
        [    0.000000]  0000000000 - 003fe00000 page 2M
        [    0.000000]  003fe00000 - 003fff0000 page 4k
        [    0.000000] kernel direct mapping tables up to 3fff0000 @ 1fffd000-20000000
        [    0.000000] RAMDISK: 364c2000 - 37259000
        [    0.000000] ACPI: RSDP 00000000000e8000 00024 (v02 PRLS  )
        [    0.000000] ACPI: XSDT 000000003fff0040 00044 (v01 PRLS   PRLS_OEM 00000001 INTL 20051216)
        [    0.000000] ACPI: FACP 000000003fff0140 000F4 (v03 PRLS   PRLS_OEM 00000001 INTL 20051216)
        [    0.000000] ACPI: DSDT 000000003fff04c0 04364 (v02 PRLS   PRLSACPI 00001001 INTL 20051216)
        [    0.000000] ACPI: FACS 000000003fff0240 00040
        [    0.000000] ACPI: APIC 000000003fff0280 00216 (v01 PRLS   PRLS_OEM 00000001 INTL 20051216)
        [    0.000000] ACPI: HPET 000000003fff4840 00038 (v00 PRLS   PRLS_OEM 00000001 INTL 20051216)
        [    0.000000] ACPI: MCFG 000000003fff4880 0003C (v01 PRLS   PRLS_OEM 00000001 INTL 20051216)
        [    0.000000] ACPI: Local APIC address 0xfee00000
        [    0.000000] No NUMA configuration found
        [    0.000000] Faking a node at 0000000000000000-000000003fff0000
        [    0.000000] Initmem setup node 0 0000000000000000-000000003fff0000
        [    0.000000]   NODE_DATA [000000003ffeb000 - 000000003ffeffff]
        [    0.000000] kvm-clock: Using msrs 4b564d01 and 4b564d00
        [    0.000000] kvm-clock: cpu 0, msr 0:1cfa741, boot clock
        [    1.118967]  [ffffea0000000000-ffffea0000ffffff] PMD -> [ffff88003e600000-ffff88003f5fffff] on node 0
        [    1.118971] Zone PFN ranges:
        [    1.118973]   DMA      0x00000010 -> 0x00001000
        [    1.118975]   DMA32    0x00001000 -> 0x00100000
        [    1.118977]   Normal   empty
        [    1.118979] Movable zone start PFN for each node
        [    1.118981] early_node_map[2] active PFN ranges
        [    1.118983]     0: 0x00000010 -> 0x0000009f
        [    1.118985]     0: 0x00000100 -> 0x0003fff0
        [    1.118988] On node 0 totalpages: 262015
        [    1.118990]   DMA zone: 64 pages used for memmap
        [    1.118992]   DMA zone: 5 pages reserved
        [    1.118994]   DMA zone: 3914 pages, LIFO batch:0
        [    1.118998]   DMA32 zone: 4032 pages used for memmap
        [    1.119001]   DMA32 zone: 254000 pages, LIFO batch:31
        [    1.119005] ACPI: PM-Timer IO Port: 0x4008
        [    1.119009] ACPI: Local APIC address 0xfee00000
        [    1.119013] ACPI: LAPIC (acpi_id[0x00] lapic_id[0x00] enabled)
        [    1.119016] ACPI: LAPIC (acpi_id[0x01] lapic_id[0x01] disabled)
        [    1.119018] ACPI: LAPIC (acpi_id[0x02] lapic_id[0x02] disabled)
        [    1.119020] ACPI: LAPIC (acpi_id[0x03] lapic_id[0x03] disabled)
        [    1.119022] ACPI: LAPIC (acpi_id[0x04] lapic_id[0x04] disabled)
        [    1.119024] ACPI: LAPIC (acpi_id[0x05] lapic_id[0x05] disabled)
        [    1.119025] ACPI: LAPIC (acpi_id[0x06] lapic_id[0x06] disabled)
        [    1.119027] ACPI: LAPIC (acpi_id[0x07] lapic_id[0x07] disabled)
        [    1.119029] ACPI: LAPIC (acpi_id[0x08] lapic_id[0x08] disabled)
        [    1.119031] ACPI: LAPIC (acpi_id[0x09] lapic_id[0x09] disabled)
        [    1.119033] ACPI: LAPIC (acpi_id[0x0a] lapic_id[0x0a] disabled)
        [    1.119035] ACPI: LAPIC (acpi_id[0x0b] lapic_id[0x0b] disabled)
        [    1.119037] ACPI: LAPIC (acpi_id[0x0c] lapic_id[0x0c] disabled)
        [    1.119038] ACPI: LAPIC (acpi_id[0x0d] lapic_id[0x0d] disabled)
        [    1.119040] ACPI: LAPIC (acpi_id[0x0e] lapic_id[0x0e] disabled)
        [    1.119042] ACPI: LAPIC (acpi_id[0x0f] lapic_id[0x0f] disabled)
        [    1.119044] ACPI: LAPIC (acpi_id[0x10] lapic_id[0x10] disabled)
        [    1.119046] ACPI: LAPIC (acpi_id[0x11] lapic_id[0x11] disabled)
        [    1.119048] ACPI: LAPIC (acpi_id[0x12] lapic_id[0x12] disabled)
        [    1.119049] ACPI: LAPIC (acpi_id[0x13] lapic_id[0x13] disabled)
        [    1.119051] ACPI: LAPIC (acpi_id[0x14] lapic_id[0x14] disabled)
        [    1.119053] ACPI: LAPIC (acpi_id[0x15] lapic_id[0x15] disabled)
        [    1.119055] ACPI: LAPIC (acpi_id[0x16] lapic_id[0x16] disabled)
        [    1.119057] ACPI: LAPIC (acpi_id[0x17] lapic_id[0x17] disabled)
        [    1.119059] ACPI: LAPIC (acpi_id[0x18] lapic_id[0x18] disabled)
        [    1.119061] ACPI: LAPIC (acpi_id[0x19] lapic_id[0x19] disabled)
        [    1.119062] ACPI: LAPIC (acpi_id[0x1a] lapic_id[0x1a] disabled)
        [    1.119064] ACPI: LAPIC (acpi_id[0x1b] lapic_id[0x1b] disabled)
        [    1.119066] ACPI: LAPIC (acpi_id[0x1c] lapic_id[0x1c] disabled)
        [    1.119068] ACPI: LAPIC (acpi_id[0x1d] lapic_id[0x1d] disabled)
        [    1.119070] ACPI: LAPIC (acpi_id[0x1e] lapic_id[0x1e] disabled)
        [    1.119072] ACPI: LAPIC (acpi_id[0x1f] lapic_id[0x1f] disabled)
        [    1.119076] ACPI: LAPIC_NMI (acpi_id[0x00] high edge lint[0x1])
        [    1.119078] ACPI: LAPIC_NMI (acpi_id[0x01] high edge lint[0x1])
        [    1.119079] ACPI: LAPIC_NMI (acpi_id[0x02] high edge lint[0x1])
        [    1.119081] ACPI: LAPIC_NMI (acpi_id[0x03] high edge lint[0x1])
        [    1.119083] ACPI: LAPIC_NMI (acpi_id[0x04] high edge lint[0x1])
        [    1.119085] ACPI: LAPIC_NMI (acpi_id[0x05] high edge lint[0x1])
        [    1.119087] ACPI: LAPIC_NMI (acpi_id[0x06] high edge lint[0x1])
        [    1.119089] ACPI: LAPIC_NMI (acpi_id[0x07] high edge lint[0x1])
        [    1.119091] ACPI: LAPIC_NMI (acpi_id[0x08] high edge lint[0x1])
        [    1.119093] ACPI: LAPIC_NMI (acpi_id[0x09] high edge lint[0x1])
        [    1.119094] ACPI: LAPIC_NMI (acpi_id[0x0a] high edge lint[0x1])
        [    1.119096] ACPI: LAPIC_NMI (acpi_id[0x0b] high edge lint[0x1])
        [    1.119098] ACPI: LAPIC_NMI (acpi_id[0x0c] high edge lint[0x1])
        [    1.119100] ACPI: LAPIC_NMI (acpi_id[0x0d] high edge lint[0x1])
        [    1.119102] ACPI: LAPIC_NMI (acpi_id[0x0e] high edge lint[0x1])
        [    1.119104] ACPI: LAPIC_NMI (acpi_id[0x0f] high edge lint[0x1])
        [    1.119106] ACPI: LAPIC_NMI (acpi_id[0x10] high edge lint[0x1])
        [    1.119107] ACPI: LAPIC_NMI (acpi_id[0x11] high edge lint[0x1])
        [    1.119109] ACPI: LAPIC_NMI (acpi_id[0x12] high edge lint[0x1])
        [    1.119111] ACPI: LAPIC_NMI (acpi_id[0x13] high edge lint[0x1])
        [    1.119113] ACPI: LAPIC_NMI (acpi_id[0x14] high edge lint[0x1])
        [    1.119115] ACPI: LAPIC_NMI (acpi_id[0x15] high edge lint[0x1])
        [    1.119117] ACPI: LAPIC_NMI (acpi_id[0x16] high edge lint[0x1])
        [    1.119119] ACPI: LAPIC_NMI (acpi_id[0x17] high edge lint[0x1])
        [    1.119120] ACPI: LAPIC_NMI (acpi_id[0x18] high edge lint[0x1])
        [    1.119122] ACPI: LAPIC_NMI (acpi_id[0x19] high edge lint[0x1])
        [    1.119124] ACPI: LAPIC_NMI (acpi_id[0x1a] high edge lint[0x1])
        [    1.119126] ACPI: LAPIC_NMI (acpi_id[0x1b] high edge lint[0x1])
        [    1.119128] ACPI: LAPIC_NMI (acpi_id[0x1c] high edge lint[0x1])
        [    1.119130] ACPI: LAPIC_NMI (acpi_id[0x1d] high edge lint[0x1])
        [    1.119131] ACPI: LAPIC_NMI (acpi_id[0x1e] high edge lint[0x1])
        [    1.119133] ACPI: LAPIC_NMI (acpi_id[0x1f] high edge lint[0x1])
        [    1.119136] ACPI: IOAPIC (id[0x00] address[0xfec00000] gsi_base[0])
        [    1.119140] IOAPIC[0]: apic_id 0, version 2, address 0xfec00000, GSI 0-23
        [    1.119143] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
        [    1.119146] ACPI: INT_SRC_OVR (bus 0 bus_irq 14 global_irq 14 dfl edge)
        [    1.119148] ACPI: INT_SRC_OVR (bus 0 bus_irq 15 global_irq 15 dfl edge)
        [    1.119151] ACPI: IRQ0 used by override.
        [    1.119152] ACPI: IRQ2 used by override.
        [    1.119155] ACPI: IRQ9 used by override.
        [    1.119157] ACPI: IRQ14 used by override.
        [    1.119159] ACPI: IRQ15 used by override.
        [    1.119161] Using ACPI (MADT) for SMP configuration information
        [    1.119164] ACPI: HPET id: 0x8086a701 base: 0xfed00000
        [    1.119168] SMP: Allowing 32 CPUs, 31 hotplug CPUs
        [    1.119172] nr_irqs_gsi: 40
        [    1.119176] PM: Registered nosave memory: 000000000009f000 - 00000000000a0000
        [    1.119178] PM: Registered nosave memory: 00000000000a0000 - 00000000000dc000
        [    1.119180] PM: Registered nosave memory: 00000000000dc000 - 0000000000100000
        [    1.119183] Allocating PCI resources starting at 40000000 (gap: 40000000:bd000000)
        [    1.119186] Booting paravirtualized kernel on KVM
        [    1.119190] setup_percpu: NR_CPUS:256 nr_cpumask_bits:256 nr_cpu_ids:32 nr_node_ids:1
        [    1.119194] PERCPU: Embedded 28 pages/cpu @ffff88003e200000 s83136 r8192 d23360 u131072
        [    1.119198] pcpu-alloc: s83136 r8192 d23360 u131072 alloc=1*2097152
        [    1.119201] pcpu-alloc: [0] 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15
        [    1.119205] pcpu-alloc: [0] 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
        [    1.119209] kvm-clock: cpu 0, msr 0:3e213741, primary cpu clock
        [    1.119213] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 257914
        [    1.119215] Policy zone: DMA32
        [    1.119218] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-3.2.0-53-generic root=UUID=fba50614-f422-4d4d-8603-132359ae7971 ro splash quiet vt.handoff=7
        [    1.119222] PID hash table entries: 4096 (order: 3, 32768 bytes)
        [    1.119226] xsave/xrstor: enabled xstate_bv 0x7, cntxt size 0x340
        [    1.119230] Checking aperture...
        [    1.119234] No AGP bridge found
        [    1.119238] Calgary: detecting Calgary via BIOS EBDA area
        [    1.119241] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
        [    1.119245] Memory: 998348k/1048512k available (6584k kernel code, 452k absent, 49712k reserved, 6622k data, 924k init)
        [    1.119261] SLUB: Genslabs=15, HWalign=64, Order=0-3, MinObjects=0, CPUs=32, Nodes=1
        [    1.119278] Hierarchical RCU implementation.
        [    1.119280] 	RCU dyntick-idle grace-period acceleration is enabled.
        [    1.119284] NR_IRQS:16640 nr_irqs:936 16
        [    1.119304] vt handoff: transparent VT on vt#7
        [    1.119308] Console: colour dummy device 80x25
        [    1.119312] console [tty0] enabled
        [    1.122307] allocated 8388608 bytes of page_cgroup
        [    1.122311] please try 'cgroup_disable=memory' option if you don't want memory cgroups
        [    1.123225] hpet clockevent registered
        [    1.123229] Detected 2800.000 MHz processor.
        [    1.123286] Calibrating delay loop (skipped) preset value.. 5600.00 BogoMIPS (lpj=11200000)
        [    1.123289] pid_max: default: 32768 minimum: 301
        [    1.123293] Security Framework initialized
        [    1.123301] AppArmor: AppArmor initialized
        [    1.123303] Yama: becoming mindful.
        [    1.123315] Dentry cache hash table entries: 131072 (order: 8, 1048576 bytes)
        [    1.123319] Inode-cache hash table entries: 65536 (order: 7, 524288 bytes)
        [    1.123323] Mount-cache hash table entries: 256
        [    1.123353] Initializing cgroup subsys cpuacct
        [    1.123357] Initializing cgroup subsys memory
        [    1.123361] Initializing cgroup subsys devices
        [    1.123363] Initializing cgroup subsys freezer
        [    1.123365] Initializing cgroup subsys blkio
        [    1.123371] Initializing cgroup subsys perf_event
        [    1.124980] Disabled fast string operations
        [    1.124983] CPU: Physical Processor ID: 0
        [    1.125017] mce: CPU supports 0 MCE banks
        [    1.125064] SMP alternatives: switching to UP code
        [    1.127735] ACPI: Core revision 20110623
        [    1.130336] ftrace: allocating 26592 entries in 105 pages
        [    1.131233] Enabling x2apic
        [    1.131237] Enabled x2apic
        [    1.131241] Switched APIC routing to physical x2apic.
        [    1.139363] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
        [    1.139365] CPU0: Intel(R) Core(TM) i7-2640M CPU @ 2.80GHz stepping 07
        [    1.247248] Performance Events: unsupported p6 CPU model 42 no PMU driver, software events only.
        [    1.247845] NMI watchdog disabled (cpu0): hardware events not enabled
        [    1.247863] Brought up 1 CPUs
        [    1.247866] Total of 1 processors activated (5600.00 BogoMIPS).
        [    1.248479] devtmpfs: initialized
        [    1.249008] EVM: security.selinux
        [    1.249010] EVM: security.SMACK64
        [    1.249012] EVM: security.capability
        [    1.249039] PM: Registering ACPI NVS region at 3ffff000 (4096 bytes)
        [    1.249556] print_constraints: dummy:
        [    1.249564] RTC time:  7:37:35, date: 11/16/14
        [    1.249572] NET: Registered protocol family 16
        [    1.249592] ACPI: bus type pci registered
        [    1.249600] PCI: MMCONFIG for domain 0000 [bus 00-0f] at [mem 0xfc000000-0xfcffffff] (base 0xfc000000)
        [    1.249603] PCI: not using MMCONFIG
        [    1.249606] PCI: Using configuration type 1 for base access
        [    1.249751] bio: create slab <bio-0> at 0
        [    1.249785] ACPI: Added _OSI(Module Device)
        [    1.249788] ACPI: Added _OSI(Processor Device)
        [    1.249790] ACPI: Added _OSI(3.0 _SCP Extensions)
        [    1.249792] ACPI: Added _OSI(Processor Aggregator Device)
        [    1.252713] ACPI: EC: Look up EC in DSDT
        [    1.253719] ACPI: Executed 1 blocks of module-level executable AML code
        [    1.267752] ACPI: Interpreter enabled
        [    1.267756] ACPI: (supports S0 S1 S3 S4 S5)
        [    1.267760] ACPI: Using IOAPIC for interrupt routing
        [    1.267764] PCI: MMCONFIG for domain 0000 [bus 00-0f] at [mem 0xfc000000-0xfcffffff] (base 0xfc000000)
        [    1.267768] PCI: MMCONFIG at [mem 0xfc000000-0xfcffffff] reserved in ACPI motherboard resources
        [    1.313449] ACPI: EC: GPE = 0xa, I/O: command/status = 0x66, data = 0x62
        [    1.313453] ACPI: No dock devices found.
        [    1.313455] HEST: Table not found.
        [    1.313458] PCI: Ignoring host bridge windows from ACPI; if necessary, use "pci=use_crs" and report a bug
        [    1.313466] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-7f])
        [    1.313478] pci_root PNP0A08:00: host bridge window [io  0x0000-0x0cf7] (ignored)
        [    1.313480] pci_root PNP0A08:00: host bridge window [io  0x0d00-0xffff] (ignored)
        [    1.313483] pci_root PNP0A08:00: host bridge window [mem 0x000a0000-0x000bffff] (ignored)
        [    1.313485] pci_root PNP0A08:00: host bridge window [mem 0x000d0000-0x000dffff] (ignored)
        [    1.313487] pci_root PNP0A08:00: host bridge window [mem 0x000c0000-0x000cffff] (ignored)
        [    1.313490] pci_root PNP0A08:00: host bridge window [mem 0xb0000000-0xfbffffff] (ignored)
        [    1.313492] pci_root PNP0A08:00: host bridge window [mem 0xfd000000-0xfd7fffff] (ignored)
        [    1.313496] pci 0000:00:00.0: [8086:29a0] type 0 class 0x000600
        [    1.313500] pci 0000:00:01.0: [8086:2981] type 1 class 0x000604
        [    1.313504] pci 0000:00:01.0: PME# supported from D0 D3hot D3cold
        [    1.313508] pci 0000:00:01.0: PME# disabled
        [    1.313512] pci 0000:00:03.0: [1ab8:4000] type 0 class 0x00ff00
        [    1.313516] pci 0000:00:03.0: reg 10: [io  0x8000-0x801f]
        [    1.313520] pci 0000:00:05.0: [1af4:1000] type 0 class 0x000200
        [    1.313524] pci 0000:00:05.0: reg 10: [io  0x8200-0x823f]
        [    1.313528] pci 0000:00:05.0: reg 14: [mem 0xee000000-0xee000fff]
        [    1.313532] pci 0000:00:0a.0: [1011:0022] type 1 class 0x000604
        [    1.314037] pci 0000:00:0e.0: [1af4:1002] type 0 class 0x000500
        [    1.314041] pci 0000:00:0e.0: reg 10: [io  0xb000-0xb01f]
        [    1.314045] pci 0000:00:1d.0: [8086:2658] type 0 class 0x000c03
        [    1.314049] pci 0000:00:1d.0: reg 20: [io  0xb200-0xb21f]
        [    1.314053] pci 0000:00:1d.6: [1033:0194] type 0 class 0x000c03
        [    1.314057] pci 0000:00:1d.6: reg 10: [mem 0xef100000-0xef100fff]
        [    1.314065] pci 0000:00:1d.7: [8086:265c] type 0 class 0x000c03
        [    1.314069] pci 0000:00:1d.7: reg 10: [mem 0xef140000-0xef1403ff]
        [    1.314073] pci 0000:00:1e.0: [8086:244e] type 1 class 0x000604
        [    1.314077] pci 0000:00:1f.0: [8086:2810] type 0 class 0x000601
        [    1.314081] pci 0000:00:1f.0: quirk: [io  0x4000-0x407f] claimed by ICH6 ACPI/GPIO/TCO
        [    1.314085] pci 0000:00:1f.1: [8086:244b] type 0 class 0x000101
        [    1.314089] pci 0000:00:1f.1: reg 20: [io  0xe000-0xe00f]
        [    1.314093] pci 0000:00:1f.2: [8086:2821] type 0 class 0x000106
        [    1.314097] pci 0000:00:1f.2: reg 10: [io  0xe200-0xe207]
        [    1.314101] pci 0000:00:1f.2: reg 14: [io  0xe400-0xe403]
        [    1.314105] pci 0000:00:1f.2: reg 18: [io  0xe600-0xe607]
        [    1.314109] pci 0000:00:1f.2: reg 1c: [io  0xe800-0xe803]
        [    1.314113] pci 0000:00:1f.2: reg 20: [io  0xea00-0xea0f]
        [    1.314117] pci 0000:00:1f.2: reg 24: [mem 0xf0200000-0xf0201fff]
        [    1.314121] pci 0000:00:1f.2: PME# supported from D3hot
        [    1.314125] pci 0000:00:1f.2: PME# disabled
        [    1.314129] pci 0000:00:1f.4: [8086:2445] type 0 class 0x000401
        [    1.314133] pci 0000:00:1f.4: reg 10: [io  0xec00-0xecff]
        [    1.314137] pci 0000:00:1f.4: reg 14: [io  0xee00-0xeeff]
        [    1.314141] pci 0000:01:00.0: [1ab8:4005] type 0 class 0x000300
        [    1.314145] pci 0000:01:00.0: reg 10: [io  0x6000-0x601f]
        [    1.314149] pci 0000:01:00.0: reg 14: [mem 0xb0000000-0xb1ffffff pref]
        [    1.314163] pci 0000:01:00.0: reg 30: [mem 0xe2000000-0xe200ffff pref]
        [    1.314167] pci 0000:00:01.0: PCI bridge to [bus 01-01] (subtractive decode)
        [    1.314171] pci 0000:00:01.0:   bridge window [io  0x6000-0x7fff]
        [    1.314175] pci 0000:00:01.0:   bridge window [mem 0xe2000000-0xedffffff]
        [    1.314179] pci 0000:00:01.0:   bridge window [mem 0xb0000000-0xdfffffff 64bit pref]
        [    1.314182] pci 0000:00:01.0:   bridge window [io  0x0000-0xffff] (subtractive decode)
        [    1.314184] pci 0000:00:01.0:   bridge window [mem 0x00000000-0xfffffffff] (subtractive decode)
        [    1.314188] pci 0000:00:0a.0: PCI bridge to [bus 02-02]
        [    1.314192] pci 0000:00:0a.0:   bridge window [io  0x9000-0xafff]
        [    1.314196] pci 0000:00:0a.0:   bridge window [mem 0xee100000-0xef0fffff]
        [    1.314200] pci 0000:00:0a.0:   bridge window [mem 0xe0000000-0xe0ffffff pref]
        [    1.314204] pci 0000:00:1e.0: PCI bridge to [bus 03-03] (subtractive decode)
        [    1.314208] pci 0000:00:1e.0:   bridge window [io  0xc000-0xdfff]
        [    1.314212] pci 0000:00:1e.0:   bridge window [mem 0xef200000-0xf01fffff]
        [    1.314216] pci 0000:00:1e.0:   bridge window [mem 0xe1000000-0x4001ab8e1ffffff 64bit pref]
        [    1.314218] pci 0000:00:1e.0:   bridge window [io  0x0000-0xffff] (subtractive decode)
        [    1.314220] pci 0000:00:1e.0:   bridge window [mem 0x00000000-0xfffffffff] (subtractive decode)
        [    1.314224] ACPI: PCI Interrupt Routing Table [\_SB_.PCI0._PRT]
        [    1.314236] ACPI: PCI Interrupt Routing Table [\_SB_.PCI0.PX16._PRT]
        [    1.314256] ACPI: PCI Interrupt Routing Table [\_SB_.PCI0.PCIN._PRT]
        [    1.314260] ACPI: PCI Interrupt Routing Table [\_SB_.PCI0.PCI2._PRT]
        [    1.314264]  pci0000:00: Requesting ACPI _OSC control (0x1d)
        [    1.314267]  pci0000:00: ACPI _OSC request failed (AE_NOT_FOUND), returned control mask: 0x1d
        [    1.314269] ACPI _OSC control for PCIe not granted, disabling ASPM
        [    1.315300] ACPI Exception: AE_NOT_FOUND, Evaluating _PRS (20110623/pci_link-184)
        [    1.315322] vgaarb: device added: PCI:0000:01:00.0,decodes=io+mem,owns=io+mem,locks=none
        [    1.315326] vgaarb: loaded
        [    1.315328] vgaarb: bridge control possible 0000:01:00.0
        [    1.315344] i2c-core: driver [aat2870] using legacy suspend method
        [    1.315347] i2c-core: driver [aat2870] using legacy resume method
        [    1.315382] SCSI subsystem initialized
        [    1.315414] libata version 3.00 loaded.
        [    1.315422] usbcore: registered new interface driver usbfs
        [    1.315426] usbcore: registered new interface driver hub
        [    1.315460] usbcore: registered new device driver usb
        [    1.315491] PCI: Using ACPI for IRQ routing
        [    1.315495] PCI: pci_cache_line_size set to 64 bytes
        [    1.315499] pci 0000:00:1e.0: no compatible bridge window for [mem 0xe1000000-0x4001ab8e1ffffff 64bit pref]
        [    1.315503] reserve RAM buffer: 000000000009fc00 - 000000000009ffff
        [    1.315505] reserve RAM buffer: 000000003fff0000 - 000000003fffffff
        [    1.315532] NetLabel: Initializing
        [    1.315534] NetLabel:  domain hash size = 128
        [    1.315538] NetLabel:  protocols = UNLABELED CIPSOv4
        [    1.315542] NetLabel:  unlabeled traffic allowed by default
        [    1.319258] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
        [    1.319262] hpet0: 8 comparators, 64-bit 16.000000 MHz counter
        [    1.321780] Switching to clocksource kvm-clock
        [    1.326718] AppArmor: AppArmor Filesystem Enabled
        [    1.326726] pnp: PnP ACPI init
        [    1.326734] ACPI: bus type pnp registered
        [    1.326738] pnp 00:00: [bus 00-7f]
        [    1.326741] pnp 00:00: [io  0x0cf8-0x0cff]
        [    1.326744] pnp 00:00: [io  0x0000-0x0cf7 window]
        [    1.326746] pnp 00:00: [io  0x0d00-0xffff window]
        [    1.326749] pnp 00:00: [mem 0x000a0000-0x000bffff window]
        [    1.326751] pnp 00:00: [mem 0x000d0000-0x000dffff window]
        [    1.326753] pnp 00:00: [mem 0x000c0000-0x000cffff window]
        [    1.326756] pnp 00:00: [mem 0xb0000000-0xfbffffff window]
        [    1.326758] pnp 00:00: [mem 0xfd000000-0xfd7fffff]
        [    1.326762] pnp 00:00: Plug and Play ACPI device, IDs PNP0a08 PNP0a03 (active)
        [    1.326766] pnp 00:01: [io  0x0060]
        [    1.326769] pnp 00:01: [io  0x0064]
        [    1.326773] pnp 00:01: [irq 1]
        [    1.326781] pnp 00:01: Plug and Play ACPI device, IDs PNP0303 (active)
        [    1.326785] pnp 00:02: [irq 12]
        [    1.326793] pnp 00:02: Plug and Play ACPI device, IDs PNP0f03 (active)
        [    1.326797] pnp 00:03: [io  0x0070-0x0075]
        [    1.326801] pnp 00:03: Plug and Play ACPI device, IDs PNP0b00 (active)
        [    1.326805] pnp 00:04: [io  0x0061]
        [    1.326813] pnp 00:04: Plug and Play ACPI device, IDs PNP0800 (active)
        [    1.326817] pnp 00:05: [mem 0xffc00000-0xffffffff]
        [    1.326825] system 00:05: [mem 0xffc00000-0xffffffff] has been reserved
        [    1.326829] system 00:05: Plug and Play ACPI device, IDs PNP0c01 (active)
        [    1.326833] pnp 00:06: [io  0x0000-0x000f]
        [    1.326836] pnp 00:06: [io  0x0080-0x0090]
        [    1.326838] pnp 00:06: [io  0x0094-0x009f]
        [    1.326840] pnp 00:06: [io  0x00c0-0x00df]
        [    1.326844] pnp 00:06: [dma 4]
        [    1.326848] pnp 00:06: Plug and Play ACPI device, IDs PNP0200 (active)
        [    1.326852] pnp 00:07: [io  0x0092-0x0093]
        [    1.326854] pnp 00:07: [io  0x04d0-0x04d1]
        [    1.326856] pnp 00:07: [io  0x1000-0x107f]
        [    1.326858] pnp 00:07: [io  0x1300-0x133f]
        [    1.326860] pnp 00:07: [mem 0xfc000000-0xfcffffff]
        [    1.326868] system 00:07: [io  0x04d0-0x04d1] has been reserved
        [    1.326871] system 00:07: [io  0x1000-0x107f] has been reserved
        [    1.326874] system 00:07: [io  0x1300-0x133f] has been reserved
        [    1.326876] system 00:07: [mem 0xfc000000-0xfcffffff] has been reserved
        [    1.326879] system 00:07: Plug and Play ACPI device, IDs PNP0c02 (active)
        [    1.326883] pnp 00:08: [io  0x00f0-0x00ff]
        [    1.326887] pnp 00:08: [irq 13]
        [    1.326899] pnp 00:08: Plug and Play ACPI device, IDs PNP0c04 (active)
        [    1.326903] pnp 00:09: [mem 0xffc00000-0xffffffff]
        [    1.326907] pnp 00:09: Plug and Play ACPI device, IDs INT0800 (active)
        [    1.326911] pnp 00:0a: [mem 0xfed00000-0xfed003ff]
        [    1.326914] pnp 00:0a: [irq 0 disabled]
        [    1.326918] pnp 00:0a: [irq 8]
        [    1.326928] pnp 00:0a: Plug and Play ACPI device, IDs PNP0103 (active)
        [    1.357794] pnp: PnP ACPI: found 11 devices
        [    1.357796] ACPI: ACPI bus type pnp unregistered
        [    1.365225] PCI: max bus depth: 1 pci_try_num: 2
        [    1.365229] pci 0000:00:01.0: PCI bridge to [bus 01-01]
        [    1.365233] pci 0000:00:01.0:   bridge window [io  0x6000-0x7fff]
        [    1.365237] pci 0000:00:01.0:   bridge window [mem 0xe2000000-0xedffffff]
        [    1.365241] pci 0000:00:01.0:   bridge window [mem 0xb0000000-0xdfffffff 64bit pref]
        [    1.365245] pci 0000:00:0a.0: PCI bridge to [bus 02-02]
        [    1.365248] pci 0000:00:0a.0:   bridge window [io  0x9000-0xafff]
        [    1.365252] pci 0000:00:0a.0:   bridge window [mem 0xee100000-0xef0fffff]
        [    1.365256] pci 0000:00:0a.0:   bridge window [mem 0xe0000000-0xe0ffffff pref]
        [    1.365260] pci 0000:00:1e.0: PCI bridge to [bus 03-03]
        [    1.365263] pci 0000:00:1e.0:   bridge window [io  0xc000-0xdfff]
        [    1.365267] pci 0000:00:1e.0:   bridge window [mem 0xef200000-0xf01fffff]
        [    1.365271] pci 0000:00:01.0: setting latency timer to 64
        [    1.365275] pci 0000:00:0a.0: setting latency timer to 64
        [    1.365279] pci 0000:00:1e.0: setting latency timer to 64
        [    1.365283] pci_bus 0000:00: resource 0 [io  0x0000-0xffff]
        [    1.365285] pci_bus 0000:00: resource 1 [mem 0x00000000-0xfffffffff]
        [    1.365287] pci_bus 0000:01: resource 0 [io  0x6000-0x7fff]
        [    1.365289] pci_bus 0000:01: resource 1 [mem 0xe2000000-0xedffffff]
        [    1.365291] pci_bus 0000:01: resource 2 [mem 0xb0000000-0xdfffffff 64bit pref]
        [    1.365294] pci_bus 0000:01: resource 4 [io  0x0000-0xffff]
        [    1.365296] pci_bus 0000:01: resource 5 [mem 0x00000000-0xfffffffff]
        [    1.365298] pci_bus 0000:02: resource 0 [io  0x9000-0xafff]
        [    1.365300] pci_bus 0000:02: resource 1 [mem 0xee100000-0xef0fffff]
        [    1.365302] pci_bus 0000:02: resource 2 [mem 0xe0000000-0xe0ffffff pref]
        [    1.365304] pci_bus 0000:03: resource 0 [io  0xc000-0xdfff]
        [    1.365306] pci_bus 0000:03: resource 1 [mem 0xef200000-0xf01fffff]
        [    1.365308] pci_bus 0000:03: resource 4 [io  0x0000-0xffff]
        [    1.365310] pci_bus 0000:03: resource 5 [mem 0x00000000-0xfffffffff]
        [    1.365314] NET: Registered protocol family 2
        [    1.365318] IP route cache hash table entries: 32768 (order: 6, 262144 bytes)
        [    1.365330] TCP established hash table entries: 131072 (order: 9, 2097152 bytes)
        [    1.365334] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes)
        [    1.365338] TCP: Hash tables configured (established 131072 bind 65536)
        [    1.365342] TCP reno registered
        [    1.365346] UDP hash table entries: 512 (order: 2, 16384 bytes)
        [    1.365350] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes)
        [    1.365362] NET: Registered protocol family 1
        [    1.365366] pci 0000:00:1d.0: PCI INT C -> GSI 18 (level, low) -> IRQ 18
        [    1.365812] pci 0000:00:1d.0: HCRESET not completed yet!
        [    1.365816] pci 0000:00:1d.0: PCI INT C disabled
        [    1.365820] pci 0000:00:1d.6: PCI INT A -> GSI 16 (level, low) -> IRQ 16
        [    1.369444] pci 0000:00:1d.6: PCI INT A disabled
        [    1.369448] pci 0000:00:1d.7: PCI INT D -> GSI 19 (level, low) -> IRQ 19
        [    1.369483] pci 0000:00:1d.7: PCI INT D disabled
        [    1.369487] pci 0000:01:00.0: Boot video device
        [    1.369491] PCI: CLS 0 bytes, default 64
        [    1.369595] audit: initializing netlink socket (disabled)
        [    1.369599] type=2000 audit(1416123455.132:1): initialized
        [    1.383324] Trying to unpack rootfs image as initramfs...
        [    1.402383] HugeTLB registered 2 MB page size, pre-allocated 0 pages
        [    1.406732] VFS: Disk quotas dquot_6.5.2
        [    1.406742] Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
        [    1.413828] fuse init (API version 7.17)
        [    1.414353] msgmni has been set to 1949
        [    1.425880] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
        [    1.425921] io scheduler noop registered
        [    1.425925] io scheduler deadline registered
        [    1.425933] io scheduler cfq registered (default)
        [    1.425945] pci_hotplug: PCI Hot Plug PCI Core version: 0.5
        [    1.425949] pciehp: PCI Express Hot Plug Controller Driver version: 0.4
        [    1.428022] ACPI: Deprecated procfs I/F for AC is loaded, please retry with CONFIG_ACPI_PROCFS_POWER cleared
        [    1.428698] ACPI: AC Adapter [ADP0] (on-line)
        [    1.429683] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0
        [    1.429690] ACPI: Power Button [PWRF]
        [    1.429746] input: Sleep Button as /devices/LNXSYSTM:00/LNXSLPBN:00/input/input1
        [    1.429750] ACPI: Sleep Button [SLPF]
        [    1.431365] ACPI: Deprecated procfs I/F for battery is loaded, please retry with CONFIG_ACPI_PROCFS_POWER cleared
        [    1.431373] ACPI: Battery Slot [BAT0] (battery present)
        [    1.431411] ERST: Table is not found!
        [    1.431415] GHES: HEST is not enabled!
        [    1.431419] virtio-pci 0000:00:05.0: enabling device (0000 -> 0003)
        [    1.431423] virtio-pci 0000:00:05.0: PCI INT A -> GSI 23 (level, low) -> IRQ 23
        [    1.431427] virtio-pci 0000:00:05.0: setting latency timer to 64
        [    1.433194] virtio-pci 0000:00:0e.0: enabling device (0000 -> 0001)
        [    1.433198] virtio-pci 0000:00:0e.0: PCI INT B -> GSI 22 (level, low) -> IRQ 22
        [    1.433202] virtio-pci 0000:00:0e.0: setting latency timer to 64
        [    1.442327] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
        [    1.444395] Linux agpgart interface v0.103
        [    1.444727] brd: module loaded
        [    1.444918] loop: module loaded
        [    1.444926] ahci 0000:00:1f.2: version 3.0
        [    1.444930] ahci 0000:00:1f.2: PCI INT A -> GSI 16 (level, low) -> IRQ 16
        [    1.445431] ahci 0000:00:1f.2: irq 40 for MSI/MSI-X
        [    1.445807] ahci: SSS flag set, parallel bus scan disabled
        [    1.446953] ahci 0000:00:1f.2: AHCI 0001.0100 32 slots 6 ports 3 Gbps 0x3f impl SATA mode
        [    1.446957] ahci 0000:00:1f.2: flags: 64bit ncq stag pm led only slum part
        [    1.446961] ahci 0000:00:1f.2: setting latency timer to 64
        [    1.458143] scsi0 : ahci
        [    1.460750] scsi1 : ahci
        [    1.460810] scsi2 : ahci
        [    1.463898] scsi3 : ahci
        [    1.469819] scsi4 : ahci
        [    1.470929] scsi5 : ahci
        [    1.470959] ata1: SATA max UDMA/133 abar m8192@0xf0200000 port 0xf0200100 irq 40
        [    1.470963] ata2: SATA max UDMA/133 abar m8192@0xf0200000 port 0xf0200180 irq 40
        [    1.470967] ata3: SATA max UDMA/133 abar m8192@0xf0200000 port 0xf0200200 irq 40
        [    1.470971] ata4: SATA max UDMA/133 abar m8192@0xf0200000 port 0xf0200280 irq 40
        [    1.470975] ata5: SATA max UDMA/133 abar m8192@0xf0200000 port 0xf0200300 irq 40
        [    1.470978] ata6: SATA max UDMA/133 abar m8192@0xf0200000 port 0xf0200380 irq 40
        [    1.470986] ata_piix 0000:00:1f.1: version 2.13
        [    1.471483] ata_piix 0000:00:1f.1: setting latency timer to 64
        [    1.473854] scsi6 : ata_piix
        [    1.475082] scsi7 : ata_piix
        [    1.475111] ata7: PATA max UDMA/100 cmd 0x1f0 ctl 0x3f6 bmdma 0xe000 irq 14
        [    1.475115] ata8: PATA max UDMA/100 cmd 0x170 ctl 0x376 bmdma 0xe008 irq 15
        [    1.475512] Fixed MDIO Bus: probed
        [    1.475528] tun: Universal TUN/TAP device driver, 1.6
        [    1.475532] tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
        [    1.475822] virtio-pci 0000:00:05.0: irq 41 for MSI/MSI-X
        [    1.475988] virtio-pci 0000:00:05.0: irq 42 for MSI/MSI-X
        [    1.476007] virtio-pci 0000:00:05.0: irq 43 for MSI/MSI-X
        [    1.478850] PPP generic driver version 2.4.2
        [    1.478861] ACPI: Battery Slot [BAT0] (battery present)
        [    1.478888] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
        [    1.478892] ehci_hcd 0000:00:1d.7: PCI INT D -> GSI 19 (level, low) -> IRQ 19
        [    1.478896] ehci_hcd 0000:00:1d.7: setting latency timer to 64
        [    1.478900] ehci_hcd 0000:00:1d.7: EHCI Host Controller
        [    1.479138] ehci_hcd 0000:00:1d.7: new USB bus registered, assigned bus number 1
        [    1.479215] ehci_hcd 0000:00:1d.7: Enabling legacy PCI PM
        [    1.479219] ehci_hcd 0000:00:1d.7: cache line size of 64 is not supported
        [    1.479223] ehci_hcd 0000:00:1d.7: irq 19, io mem 0xef140000
        [    1.489850] ehci_hcd 0000:00:1d.7: USB 2.0 started, EHCI 1.00
        [    1.490394] hub 1-0:1.0: USB hub found
        [    1.490398] hub 1-0:1.0: 15 ports detected
        [    1.490410] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
        [    1.490414] uhci_hcd: USB Universal Host Controller Interface driver
        [    1.490418] uhci_hcd 0000:00:1d.0: PCI INT C -> GSI 18 (level, low) -> IRQ 18
        [    1.490422] uhci_hcd 0000:00:1d.0: setting latency timer to 64
        [    1.490426] uhci_hcd 0000:00:1d.0: UHCI Host Controller
        [    1.490444] uhci_hcd 0000:00:1d.0: new USB bus registered, assigned bus number 2
        [    1.492638] uhci_hcd 0000:00:1d.0: HCRESET not completed yet!
        [    1.492642] uhci_hcd 0000:00:1d.0: irq 18, io base 0x0000b200
        [    1.492719] hub 2-0:1.0: USB hub found
        [    1.492723] hub 2-0:1.0: 2 ports detected
        [    1.492731] xhci_hcd 0000:00:1d.6: PCI INT A -> GSI 16 (level, low) -> IRQ 16
        [    1.492735] xhci_hcd 0000:00:1d.6: setting latency timer to 64
        [    1.492739] xhci_hcd 0000:00:1d.6: xHCI Host Controller
        [    1.492761] xhci_hcd 0000:00:1d.6: new USB bus registered, assigned bus number 3
        [    1.492933] xhci_hcd 0000:00:1d.6: cache line size of 64 is not supported
        [    1.493135] xhci_hcd 0000:00:1d.6: irq 44 for MSI/MSI-X
        [    1.497817] xHCI xhci_add_endpoint called for root hub
        [    1.497820] xHCI xhci_check_bandwidth called for root hub
        [    1.497828] hub 3-0:1.0: USB hub found
        [    1.497832] hub 3-0:1.0: 2 ports detected
        [    1.497840] xhci_hcd 0000:00:1d.6: xHCI Host Controller
        [    1.497859] xhci_hcd 0000:00:1d.6: new USB bus registered, assigned bus number 4
        [    1.498242] xHCI xhci_add_endpoint called for root hub
        [    1.498244] xHCI xhci_check_bandwidth called for root hub
        [    1.498287] hub 4-0:1.0: USB hub found
        [    1.498291] hub 4-0:1.0: 12 ports detected
        [    1.498306] usbcore: registered new interface driver libusual
        [    1.498310] i8042: PNP: PS/2 Controller [PNP0303:KBC,PNP0f03:PS2M] at 0x60,0x64 irq 1,12
        [    1.498709] serio: i8042 KBD port at 0x60,0x64 irq 1
        [    1.498716] serio: i8042 AUX port at 0x60,0x64 irq 12
        [    1.498761] mousedev: PS/2 mouse device common for all mice
        [    1.498995] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input2
        [    1.499430] rtc_cmos 00:03: rtc core: registered rtc_cmos as rtc0
        [    1.499449] rtc0: alarms up to one day, y3k, 242 bytes nvram, hpet irqs
        [    1.499465] device-mapper: uevent: version 1.0.3
        [    1.499488] device-mapper: ioctl: 4.22.0-ioctl (2011-10-19) initialised: dm-devel@redhat.com
        [    1.499496] cpuidle: using governor ladder
        [    1.499498] cpuidle: using governor menu
        [    1.499500] EFI Variables Facility v0.08 2004-May-17
        [    1.499508] TCP cubic registered
        [    1.499532] NET: Registered protocol family 10
        [    1.500272] NET: Registered protocol family 17
        [    1.500276] Registering the dns_resolver key type
        [    1.500318] PM: Hibernation image not present or could not be loaded.
        [    1.500326] registered taskstats version 1
        [    1.613805] Freeing initrd memory: 13916k freed
        [    1.620446]   Magic number: 6:554:622
        [    1.620675] rtc_cmos 00:03: setting system clock to 2014-11-16 07:37:35 UTC (1416123455)
        [    1.620695] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found
        [    1.620696] EDD information not available.
        [    1.794615] ata1: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
        [    1.794728] ata1.00: ATA-8: Master-0 SSD, F.P6PVE4, max UDMA/100
        [    1.794730] ata1.00: 134217728 sectors, multi 0: LBA48 NCQ (depth 31/32)
        [    1.794846] ata1.00: configured for UDMA/100
        [    1.794935] scsi 0:0:0:0: Direct-Access     ATA      Master-0 SSD     F.P6 PQ: 0 ANSI: 5
        [    1.795043] sd 0:0:0:0: [sda] 134217728 512-byte logical blocks: (68.7 GB/64.0 GiB)
        [    1.795045] sd 0:0:0:0: [sda] 4096-byte physical blocks
        [    1.795077] sd 0:0:0:0: [sda] Write Protect is off
        [    1.795078] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
        [    1.795089] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
        [    1.795241] sd 0:0:0:0: Attached scsi generic sg0 type 0
        [    1.795510]  sda: sda1 sda2 < sda5 >
        [    1.795717] sd 0:0:0:0: [sda] Attached SCSI disk
        [    1.801984] usb 1-1: new high-speed USB device number 2 using ehci_hcd
        [    2.113994] ata2: SATA link up 1.5 Gbps (SStatus 113 SControl 300)
        [    2.114110] ata2.00: ATAPI: Virtual DVD-ROM [1], FWR1, max UDMA/25
        [    2.114280] ata2.00: configured for UDMA/25
        [    2.114602] scsi 1:0:0:0: CD-ROM                     Virtual DVD-ROM  R103 PQ: 0 ANSI: 5
        [    2.114925] sr0: scsi3-mmc drive: 44x/44x cd/rw xa/form2 cdda tray
        [    2.114927] cdrom: Uniform CD-ROM driver Revision: 3.20
        [    2.115004] sr 1:0:0:0: Attached scsi CD-ROM sr0
        [    2.115069] sr 1:0:0:0: Attached scsi generic sg1 type 5
        [    2.366344] Refined TSC clocksource calibration: 2795.207 MHz.
        [    2.434044] ata3: SATA link down (SStatus 0 SControl 300)
        [    2.628850] uhci_hcd 0000:00:1d.0: Controller not stopped yet!
        [    2.753871] ata4: SATA link down (SStatus 0 SControl 300)
        [    3.074528] ata5: SATA link down (SStatus 0 SControl 300)
        [    3.393951] ata6: SATA link down (SStatus 0 SControl 300)
        [    3.394885] Freeing unused kernel memory: 924k freed
        [    3.394966] Write protecting the kernel read-only data: 12288k
        [    3.398048] Freeing unused kernel memory: 1588k freed
        [    3.400272] Freeing unused kernel memory: 1188k freed
        [    3.410792] udevd[96]: starting version 175
        [    3.569410] EXT4-fs (sda1): INFO: recovery required on readonly filesystem
        [    3.569413] EXT4-fs (sda1): write access will be enabled during recovery
        [    4.508545] EXT4-fs (sda1): orphan cleanup on readonly fs
        [    4.508552] EXT4-fs (sda1): ext4_orphan_cleanup: deleting unreferenced inode 797077
        [    4.508592] EXT4-fs (sda1): ext4_orphan_cleanup: deleting unreferenced inode 1578825
        [    4.508597] EXT4-fs (sda1): ext4_orphan_cleanup: deleting unreferenced inode 1576542
        [    4.508601] EXT4-fs (sda1): ext4_orphan_cleanup: deleting unreferenced inode 1576540
        [    4.508605] EXT4-fs (sda1): ext4_orphan_cleanup: deleting unreferenced inode 1576539
        [    4.508609] EXT4-fs (sda1): ext4_orphan_cleanup: deleting unreferenced inode 1576538
        [    4.508612] EXT4-fs (sda1): 6 orphan inodes deleted
        [    4.508613] EXT4-fs (sda1): recovery complete
        [    4.745208] EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
        [    5.619435] Adding 522236k swap on /dev/sda5.  Priority:-1 extents:1 across:522236k SS
        [    6.048803] EXT4-fs (sda1): re-mounted. Opts: errors=remount-ro
        [    6.621262] ADDRCONF(NETDEV_UP): eth0: link is not ready
        [    6.641977] udevd[345]: starting version 175
        [    6.649901] RPC: Registered named UNIX socket transport module.
        [    6.649903] RPC: Registered udp transport module.
        [    6.649904] RPC: Registered tcp transport module.
        [    6.649904] RPC: Registered tcp NFSv4.1 backchannel transport module.
        [    6.651205] FS-Cache: Loaded
        [    6.675078] FS-Cache: Netfs 'nfs' registered for caching
        [    6.687039] lp: driver loaded but no devices found
        [    6.701639] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).
        [    6.842176] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
        [    6.885456] snd_intel8x0 0000:00:1f.4: PCI INT B -> GSI 17 (level, low) -> IRQ 17
        [    6.885459] intel8x0: enable Parallels VM optimization
        [    6.885469] snd_intel8x0 0000:00:1f.4: setting latency timer to 64
        [    6.935886] type=1400 audit(1416123460.812:2): apparmor="STATUS" operation="profile_load" name="/sbin/dhclient" pid=520 comm="apparmor_parser"
        [    6.936112] type=1400 audit(1416123460.812:3): apparmor="STATUS" operation="profile_load" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=520 comm="apparmor_parser"
        [    6.936240] type=1400 audit(1416123460.812:4): apparmor="STATUS" operation="profile_load" name="/usr/lib/connman/scripts/dhclient-script" pid=520 comm="apparmor_parser"
        [    6.965299] Linux video capture interface: v2.00
        [    6.982030] uvcvideo: Found UVC 1.00 device Virtual Video Camera (203a:fff9)
        [    6.984567] uvcvideo: UVC non compliance - GET_DEF(PROBE) not supported. Enabling workaround.
        [    6.986136] usbcore: registered new interface driver uvcvideo
        [    6.986138] USB Video Class driver (1.1.1)
        [    7.269027] init: failsafe main process (598) killed by TERM signal
        [    7.357706] type=1400 audit(1416123461.232:5): apparmor="STATUS" operation="profile_replace" name="/sbin/dhclient" pid=832 comm="apparmor_parser"
        [    7.358170] input: ImExPS/2 Generic Explorer Mouse as /devices/platform/i8042/serio1/input/input3
        [    7.360335] type=1400 audit(1416123461.236:6): apparmor="STATUS" operation="profile_replace" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=832 comm="apparmor_parser"
        [    7.360465] type=1400 audit(1416123461.236:7): apparmor="STATUS" operation="profile_replace" name="/usr/lib/connman/scripts/dhclient-script" pid=832 comm="apparmor_parser"
        [    7.363443] type=1400 audit(1416123461.240:8): apparmor="STATUS" operation="profile_load" name="/usr/sbin/mysqld" pid=839 comm="apparmor_parser"
        [    7.376497] type=1400 audit(1416123461.252:9): apparmor="STATUS" operation="profile_load" name="/usr/sbin/tcpdump" pid=851 comm="apparmor_parser"
        [    7.495034] type=1400 audit(1416123461.372:10): apparmor="STATUS" operation="profile_replace" name="/usr/sbin/mysqld" pid=931 comm="apparmor_parser"
        [    7.655277] NFSD: Using /var/lib/nfs/v4recovery as the NFSv4 state recovery directory
        [    7.662341] NFSD: starting 90-second grace period
        [    7.925540] intel8x0_measure_ac97_clock: measured 55152 usecs (2728 samples)
        [    7.925544] intel8x0: clocking to 46580
        [    7.991875] vesafb: mode is 800x600x32, linelength=3200, pages=0
        [    7.991877] vesafb: scrolling: redraw
        [    7.991880] vesafb: Truecolor: size=8:8:8:8, shift=24:16:8:0
        [    7.995170] vesafb: framebuffer at 0xb0000000, mapped to 0xffffc90001580000, using 1920k, total 1920k
        [    8.005480] Console: switching to colour frame buffer device 100x37
        [    8.005490] fb0: VESA VGA frame buffer device

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

