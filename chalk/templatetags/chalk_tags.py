from django import template

from chalk.models import Article


register = template.Library()

@register.simple_tag
def chalk_latest_link():
    """
    Returns a link to the newest published article, or an empty string if no
    articles are found.

    """
    articles = Article.objects.filter(published=True)
    # Get latest article link, or empty string if no articles found
    try:
        article = articles[0]
    except IndexError:
        link = ''
    else:
        link = '<a href="%s">%s</a>' % (article.get_absolute_url(), article.title)
    return link

@register.inclusion_tag('chalk/latest_articles.html')
def chalk_latest_list(limit=5):
    """
    Returns a list of links to most recent articles.

    Fetches up to 5 articles by default but you can alter this by using the
    'limit' kwarg.

    """
    articles = Article.objects.filter(published=True)[:limit]
    return {'articles': articles}
