from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from bio.models import Bio

def index(request):
    bio = Bio.objects.get(pk=1)
    context = {'bio': bio}
    return render(request, 'bio/index.html', context)