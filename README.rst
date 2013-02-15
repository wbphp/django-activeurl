================
django-activeurl
================
:Info: Easy to use active url highlighting for django

Features:
*********
* Automatic highlighting currently active <a> tags with css
* Automatic highlighting up-level <a> tags for your menus
* Removes boring stuff from your life!

Usage:
******
in your templates you need::

    {% load activeurl %}

then::

    {% activeurl %}
        <ul>
            <li>
                <a href="/some_page/">
                    some_page
                </a>
            </li>
            <li>
                <a href="/another_page/">
                    another_page
                </a>
            </li>
        </ul>
    {% endactiveurl %}

will be rendered into::

    <ul>
        <li class="active">
            <a href="/some_page/">
                some_page
            </a>
        </li>
        <li>
            <a href="/another_page/">
                another_page
            </a>
        </li>
    </ul>

html tags inside ``{% activeurl %}{% endactiveurl %}`` must have valid root tag,
like <ul> or <div>, etc - otherwise they will be wrapped into <div>

if your yor current ``request.get_full_path()`` starts with ``/some_page/``

`starts with logic decided for appling "active" status for up-level <a>
in your menus/submenus`

Installation
************
install the ``stable version`` using ``pip``::

    pip install django-activeurl

install the ``in-development version`` using ``pip``::

    pip install -e git+git://github.com/hellysmile/django-activeurl#egg=django-activeurl


modify your ``settings.py``:

add ``'django-activeurl'`` to your ``INSTALLED_APPS``

add ``'django.core.context_processors.request'`` to your ``TEMPLATE_CONTEXT_PROCESSORS``

like this::

    INSTALLED_APPS = (
        ...
        'django-activeurl',
        ...
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'django.core.context_processors.request',
        ...
    )

Quick start
***********
for successful lxml building you need to install some system stuff eg:

Ubuntu:
-------
::

    sudo apt-get install libxml2 libxml2-dev libxslt-dev build-essential python-dev
    sudo ldconfig

Fedora:
-------
::

    sudo yum groupinstall 'Development Tools'
    sudo yum install libxslt-devel libxml2 libxml2-devel python-devel
    sudo ldconfig


Windows:
--------
pre build lxml binary you can find `here <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_

Cloud:
-------
99.99% thats ``lxml`` will build out from the box

Keep in mind, if your distro/os provides executable ``python`` with ``python3``
(like `Archlinux <https://www.archlinux.org/>`_) you may check installation
and addition instructions

ready to use example:
---------------------
::

    git clone https://github.com/hellysmile/django-activeurl.git
    cd django-activeurl
    virtualenv env
    source env/bin/activate
    cd example
    pip install -r dev_requirements.txt
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver

then open `http://127.0.0.1:8000/pages/page1/ <http://127.0.0.1:8000/pages/page1/>`_
in your favorite web-browser

Configuration and performance
*****************************
in additional to ``{% activeurl %}`` you can add keyword parameters
``css_class`` and ``parent_tag``, which means css class which will
be added to parent element of <a>, is these case it is <li>

example::

    {% activeurl css_class="current" parent_tag="li" %}
        <ul>
            <li>
                <a href="/some_page/">
                    some_page
                </a>
            </li>
        </ul>
    {% endactiveurl %}

will be rendered into::

    <ul>
        <li class="current">
            <a href="/some_page/">
                some_page
            </a>
        </li>
    </ul>

by default these values are::

    {% activeurl css_class="active" parent_tag="li" %}

there is no rebuilding HTML inside template tag when no "active" urls found

by default ``CACHE_ACTIVE_URL`` is ``True``, so before building HTML tree,
searching "active" urls, ``django-activeurl`` will try to get
previously rendered HTML from your cache backend

You can disable caching in your ``settngs.py``::

    CACHE_ACTIVE_URL = False

addition you can set ``CACHE_ACTIVE_URL_TIMEOUT`` which is
timeout for cache key to expire

default value is::

    CACHE_ACTIVE_URL_TIMEOUT = 60 * 60 * 24 # 1 day

and the last one configurable option is ``CACHE_ACTIVE_URL_PREFIX`` which is
by defaults ``django_activeurl.`` - its cache key prefix, for skipping issues
with similar keys in your backend

Background
**********
for building HTML element tree ``django-activeurl`` uses
`lxml <http://pypi.python.org/pypi/lxml/>`_, which is one of the best HTML
parsing tools,more info and benchmarks can be found at
`habrahabr.ru <http://habrahabr.ru/post/163979/>`_ (in russian)

Additional
**********
Python 3.x, Django 1.5 `status <https://github.com/hellysmile/django-activeurl/issues/1>`_

*I will make python 3 port after django 1.5 stable will be released,
as soon as possible*

thnx `initializr <http://www.initializr.com/>`_ for easy to use html template
and nice one "fork me" `button <https://github.com/simonwhitaker/github-fork-ribbon-css>`_