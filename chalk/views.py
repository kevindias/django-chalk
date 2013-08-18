from django.views.generic import DetailView, ListView

from .models import Article


class ArticleList(ListView):
    model = Article

    def get_queryset(self):
        qs = self.model.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(published=True)
        return qs


class ArticleView(DetailView):
    model = Article

    def get_queryset(self):
        qs = self.model.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(published=True)
        return qs
