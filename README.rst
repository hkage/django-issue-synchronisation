============================
django-issue-synchronisation
============================

The idea behind this project started with an internal web based working time tracking 
software I wrote for our company (`Ìnhouse-Web`__ became the Open Source spinoff
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