from django.shortcuts import render
from django.views import generic

from .models import News

# Create your views here.
class Detail(generic.DetailView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return News.objects.order_by('-pub_date')[:5]
