from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
import logging

logger = logging.getLogger(__name__)
# Create your views here.

def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  logger.debug("Got %d posts",len(posts))
  context = {'posts':posts}
  return render(request,'blog/index.html',context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # comment_form = None  # Initialize the variable outside the conditional blocks

    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                logger.info(
                  "Created comment on Post %d for user %s", post.pk, request.user
                )
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()  # Initialize comment_form for GET requests
    else:
        comment_form = None  # Set comment_form to None if the user is not active

    context = {'post': post, 'comment_form': comment_form}
    return render(request, 'blog/post-detail.html', context)



