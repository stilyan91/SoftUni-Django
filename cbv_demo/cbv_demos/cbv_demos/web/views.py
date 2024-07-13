from django import forms
from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from cbv_demos.web.models import Articles

from django.template import engines

engine = engines['django']


# View in Django:
# 1. The view must be 'callable'
# 2. Return HttpResponse object


def list_view(request):
    article = Articles.objects.all()
    context = {'articles': article}
    return render(request, 'articles.list.html', context)


# generic.CreateView
# generic.ListView
# generic.DetailView
# generic.UpdateView
# generic.DeleteView


class BaseView:
    def post(self, request):
        pass

    def get(self, request):
        pass

    @classmethod
    def as_view(cls):
        self = cls()

        def view(request):
            if request.method == "GET":
                return self.get(request)
            else:
                return self.post(request)

        return view


# class ArticleView(BaseView):
# class ArticleView(generic.View):
#     def post(self, request):
#         pass
#
#     def get(self, request):

#       #def get_context_data()...
#         context = {
#             'articles': Articles.objects.all()
#         }
#          #render_to_response()
#         return render(request, 'articles.list.html', context=context)


# class ArticleView(generic.TemplateView):
#     template_name = 'articles.list.html'
#
#     # template_engine =  django.templates
#
#     # extra_context = {
#     #     'articles': Articles.objects.all(),
#     # } == get_context_data = {}
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Articles.objects.all()
#         return context


# reverse() vs reverse_lazy()


class RedirectToArticleView(generic.RedirectView):
    url = reverse_lazy('list_articles_cbv')


class ArticlesListView(generic.ListView):
    template_name = 'articles.list.html'
    model = Articles

    # context_object_name = 'articles_list' # use the default - 'object_list'
    # paginate_by = 5

    # Article.object.filter(name_icontains=search)...
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class ArticleDetailView(generic.DetailView):
    model = Articles
    template_name = 'articles.detail.html'
    # pk_ulr_kwarg = 'id'

    # /pk
    # /slug
    # /pk/slug, /slug/pk


class ArticleForm(forms.ModelForm):
    pass


# Forms:
# 1. Auto created based on fields (default)
# 2. 'form_class' - return class
# 3. 'get_form_class' - return class
# 4. overwrite get_form - return instance

class DisabledFormFieldsMixin:
    disabled_fields = []

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'
            form.fields[field].widget.attrs['readonly'] = 'readonly'

        return form


class ArticleCreateView(DisabledFormFieldsMixin, generic.CreateView, ):
    model = Articles
    template_name = 'articles.create.html'
    fields = ['title', 'content']  # '__all__'
    disabled_fields = ['title']
    success_url = reverse_lazy('list_articles_cbv')

    # form_class = modelform_factory(
    #     Articles,
    #     fields=['title', 'content'],
    #     widgets={
    #         'title': forms.TextInput(
    #             attrs={'class': 'abv'}
    #         )
    #     }
    # )

    # def get_form(self, *args, **kwargs):
    #     form = super().get_form(*args, **kwargs)
    #
    #     for field in self.disabled_fields:
    #         form.fields[field].widget.attrs['disabled'] = 'disabled'
    #
    #     return form

    # form_class = ArticleForm // customize the form , if we want to overwrite clean_data, valid_form or customize the form.save()
    # def get_form_class(self):
    #   pass

    # get_form(self, form_class = None):
    #   pass


class ArticleUpdateView(generic.UpdateView, ):
    model = Articles
    fields = ['title', 'content']
    template_name = 'article.update_template.html'


class ArticleDeleteView(DisabledFormFieldsMixin, generic.DeleteView, ):
    model = Articles
    template_name = 'articles.delete.html'
    form_class = modelform_factory(Articles, fields=('title', 'content'), widgets={
        'title': forms.TextInput(attrs={'class': 'form-control'}),
    })
    disabled_fields = ['title', 'content']

    def form_valid(self, form):
        # on success
        pass

    def form_invalid(self, form):
        # on not success
        pass
