from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
import django.views as views
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import News, Comment
from django.utils import timezone
from django.template.context_processors import csrf
from .forms import CommentForm


class PaginatorMixin:

    @staticmethod
    def paginate(queryset, objects_per_page, page):
        paginator = Paginator(queryset, objects_per_page)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(1)
        return queryset


class NewsList(views.View, PaginatorMixin):
    """
    Список новостей с пагинацией
    """
    template_name = 'NewsApp/News.html'

    def get(self, request):
        context = {
            'user': request.user,
        }
        news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        news = self.paginate(news, 2, request.GET.get('page'))
        context.update({'News': news})
        return render(request, self.template_name, context)


class NewsDetail(views.View):
    """
    Представление новости
    """
    template_name = 'NewsApp/NewsDetail.html'

    def get(self, request, pk):
        context = {
            'user': request.user,
        }
        context.update(csrf(request))
        new = News.objects.get(pk=pk)
        comments = Comment.objects.filter(news=new)
        context.update({'post': new, 'comments': comments})
        return render(request, self.template_name, context)

    def post(self, request, pk):
        """
        Комментарии
        """
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/users/login')
        form = CommentForm(request.POST)
        new = News.objects.get(pk=pk)
        if form.is_valid():
            comment = Comment(
                author=request.user,
                text=form.cleaned_data.get('text'),
                news=new
            )
            comment.save()
        return HttpResponseRedirect(new.get_absolute_url())


class Detail(generic.DetailView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return News.objects.order_by('-pub_date')[:5]