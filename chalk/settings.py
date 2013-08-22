from django.conf import settings


# Used as the title for RSS and Atom feeds of articles.
# Set CHALK_FEED_TITLE in your settings.py to override.
FEED_TITLE = getattr(settings, 'CHALK_FEED_TITLE', 'Article Feed1')

# Used as the feed description (RSS) or subtitle (Atom) for article feeds.
# Set CHALK_FEED_DESCRIPTION in your settings.py to override.
FEED_DESCRIPTION = getattr(settings, 'CHALK_FEED_DESCRIPTION', 'All Articles1')
