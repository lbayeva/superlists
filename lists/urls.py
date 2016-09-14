from django.conf.urls import url
from lists import views
from lists.views import NewListView

urlpatterns = [
    url(r'^new$', NewListView.as_view(), name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
]
