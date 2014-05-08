from django.conf.urls import patterns, url
from misterprofessor import views

urlpatterns = patterns('',
    url(r'^index/$', views.index, name='index'),
    url(r'^index/(?P<code>\w+)/$', views.index, name='postSubscription'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search/result$', views.searchresult, name='searchresult'),
    url(r'^course/(?P<code>\w+)/(.|$)', views.course, name='course'),
    url(r'^profile/(?P<code>\w+)/(.|$)', views.profile, name='profile'),
    url(r'^profile/$', views.profile, name='myprofile'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/post$', views.settingspost, name='settingspost'),
    url(r'^$', views.first, name='first'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^subscription/(?P<code>\w+)/$', views.course_subscription, name='subscription'),
    url(r'^error$', views.error, name='error'),
    url(r'^logout$', views.logout_view, name='logout'), 
)
