from django.views.generic.base import ContextMixin
from django.views.generic.edit import ProcessFormView
from django.http import JsonResponse
from tags.models import Tag
from tags.forms import TagForm


class TagMixin(ContextMixin, ProcessFormView):
    """
    Mixin для создания формы тегов внутри формы создания поста
    """
    form = None
    tag_form = TagForm

    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tag_form'] = self.tag_form
        return context

    @staticmethod
    def ajax_add_tag(request):
        """
        добавление тега
        """
        response = {'status': 'OK'}
        try:
            new_tag = request.POST.get('tag')
            tag = Tag.objects.create(tag=new_tag)
            response.update(tag.as_dict())
        except:
            response.update({'status': "Тег уже существует!"})
        return JsonResponse(response)
