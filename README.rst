============================
django-issue-synchronisation
============================

The idea behind this project started with an internal web based working time tracking
software I wrote for our company (`Inhouse-Web`__ became the Open Source spinoff
project for this idea). We needed a mechanism to synchronize `Trac`__ issues
automatically, and provide an autocompletion feature for issue based worktime
bookings. As issue data is always based upon more or less similar information, I
thought of building a separate application, that can easily beplugged into a
Django based web application to aggregate different issue tracking systems into
one database.

Thanks
======

`Andi Albrecht`__ wrote the first Trac methods, which are the base for the
synchronisation plugin used in django-issue-synchronisation.

Features
========

 * Supports issue aggregation for various issue tracking systems.
 * Provides an universal table structure for issue data.
 * Commandline actions for synchronizing the issue tracking systems.
 * Admin backend to administrate the trackers and issues.
 * Signals for pre and post actions.

Installation
============

#. Get the code::

	$ pip install django-issue-synchronisation
	$ easy_install django-issue-synchronisation

   or for the latest development version::

	$ git clone git://github.com/hkage/django-issue-synchronisation.git

#. Add `issues` to the list of `INSTALLED_APPS`::

	INSTALLED_APPS = (
	    # ...,
	    'issues'
	)

#. Run::

	$ python manage.py syncdb

   to create the needed tables.

Configuration
=============

`SOCKET_TIMEOUT`
----------------

Maximum timeout duration of any socket operations in seconds. Default is 10.

Start Synchronization
=====================

If you plugged in ``django-issue-synchronisation`` into your Django application,
it will provide some new commands to the ``manage.py`` script. The most
important of them is the ``sync_issues`` command::

	$ python manage.py sync_issues

This will synchronise all issues trackers, that are defined in the **tracker**
table. If you want to synchronise only certain trackers, you can use their
internal ids::

	$ python manage.py sync_issues 1 2


Supported issue tracking systems
================================

============= ========= ========================  ===========
Issue tracker Protocoll Type                      tested with
============= ========= ========================  ===========
`Github`__    HTTP      decentralized [#decent]_
`Roundup`__   XML-RPC   both                      1.4.15
`Trac`__      XML-RPC   both                      0.12
============= ========= ========================  ===========

__ https://github.com/hkage/inhouse-web
__ http://trac.edgewall.org
__ https://github.com/andialbrecht
__ http://www.github.com
__ http://www.roundup-tracker.org/
__ http://trac.edgewall.org

.. [#decent] Decentralized issue trackers are restriced to one location/URL.
 They don't work with local instances and will be hard coded against their URLs.
