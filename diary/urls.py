from django.urls import path, include
from . import views
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('<uuid:diary_id>/settings/', views.diary_config, name='diary_config'),
    # path('create/', views.create_entry, name='create_entry'),
    path('<uuid:entry_id>/', views.entry, name='entry'),
    path('<uuid:entry_id>/edit', views.edit_entry, name='edit_entry'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
