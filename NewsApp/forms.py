import django.forms as forms


class CommentForm(forms.Form):
    """
    Форма добавления комментария
    """
    text = forms.CharField()
