from django.conf import settings


FEED_TITLE = getattr(settings, 'CHALK_FEED_TITLE', 'Article Feed')
FEED_DESCRIPTION = getattr(settings, 'CHALK_FEED_DESCRIPTION', 'All Articles')
