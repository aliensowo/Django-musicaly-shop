from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from knowledge.models import Article


class ESearchView(View):
    template_name = 'search/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_articles = Article.objects.filter(article_content__search=question)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_articles, 10)

            page = request.GET.get('page')
            try:
                context['article_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['article_lists'] = current_page.page(1)
            except EmptyPage:
                context['article_lists'] = current_page.page(current_page.num_pages)

        return render_to_response(template_name=self.template_name, context=context)