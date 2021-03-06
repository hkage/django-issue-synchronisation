============================
django-issue-synchronisation
============================

|buildstatus|_

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
synchronisation plugin used in ``django-issue-synchronisation`.

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

.. code-block:: python

	INSTALLED_APPS = (
	    # ...,
	    'issues'
	)

#. Run::

	$ python manage.py syncdb

   to create the needed tables.

Settings
========

``SOCKET_TIMEOUT`` (default: 10)
  Maximum timeout duration of any socket operations in seconds.

Commands
========

The following ``manage.py`` commands are available after installing the
application:

``manage_sync``
  This command will provide some actions to manage the different tracker
  defined. See the command help for details.

``sync_issues TRACKER_ID``
  Start synchronizing a tracker by it's id. If no id given, all trackers will
  be updated.


Supported issue tracking systems
================================

============= ========= ========================  ===========
Issue tracker Protocoll Type                      tested with
============= ========= ========================  ===========
`Github`__    HTTP      decentralized [#decent]_
`Roundup`__   XML-RPC   both                      1.4.15
`Trac`__      XML-RPC   both                      0.12.x
============= ========= ========================  ===========

__ https://github.com/hkage/inhouse-web
__ http://trac.edgewall.org
__ https://github.com/andialbrecht
__ http://www.github.com
__ http://www.roundup-tracker.org/
__ http://trac.edgewall.org

.. [#decent] Decentralized issue trackers are restriced to one location/URL.
 They don't work with local instances and will be hard coded against their URLs.

.. |buildstatus| image:: https://travis-ci.org/hkage/django-issue-synchronisation.png?branch=master
.. _buildstatus: http://travis-ci.org/hkage/idjango-issue-synchronisation