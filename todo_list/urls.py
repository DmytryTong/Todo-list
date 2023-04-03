from django.urls import path

from todo_list.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    change_complete_status,
)

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
    path(
        "change_complete_status/<int:pk>/",
        change_complete_status,
        name="change-complete-status",
    ),
]

app_name = "todo-list"
