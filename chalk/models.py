from datetime import date

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from docutils.core import publish_parts

from .settings import DOCUTILS_OVERRIDES


class Article(models.Model):
    """
    A chalk article or blog post.

    The content_html and excerpt_html fields are populated from the
    reStructuredText in content and excerpt. This HTML is regenerated
    on every model save unless the protect_html flag is set, in which
    case the HTML fields will not be changed automatically.

    """
    author = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    published = models.BooleanField()
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    protect_html = models.BooleanField(help_text='If checked, Content HTML and '
                                       'Excerpt HTML will not be overwritten '
                                       'by generated HTML')
    content_html = models.TextField('content HTML', blank=True)
    excerpt_html = models.TextField('excerpt HTML', blank=True)
    publication_date = models.DateField(default=date.today())
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publication_date']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Populate content_html and excerpt_html and save the model.

        If the protect_html flag is set, leave content_html and excerpt_html
        untouched.

        """
        if not self.protect_html:
            content_html, excerpt_html = self.generate_html()
            self.content_html = content_html
            self.excerpt_html = excerpt_html
        return super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_article', kwargs={'slug': self.slug})
    
    def generate_html(self):
        """
        Generate HTML from the content and excerpt fields.

        Returns the generated HTML as a (content, excerpt) tuple.

        """
        content = self.content
        excerpt = self.excerpt

        content_html = publish_parts(content,
                                     writer_name='html',
                                     settings_overrides=DOCUTILS_OVERRIDES)['fragment']
        excerpt_html = publish_parts(excerpt,
                                     writer_name='html',
                                     settings_overrides=DOCUTILS_OVERRIDES)['fragment']

        return (content_html, excerpt_html)
