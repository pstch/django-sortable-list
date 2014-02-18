django-sortable-list [![Build Status](https://travis-ci.org/pstch/django-sortable-list.png?branch=master)](https://travis-ci.org/pstch/django-sortable-list)
========================
An extension of django's MultipleObjectMixin that provides sorting.

Based on [aptivate/django-sortable-listview](https://github.com/aptivate/django-sortable-listview) by Sarah Bird, forked to use a Mixin instead of a full ListView.

Features:
- Works with django's built in pagination.
- Adds an arrow to show the sort direction on the active sort.
- Knows what the next sort is (i.e. if you're already sorted by title in one direction, clicking on the title button/link again will sort it in the other direction).
- Lets you specify default sort for your list (defaults to -id) and for each of the sortable fields.
- Modifies the queryset, so your database does your sorting.

Install
=======
Using pip::

    pip install -e git+https://github.com/pstch/django-sortable-list.git#egg=django-sortable-list

Then, just use sortable_list.mixins.SortableListMixin

Example Project
===============
![Screenshot of example project](/example_project/screenshot.png)

To run the example project. First make sure django and django-sortable-list are on your python path. For example, from inside a virtualenv::

    pip install django
    pip install django-sortable-list

Then from your cloned folder::

    cd example_project
    python manage.py runserver

You should be able to see the example project at localhost:8000. A database is provided with some sample content. The username and password is admin/admin

Development and Tests
=====================

To run the tests::

    python setup.py test
