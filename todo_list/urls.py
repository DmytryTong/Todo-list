from django.urls import path

from todo_list.views import TaskListView, TagListView

urlpatterns = [
    path(
        "",
        TaskListView.as_view(),
        name="tasks-list",
    ),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="tasks-create",
    ),
    path(
        "<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="tasks-update",
    ),
    path(
        "<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="tasks-delete",
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tags-list",
    ),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tags-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tags-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tags-delete",
    ),
]

app_name = "todo_list"