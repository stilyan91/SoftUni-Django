from django.urls import path
from .views import list_view, ArticlesListView, RedirectToArticleView, ArticleDetailView, ArticleCreateView, \
    ArticleDeleteView

urlpatterns = [
    path('', list_view),
    path('cbv/', ArticlesListView.as_view(), name='list_articles_cbv'),
    path('cbv/<int:pk>/', ArticleDetailView.as_view(), name='article_details_cbv'),
    path('redirect-to-articles', RedirectToArticleView.as_view(), name='redirect_to_articles'),
    path('cbv/create/', ArticleCreateView.as_view(), name='article_create_cbv'),
    path('cbv/delete/<int:pk>', ArticleDeleteView.as_view(), name='delete_article')

]