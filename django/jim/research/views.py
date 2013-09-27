from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from research.models import Paper

class IndexView(generic.ListView):
    template_name = 'research/index.html'
    context_object_name = 'latest_paper_list'

    def get_queryset(self):
        """Return papers."""
        return Paper.objects.order_by('-title')