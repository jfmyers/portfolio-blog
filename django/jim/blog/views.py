from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from blog.forms import CommentForm
from blog.models import Post,Comment

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')
        
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        comments = Comment.objects.filter(post_id=post_id).order_by('-pub_date')
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blog/detail.html', {'post': post,'comment_list':comments})

def results(request, post_id):
    return HttpResponse("You're looking at the results of post %s." % post_id)

def comment(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post:detail', args=(p.id,)))
        else:
            form = CommentForm(request.POST)
            c = {'form':form}  
            return HttpResponseRedirect(reverse('post:detail', args=(p.id,)))
            #return HttpResponse("You're looking at the comments of post %s." % c)
            
    return HttpResponseRedirect('/post/' % post_id)