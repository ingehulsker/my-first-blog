from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'', include('blog.urls')),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
