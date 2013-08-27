Simple reStructuredText blogging for Django
===========================================

Summary
-------

Chalk is a basic blogging app for `Django`_ which lets you write posts using
`reStructuredText`_. It was written for personal use and I'll be adding
features as I need them but if you end up finding it useful and would like to
see anything added then I'd like to hear from you. Either email me at
kevin@kevindias.com or open an issue in the `Bitbucket repo`_.

Installing django-chalk
-----------------------

There are several ways to install this application.

Using pip or easy_install
^^^^^^^^^^^^^^^^^^^^^^^^^

Pip is the recommended package-installation tool for Python. To install
django-chalk with pip, use the command::

    pip install django-chalk

If you prefer to use easy_install then replace ``pip`` with ``easy_install``
in the above command.

To install the latest in-development version (which may not be stable) directly
from the project's Git repository you can use the command::

    pip install -e git+https://bitbucket.org/dias.kev/django-chalk.git#egg=chalk

Using setuptools
^^^^^^^^^^^^^^^^

Download the package source code or distribution tarball and then run the
following command in the django-chalk directory::

    python setup.py install


Configuring django-chalk
------------------------

Settings and models
^^^^^^^^^^^^^^^^^^^

Add ``chalk`` to the ``INSTALLED_APPS`` setting of your project. Once you've done
this you can create chalk's database tables using ``manage.py syncdb``.

Setting up URLs
^^^^^^^^^^^^^^^

All the URLs which chalk needs are set in ``chalk.urls`` so you can simply
include that file in your project's root URLconf. For example, to add chalk
to your project under the path ``/blog/`` you would add the following to your
root URLconf::

    (r'^blog', include('chalk.urls')),

With this setup chalk all articles are listed at the URL ``/blog/`` and
individual articles can be found at ``/blog/[article_slug]/``

Templates
^^^^^^^^^

Chalk includes bare-bones examples of the templates it needs but these may not
work with your project's template structure and even if they do you'll probably
want to override them. The templates to override are
``chalk/article_list.html`` which displays a list of all articles and
``chalk/article_detail.html`` which displays individual articles.


Reporting problems or suggesting improvements
---------------------------------------------

Please use the issue tracker at the project's `Bitbucket repo`_



.. _Bitbucket repo: https://bitbucket.org/dias.kev/django-chalk/
.. _Django: https://www.djangoproject.com/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
