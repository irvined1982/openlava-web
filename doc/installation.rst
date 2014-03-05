Web Server Installation
=======================

Openlava-Web is a django application. It is installed and configured just like any other Django application would be. The following steps are required to install Openlava-Web.

Install Django
--------------

If you have not already done so, `Install Django <https://docs.djangoproject.com/en/1.6/intro/install/>`_.

Django Project
--------------

Create and configure a django project. This can be done by following `these steps <https://docs.djangoproject.com/en/1.6/intro/tutorial01/#creating-a-project>`_.

Web Server Configuration
------------------------

There are two possible configuration options, the first, if you simply want a read-only interface to your cluster, for example to show job information and queue utilization, you can use the WSGI configuration as prescribed in the Django tutorial.  However, if you want to enable job submission and cluster management, OpenlavaWeb needs to be able to call setuid, which requires root privileges.  It is not permitted to run WSGI applications as root, to get around this you need to configure FastCGI, this allows you to start the FastCGI server as root.
 
To start the FastCGI server, on the command line use something like::

    $ sudo ./manage.py runfcgi method=prefork host=127.0.0.1 port=3033 pidfile=olweb.pid

Ideally you should put this in an init script so that the server will be persistent across reboots.  

I’ve found Lighttpd is easy to configure and works well for this purpose, it is fast, and easy to configure.  The appropriate configuration sections are::

    alias.url = (
        "/static" => "/var/www/olweb/static",
        "/media" => "/var/www/olweb/media",
    )
    
    fastcgi.server = (
        "/olweb" => (
            "main" => (
                # Use host / port instead of socket for TCP fastcgi
                "host" => "127.0.0.1",
                "port" => 3033,
                #"socket" => "/home/user/mysite.sock",
                "check-local" => "disable",
            )
        ),
    )

Install openlava-python
-----------------------

Install the Openlava python bindings.::

    $ git clone https://github.com/irvined1982/openlava-python.git
    $ cd openlava-python/openlava/
    $ python setup.py install

Download Openlava-Web
--------------------

Use git to checkout `Openlava-Web <https://github.com/irvined1982/openlava-web>`_.::

    $ git clone https://github.com/irvined1982/openlava-web.git
    $ git submodule update --init --recursive

Install Openlava-Web
--------------------

Use setuptools to install the module.::

    $ sudo python setup.py install

Activate Openlava-Web
---------------------

Install Openlava-Web as an application in your django project.::

    INSTALLED_APPS = (
    ...
        'openlavaweb',
    ...
    )

Configure the URLs for Openlava-Web. Open urls.py in your django project, and include the url configuration for Openlava-Web::

    urlpatterns = patterns('',
        url(r'^', include('openlavaweb.urls')),

You can now view open lava web by visiting your web server.

Client Tools Installation
=========================

Download Openlava-Web
--------------------

Use git to checkout `Openlava-Web <https://github.com/irvined1982/openlava-web>`_.::

    $ git clone https://github.com/irvined1982/openlava-web.git
    $ git submodule update --init --recursive

Install Openlava-Web
--------------------

Enter the client-tools directory and use setuptools to install the module.::

    $ cd client-tools
    $ sudo python setup.py install
