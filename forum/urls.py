from django.conf.urls import url

from forum import views

app_name = 'forum'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detailView, name='detail'),
    url(r'^(?P<post_id>[0-9]+)/addcomment/$',views.addComment),
    url(r'^createpost/', views.CreatePostForm.as_view()),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),

]
