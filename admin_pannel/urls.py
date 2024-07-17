from django.conf import urls
from django.urls import path
from admin_pannel import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
      path('', views.admin_login,name=""),
      path('logout', views.admin_logout,name="logout"),
      path('dashboard', views.admin_login,name="dashboard"),
      path('admin_pannel', views.admin_login,name="admin_pannel"),
      path('my-profile', views.profile,name="my-profile"),
      path('add-user', views.admin_register,name="add-user"),
      path('add-post', views.add_post,name="add-post"),
      # path('save-post', views.save_post,name="save-post"),
      path('posts', views.show_posts,name="posts"),
      path('settings', views.settings,name="settings"),
      path('edit-post/<int:pk>', views.edit_posts,name="edit-post"),
      path('delete-post/<int:pk>', views.delete_posts,name="delete-post"),
      path('categories', views.show_categories,name="categories"),
      path('add-category', views.add_category,name="add-category"),
      path('edit-category/<int:pk>', views.edit_category,name="edit-category"),
      path('delete-category/<int:pk>', views.delete_category,name="delete-category"),
      path('mails', views.mails,name="mails"),
      path('delete-mail/<int:pk>', views.delete_mail,name="delete-mail"),
      path('delete-contact/<int:pk>', views.delete_contact,name="delete-contact"),
      path('contacts', views.contact,name="contacts"),
      path('about-page', views.about,name="about-page"),
 ]
if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)