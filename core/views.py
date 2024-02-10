# comments/views.py

from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from .models import Comment, Post
from .forms import *

def home(request): 
    return render(request,'comments/base.html')
def postPage(request, id):
    response_form = CommentForm()
    reply_form = ReplyForm()

    if request.method == 'POST':
        try:
            response_form = CommentForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.post = Post(id=id)
                response.save()
                return redirect('/post/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            raise

    post = Post.objects.get(id=id)
    # responses = Question.get_response()
    # response = Response.get_response()
    comments = Comment.objects.filter(parent_comment = None,post = post)
    context = {
        'post': post,
        'comment_form': response_form,
        'reply_form': reply_form,
        'comments':comments
        # 'responses':responses,
        # 'response':response
    }
    return render(request, 'comments/post_detail.html', context)


def replyPage(request):
    if request.method == 'POST':
        try:
            form = ReplyForm(request.POST)
            if form.is_valid():
                post_id = request.POST.get('post')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                reply.user = request.user
                reply.post = Post(id=post_id)
                reply.parent_comment = Comment(id=parent_id)
                reply.save()
                return redirect('/post/'+str(post_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            raise

    return redirect('index')