from django.forms import ModelForm
from blog.models import Tag


class TagForm(ModelForm):
    """
    Форма создания тега
    """
    class Meta:
        model = Tag
        fields = ['tag']
