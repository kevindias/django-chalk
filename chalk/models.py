from datetime import date

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from docutils.core import publish_parts


DOCUTILS_OVERRIDES = {
    'syntax_highlight': 'short',
    'initial_header_level': 2,
    'doctitle_xform': False,
}


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    published = models.BooleanField()
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    protect_html = models.BooleanField()
    content_html = models.TextField(blank=True)
    excerpt_html = models.TextField(blank=True)
    publication_date = models.DateField(default=date.today())
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publication_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_article', kwargs={'slug': self.slug})
    
    def generate_html(self):
        content = self.content
        excerpt = self.excerpt

        content_html = publish_parts(content,
                                     writer_name='html',
                                     settings_overrides=DOCUTILS_OVERRIDES)['fragment']
        excerpt_html = publish_parts(excerpt,
                                     writer_name='html',
                                     settings_overrides=DOCUTILS_OVERRIDES)['fragment']

        return (content_html, excerpt_html)

    def save(self, *args, **kwargs):
        if not self.protect_html:
            content_html, excerpt_html = self.generate_html()
            self.content_html = content_html
            self.excerpt_html = excerpt_html
        return super(Article, self).save(*args, **kwargs)
