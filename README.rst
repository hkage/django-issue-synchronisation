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

Get the code:

 $ pip install django-issue-synchronisation
 $ easy_install django-issue-synchronisation
 
or for the latest development version:

 $ git clone git://github.com/hkage/django-issue-synchronisation.git
 
Add ``issues`` to the list of ``INSTALLED_APPS``.

Run ``python manage.py syncdb`` to create the needed tables.

Supported issue tracking systems
================================

============= ========= ============= ===========
Issue tracker Protocoll Type          tested with
============= ========= ============= ===========
`Github`__    HTTP      decentralized
`Roundup`__   XML-RPC   both          1.4.15
`Trac`__      XML-RPC   both          0.12
============= ========= ============= ===========

__ https://github.com/hkage/inhouse-web
__ http://trac.edgewall.org
__ https://github.com/andialbrecht
__ http://www.github.com
__ http://www.roundup-tracker.org/
__ http://trac.edgewall.org