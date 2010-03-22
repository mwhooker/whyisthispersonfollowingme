import logging

from pylons import url, config, request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from friendintersect.lib.base import BaseController, render
from friendintersect.lib.twitterapi import api

import json

log = logging.getLogger(__name__)

class IntersectsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""

    def index(self, format='html'):
        """GET /intersects: All items in the collection"""
        # url('intersects')

    def create(self):
        """POST /intersects: Create a new item"""
        # url('intersects')

    def new(self, format='html'):
        """GET /intersects/new: Form to create a new item"""
        # url('new_intersect')

    def update(self, id):
        """PUT /intersects/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('intersect', id=ID),
        #           method='put')
        # url('intersect', id=ID)

    def delete(self, id):
        """DELETE /intersects/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('intersect', id=ID),
        #           method='delete')
        # url('intersect', id=ID)

    def show(self, id, format='html'):
        """
        what relationship do I have to 'them'?

            * their friends who follow me (FFM)
            * their friends whom I follow (FIF)
        """

        their_id = request.params.get('their_id', None)
        if their_id is None:
            abort(400)

        my_friends = set(api.GetFriends(id))
        my_followers = set(api.GetFollowers(id))

        their_friends = set(api.GetFriends(their_id))
        #their_follows = api.GetFollowers(their_id)


        FFM = their_friends.intersection(my_followers)
        FIF = their_friends.intersection(my_friends)

        intersects = {'FFM': list(FFM), 'FIF': list(FIF)}

        if 'paste.testing_variables' in request.environ:
            request.environ['paste.testing_variables']['intersects'] = intersects

        return json.dumps(intersects)
        
        

        

    def edit(self, id, format='html'):
        """GET /intersects/id/edit: Form to edit an existing item"""
        # url('edit_intersect', id=ID)
