import django.forms as forms
from .models import News

class CommentForm(forms.Form):
    """
    Форма добавления комментария
    """
    text = forms.CharField()


class CreateNewsForm(forms.ModelForm):
    # image = forms.ImageField(label = "Изображение")
    # title = forms.CharField(label="Тема")
    # text = forms.CharField(label="Текст", widget=forms.Textarea)

    class Meta:
        model = News
        fields = (
            'title'
			,'text'
			,'image'
			# ,'created_date'
        )


# news = form.save(commit=False)
# news.author=request.user
# news.published_date=timezone.now()
# news.save()