==============
librarian-logs
==============

This component contains a dashboard plugin for viewing and downloading
application and system logs, along with an independent tool for collecting and
packaging useful diagnostic information, meant to ease the troubleshooting
process of issues encountered on deployed devices.

Installation
------------

The component has the following dependencies:

- librarian-core_
- librarian-dashboard_

To enable this component, add it to the list of components in librarian_'s
`config.ini` file, e.g.::

    [app]
    +components =
        librarian_logs

Development
-----------

In order to recompile static assets, make sure that compass_ and coffeescript_
are installed on your system. To perform a one-time recompilation, execute::

    make recompile

To enable the filesystem watcher and perform automatic recompilation on changes,
use::

    make watch

.. _librarian: https://github.com/Outernet-Project/librarian
.. _librarian-core: https://github.com/Outernet-Project/librarian-core
.. _librarian-dashboard: https://github.com/Outernet-Project/librarian-dashboard
.. _compass: http://compass-style.org/
.. _coffeescript: http://coffeescript.org/
