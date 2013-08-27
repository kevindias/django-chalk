from datetime import date

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import strip_tags

from docutils.core import publish_parts

from .settings import DOCUTILS_OVERRIDES


# Safe version of settings.AUTH_USER_MODEL for Django < 1.5
auth_user_model = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Article(models.Model):
    """
    A chalk article or blog post.

    The content_html and excerpt_html fields are populated from the
    reStructuredText in content and excerpt. This HTML is regenerated
    on every model save unless the protect_html flag is set, in which
    case the HTML fields will not be changed automatically.

    """
    author = models.ForeignKey(auth_user_model)
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
    meta_description = models.TextField(blank=True,
                                        help_text='If this is blank the '
                                        'get_meta_description method returns '
                                        'a plaintext version of excerpt_html')
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
        # Ensure that if meta_description appears empty to the user then it is
        # saved as an empty field. Prevents accidentally-inserted whitespace
        # from causing a blank description.
        self.meta_description = self.meta_description.strip()
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

    def get_meta_description(self):
        """
        Returns contents of meta_description field unless it's empty, in which
        case we strip tags from excerpt_html and return resulting text.

        """
        if self.meta_description:
            return self.meta_description
        # Extra strip() removes newlines, which can break some parsers
        desc = strip_tags(self.excerpt_html).strip()
        return desc
