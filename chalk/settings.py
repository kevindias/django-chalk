from django.conf import settings


# Used as the title for RSS and Atom feeds of articles.
# Set CHALK_FEED_TITLE in your settings.py to override.
FEED_TITLE = getattr(settings, 'CHALK_FEED_TITLE', 'Article Feed1')

# Used as the feed description (RSS) or subtitle (Atom) for article feeds.
# Set CHALK_FEED_DESCRIPTION in your settings.py to override.
FEED_DESCRIPTION = getattr(settings, 'CHALK_FEED_DESCRIPTION', 'All Articles1')

# Docutils config options.
# See: http://docutils.sourceforge.net/docs/user/config.html
# This dictionary is passed as the settings_overrides argument
# of docutils.core.publish_parts
# Set CHALK_DOCUTILS_OVERRIDES in your settings.py to override.
DOCUTILS_OVERRIDES = {
    'syntax_highlight': 'short',
    'initial_header_level': 2,
    'doctitle_xform': False,
}

DOCUTILS_OVERRIDES.update(
    getattr(settings, 'CHALK_DOCUTILS_OVERRIDES', {})
)
