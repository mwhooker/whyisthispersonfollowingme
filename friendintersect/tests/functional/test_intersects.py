from friendintersect.tests import *
from friendintersect.tests.test_models import TwitterMock
import friendintersect.controllers.intersects

friendintersect.controllers.intersects.api = TwitterMock()

"""
The User structure exposes the following properties:
     
    user.id
    user.name
    user.screen_name
    user.location
    user.description
    user.profile_image_url
    user.profile_background_tile
    user.profile_background_image_url
    user.profile_sidebar_fill_color
    user.profile_background_color
    user.profile_link_color
    user.profile_text_color
    user.protected
    user.utc_offset
    user.time_zone
    user.url
    user.status
    user.statuses_count
    user.followers_count
    user.friends_count
    user.favourites_count
"""
class TestIntersectsController(TestController):


    def test_show(self):
        response = self.app.get(url('intersects', id=TwitterMock.ME,
                                    their_id=TwitterMock.THEM))
        intersects = response.intersects
        
#FFM
        assert intersects['FFM'] == [3]

#FIF
        assert intersects['FIF'] == [5]

"""
    def test_show_as_xml(self):
        response = self.app.get(url('formatted_intersect', id=1, format='xml'))
"""
