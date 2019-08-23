from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.urls import reverse_lazy

from .models import Category, Post, Tag
from .forms import ContactForm
# Create your views here.
class PostListView(ListView):
    model = Post
    paginate_by = 3

    def get_queryset(self):
        if 'catd' in self.kwargs:
            queryset = Post.objects.filter(categories__title=self.kwargs['catd']).order_by('-created')
        elif 'q' in self.request.GET:
            queryset = Post.objects.filter(
                Q(title__icontains=self.request.GET['q']) |
                Q(text__icontains=self.request.GET['q'])
            ).distinct().order_by('-created')
        else:
            queryset = Post.objects.all().order_by('-created')

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        objects = super().get_context_data(**kwargs)
        objects['categories'] = Category.objects.filter(activate=True)
        return objects

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        objects = super().get_context_data(**kwargs)
        objects['categories'] = Category.objects.filter(activate=True)
        self.object.visits += + 1
        self.object.save()
        return  objects

class ContactView(FormView):
    template_name = 'blog/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blog:contact_form')

    def form_valid(self, form):
        try:
            send_mail(form.cleaned_data['subject'], form.cleaned_data['message'] , form.cleaned_data['from_email'], ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return super().form_valid(form)




