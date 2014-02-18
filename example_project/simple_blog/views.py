from django.views.generic import ListView
from django_sortable_list.mixins import SortableListMixin

from .models import Article

class ArticleListView(SortableListMixin, ListView):
    allowed_sort_fields = {'title': {'default_direction': '',
                                     'verbose_name': 'Title'},
                           'published_date': {'default_direction': '-',
                                              'verbose_name': 'Published On'}}
    default_sort_field = 'published_date'
    paginate_by = 5
    template_name = 'list.html'
    model = Article
