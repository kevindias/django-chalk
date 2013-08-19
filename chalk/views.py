from django.views.generic import DetailView, ListView

from .models import Article


class ArticleList(ListView):
    """
    List all articles by publication date descending.

    The default template extends the 'container' block of 'base.html'
    and is meant mostly as an example. Override 'chalk/article_list.html'
    to use your own template.

    Articles are provided to the template context in the 'article_list'
    variable.

    """
    model = Article

    def get_queryset(self):
        """Non-staff users only see published articles."""
        qs = self.model.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(published=True)
        return qs


class ArticleView(DetailView):
    """
    Show a detailed view of a single article.

    The default template extends the 'container' block of 'base.html'
    and is meant mostly as an example. Override 'chalk/article_detail.html'
    to use your own template.

    You can access the article being viewed through the 'article' variable
    in the template context.

    """
    model = Article

    def get_queryset(self):
        """Non-staff users only see published articles."""
        qs = self.model.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(published=True)
        return qs
