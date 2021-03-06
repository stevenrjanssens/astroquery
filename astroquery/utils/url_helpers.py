import six
import os.path


def urljoin_keep_path(url, path):
    """Join a base URL and a relative or absolute path. The important
    difference to :func:`urlparse.urljoin` (or
    :func:`urllib.parse.urljoin` on Python 3) is that `urljoin_keep_path`
    does not remove the last directory of the path found in the parameter
    `url` if it is in relative form. Compare the examples below to verify.

    Examples
    --------
    >>> urljoin_keep_path('http://example.com/foo', 'bar')
    'http://example.com/foo/bar'
    >>> try:
    ...     import urlparse
    ... except ImportError:
    ...     import urllib.parse as urlparse
    ...
    >>> urlparse.urljoin('http://example.com/foo', 'bar')
    'http://example.com/bar'

    """
    # urlparse.SplitResult doesn't allow overriding attribute values,
    # so ``splitted_url.path = ...`` is not possible here, unfortunately.
    splitted_url = six.moves.urllib_parse.urlsplit(url)
    return six.moves.urllib_parse.SplitResult(
        splitted_url.scheme,
        splitted_url.netloc,
        os.path.join(splitted_url.path, path),
        splitted_url.query,
        splitted_url.fragment).geturl()