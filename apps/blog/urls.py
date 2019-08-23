from django.urls import path

from .views import PostListView, PostDetailView, ContactView

# Personalized urls from the app
app_name = 'blog'

urlpatterns = [
    # path('url/' , views.function, name='url_name')
    path( '',PostListView.as_view(), name='post_list'),
    path('post/<slug>', PostDetailView.as_view(), name='post_detail'),
    path('<str:catd>/', PostListView.as_view(), name='post_catd_list'),
    path('contact/form/', ContactView.as_view(), name='contact_form'),
]