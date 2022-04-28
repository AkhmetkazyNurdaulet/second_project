from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'kaz'

urlpatterns = [
    path('', views.home, name='home'),
    path('tours/', views.tours, name='tours'),
    path('tourists/', views.tourists, name='tourists'),
    path('registration/', views.reg, name='registration'),
    path('info/', views.info, name='info'),
    path('update/<int:post_id>', views.update_tour),
    path('delete/<int:post_id>', views.delete_tour),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('cat/', views.cat, name='cat'),
    path('list_cat/', views.list_cat, name='list_cat'),
    path('send/', views.send_message),

    

]

urlpatterns += staticfiles_urlpatterns()