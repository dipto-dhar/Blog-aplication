from django.conf import urls
from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
      path('', views.index,name=""),
      path('home', views.index,name="home"),
      path('about', views.about,name="about"),
      path('contact', views.contact,name="contact"),
      path('categories', views.category,name="categories"),
      path('category/<slug>', views.single_category,name="category"),
      path('post/<slug>', views.show_single_post,name="post"),
      

 ]
if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)