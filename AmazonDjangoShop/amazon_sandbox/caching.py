import os
import tempfile
from lxml import etree

try: # make it python2.4 compatible!
    from hashlib import md5 # pylint: disable-msg=E0611
except ImportError: # pragma: no cover
    from md5 import new as md5

from amazonproduct.api import API

DEFAULT_CACHE_DIR = tempfile.mkdtemp(prefix='amzn_')

class ResponseCachingAPI (API):

    """
    This API stores each response from Amazon in an XML file and uses these for
    subsequent requests. File are name with a hash based on submitted parameters
    in URL (excluding Timestamp and Signature).

    Using this class is an excellent idea during development!

    This class is based on code by Dmitry Chaplinsky
    https://gist.github.com/657174
    """

    def __init__(self, access_key_id, secret_access_key, locale, associate_tag,
                 cachedir=DEFAULT_CACHE_DIR, **kwargs):
        """
        :param cachedir: Path to directory containing cached responses.
        """
        API.__init__(self, access_key_id, secret_access_key, locale, associate_tag, **kwargs)
        self.cache = cachedir
        if self.cache and not os.path.isdir(self.cache):
            os.mkdir(self.cache)

    def _fetch(self, url):
        if self.cache:
            path = os.path.join(self.cache, '%s.xml' % self.get_hash(url))
            # if response was fetched previously, use that one
            if os.path.isfile(path):
                return open(path)

        # fetch original response from Amazon
        resp = API._fetch(self, url)

        if self.cache:
            fp = open(path, 'w+')
            fp.write(etree.tostring(etree.parse(resp), pretty_print=True))
            fp.seek(0)
            return fp

        return resp

    @staticmethod
    def get_hash(url):
        """
        Calculate hash value for request based on URL.
        """
        cachename = "&".join([chunk for chunk in url.split('&')
              if chunk.find('Timestamp') != 0 and chunk.find('Signature') != 0])
        return md5(cachename).hexdigest()
