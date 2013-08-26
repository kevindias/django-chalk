from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Article


class ArticleViewTests(TestCase):
    """Test article views."""
    fixtures = ['chalk_test_data.json']

    def test_list_view(self):
        """Should only return published articles for non-staff users."""
        published_articles = Article.objects.filter(published=True)
        response = self.client.get(reverse('list_articles'))
        returned_articles = response.context['article_list']
        self.assertItemsEqual(returned_articles, published_articles)

    def test_detail_view(self):
        """Check that article detail view returns correct article."""
        article = Article.objects.filter(published=True)[0]
        response = self.client.get(reverse('view_article',
                                           kwargs={'slug': article.slug}))
        returned_article = response.context['article']
        self.assertEqual(article, returned_article)

    def test_detail_view_unpublished(self):
        """Unpublished articles should return 404 for non-staff users."""
        article = Article.objects.filter(published=False)[0]
        response = self.client.get(reverse('view_article',
                                           kwargs={'slug': article.slug}))
        self.assertEqual(response.status_code, 404)



class ArticleModelTests(TestCase):
    """Test the Article model."""
    fixtures = ['chalk_test_data.json']

    def test_save(self):
        """Saving should populate HTML fields by default."""
        article = Article.objects.get(title="Test Title") #From fixture
        article.content_html = "content to be overwritten"
        article.excerpt_html = "excerpt to be overwritten"
        article.save()
        self.assertEqual(article.content_html, "<p>Some content</p>\n")
        self.assertEqual(article.excerpt_html , "<p>An excerpt</p>\n")

    def test_protect_html(self):
        """Article.protect_html should prevent HTML overwrites."""
        article = Article.objects.get(title="Test Title") #From fixture
        article.protect_html = True
        article.content_html = "Protected Content"
        article.excerpt_html = "Protected Excerpt"
        article.save()
        self.assertEqual(article.content_html, "Protected Content")
        self.assertEqual(article.excerpt_html , "Protected Excerpt")

    def test_meta_description_default(self):
        """
        Article.get_meta_description should be equivalent to Article.excerpt if
        Article.meta_description is empty.

        """
        article = Article.objects.get(title="Test Title") #From fixture
        article.excerpt = "A blurb about nothing."
        article.meta_description = " "
        article.save()
        self.assertEqual(article.get_meta_description(), "A blurb about nothing.")

    def test_meta_description_custom(self):
        """
        Article.get_meta_description should return Article.meta_description if
        it isn't empty.

        """
        article = Article.objects.get(title="Test Title") #From fixture
        article.meta_description = "A custom description"
        article.save()
        self.assertEqual(article.get_meta_description(), "A custom description")

    def test_generate_html(self):
        """Articles should generate correct HTML from reST input."""
        excerpt = """Here's a bit of `reStructuredText`_ for *testing* purposes.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
"""

        expected_html = ("""<div class="section" id="glorious-content">
<h2>Glorious Content</h2>
<p>What about an internal reference to a <a class="reference internal" href="#section">Section</a>?</p>
<div class="section" id="section">
<h3>Section</h3>
<p>Great.</p>
</div>
</div>
""",
"""<p>Here's a bit of <a class="reference external" href="http://docutils.sourceforge.net/rst.html">reStructuredText</a> for <em>testing</em> purposes.</p>
""")

        content = """Glorious Content
----------------

What about an internal reference to a `Section`_?

Section
=======

Great."""

        article = Article.objects.get(title="Test Title") #From fixture
        article.excerpt = excerpt
        article.content = content

        self.assertEqual(article.generate_html(), expected_html)
