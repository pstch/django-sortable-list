"""django-sortable-list provides a SortableListMixin that provides
sorting functionality for list views

Modules :
-- mixins : sort mixin

"""
__title__ = 'django-sortable-list'
__version__ = '0.3'
__author__ = 'Sarah Bird (original), Hugo Geoffroy'
__license__ = 'See LICENSE'
__copyright__ = "Copyright 2013 Sarah Bird" \
", and individual contributors. All rights" \
"reserved."

from django_sortable_list.mixins import SortableListMixin

__all__ = ['SortableListMixin,']
