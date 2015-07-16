from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import *
from blog.forms import *

def main(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created_on")
    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("blog/list.html", dict(posts=posts, user=request.user))


def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        #post.author = request.user
        post.save()
        return redirect('/post')
    return render_to_response('blog/add_post.html', 
                              { 'form': form },
                              context_instance=RequestContext(request))

def view_post(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render_to_response('blog/blog_post.html',
                              {
                                  'post': post,
                                  'form': form,
                              },
                              context_instance=RequestContext(request))


'''def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("dbe.blog.views.post", args=[pk]))'''
