import logging

from pylons import url, config, request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from friendintersect.lib.base import BaseController, render
from friendintersect.lib.twitterapi import thesocial, peeps, nolimits

import json


log = logging.getLogger(__name__)

class IntersectsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""

    def show(self, id, format='html'):
        """
        what relationship do I have to 'them'?

            * their friends who follow me (FFM)
            * their friends whom I follow (FIF)
            * their followers I follow (FFI)
        """

        their_id = request.params.get('their_id', None)
        if their_id is None:
            abort(400)

        my_friends = set(thesocial.GetFriends(id))
        my_followers = set(thesocial.GetFollowers(id))

        their_friends = set(thesocial.GetFriends(their_id))
        their_followers = set(thesocial.GetFollowers(their_id))

        FFM = their_friends.intersection(my_followers)
        FIF = their_friends.intersection(my_friends)
        FFI = their_followers.intersection(my_friends)

        intersects = {'FFM': peeps.Lookup(list(FFM)), 'FIF':
                      peeps.Lookup(list(FIF)), 'FFI': peeps.Lookup(list(FFI))}

        log.info("remaining requests: %s" % nolimits.get())

        if 'paste.testing_variables' in request.environ:
            request.environ['paste.testing_variables']['intersects'] = intersects

        if format == 'json':
            return json.dumps(intersects)
        if format == 'html':
            c.intersects = intersects
            return render('intersects.mako')

