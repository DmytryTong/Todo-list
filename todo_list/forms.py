from django import forms

from todo_list.models import Task, Tag


class TaksCreationForm(forms.Form):
    class Meta:
        model = Task
        fields = "__all__"


class TagsCreationForm(forms.Form):
    class Meta:
        model = Tag
        fields = "__all__"
