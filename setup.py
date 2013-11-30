import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README')).read()

setup(
		name='django-openlavaweb',
		version='1.0',
		packages=['openlavaweb'],
		include_package_data=True,	
		license="GPL 3",
		description="Openlava Web is a REST based web interface to the Openlava scheduling system. Openlava Web provides both HTML and JSON interfaces allowing users to view information on jobs, queues, hosts, and other components of the scheduling environment.",
		long_description=README,
		url="http://ay60dxg.com/projects/openlavaweb/",
		author="David Irvine",
		author_email="irvined@gmail.com",
		classifiers=[
			'Environment :: Web Environment',
			'Framework :: Django',
			'Programming Language :: Python',
			'Operating System :: OS Independent',
			'Programming Language :: Python :: 2',
			'Programming Language :: Python :: 2.7',
			'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
			'Intended Audience :: Science/Research',
			'Intended Audience :: System Administrators',
			'Topic :: Scientific/Engineering',
			'Topic :: Scientific/Engineering :: Information Analysis',
			],
		)
