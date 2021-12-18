from django.contrib import admin
from django.urls import path

from table_task.views import TableView, TablePost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', TableView.as_view()),
    path('table/post/', TablePost.as_view()),
]
