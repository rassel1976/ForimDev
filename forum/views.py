from datetime import datetime, timezone

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views import generic
from django.views.generic import FormView
from django.views.generic import View

from forum.forms import CommentForm, PostForm
from forum.models import Post, Comment


class IndexView(generic.ListView):
    template_name = "forum/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        return Post.objects.order_by()[:]

def detailView(request, post_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['Post'] = Post.objects.get(id=post_id)
    args['comments'] = Comment.objects.filter(comment_post_id=post_id)
    args['form'] = comment_form
    args['request'] = request
    return render_to_response('forum/detail.html', args)


def addComment(request, post_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post = Post.objects.get(id=post_id)
            comment.comment_name = request.user.username
            comment.save()
    return redirect('/forum/%s/' % post_id)


class CreatePostForm(FormView):
    form_class = PostForm
    success_url = '/forum/'
    template_name = "forum/createpost.html"

    def form_valid(self, form):
        instanse = form.save(commit=False)
        instanse.post_user = self.request.user.username
        #print(self.request.user.username)

        instanse.save()

        return redirect(self.get_success_url())

class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = '/forum/login/'
    template_name = "forum/register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView,self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "forum/login.html"

    success_url = '/forum/'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request,self.user)
        return super(LoginFormView,self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/forum/")