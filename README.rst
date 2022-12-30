Django CodeMirror 6
===================

`Django CodeMirror 6 <http://www.grantjenks.com/docs/django-codemirror6/>`__ is
an Apache2 licensed Django application to support CodeMirror 6.


Features
--------

- Pre-compiled bundles for Code Mirror 6
- Tested on Python 3.7, 3.8, 3.9, 3.10
- Tested on Django 3.2 LTS and Django 4.0
- Tested on Linux, Mac, and Windows

.. image:: https://github.com/grantjenks/django-codemirror6/workflows/integration/badge.svg
   :target: https://github.com/grantjenks/django-codemirror6/actions?query=workflow%3Aintegration

.. image:: https://github.com/grantjenks/django-codemirror6/workflows/release/badge.svg
   :target: https://github.com/grantjenks/django-codemirror6/actions?query=workflow%3Arelease


Quickstart
----------

Installing Django CodeMirror 6 is simple with `pip
<http://www.pip-installer.org/>`_::

    $ pip install django-codemirror6

Change `settings.py` like:

.. code::

   INSTALLED_APPS += ['django_codemirror6']

In the template:

.. code::

   {% load static %}
   ...
   <script src="{% static 'cm6/cm6-all-yjs.min.js' %}"></script>

Bundles are named as:

.. code::

   cm6[-language][-yjs][.min].js

* ``[-language]`` is optional and any of cpp, css, html, java, javascript,
  json, markdown, php, python, rust, sql, xml, or the special "all"

* ``[-yjs]`` is optional for real-time sharing/collaboration

* ``[.min]`` is optional for minified sources

Examples:

* ``cm6.js`` is a text editor with no specific language support and no yjs

* ``cm6-python.min.js`` is a minified text editor with Python language support

* ``cm6-all-yjs.min.js`` is a minified text editor with everything

See the `demo`_ for a Code Mirror 6 example configuration.

.. _`demo`: https://github.com/grantjenks/django-codemirror6/blob/main/src/django_codemirror6/templates/cm6/demo.html


Reference and Indices
---------------------

* `Django CodeMirror 6 Documentation`_
* `Django CodeMirror 6 at PyPI`_
* `Django CodeMirror 6 at GitHub`_
* `Django CodeMirror 6 Issue Tracker`_

.. _`Django CodeMirror 6 Documentation`: http://www.grantjenks.com/docs/django-codemirror6/
.. _`Django CodeMirror 6 at PyPI`: https://pypi.python.org/pypi/django-codemirror6/
.. _`Django CodeMirror 6 at GitHub`: https://github.com/grantjenks/django-codemirror6
.. _`Django CodeMirror 6 Issue Tracker`: https://github.com/grantjenks/django-codemirror6/issues


Django CodeMirror 6 License
---------------------------

Copyright 2022-2023 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.
