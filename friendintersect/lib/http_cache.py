
class HttpCache(object):
    def on_response(self, http_client):
        pass

    def on_request(self, req):

        """
        if etag:
            request.add_header('If-None-Match', etag)
        if type(modified) == type(''):
            modified = _parse_date(modified)
        if modified:
            # format into an RFC 1123-compliant timestamp. We can't use
            # time.strftime() since the %a and %b directives can be affected
            # by the current locale, but RFC 2616 states that dates must be
            # in English.
            short_weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            request.add_header('If-Modified-Since', '%s, %02d %s %04d %02d:%02d:%02d GMT' % (short_weekdays[modified[6]], modified[2], months[modified[1] - 1], modified[0], modified[3], modified[4], modified[5]))    
        """

