from django.conf import settings
from .base import FunctionalTest
from .sever_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session

class MyListTest(FunctionalTest):
    
    def create_pre_authenticated_session(self, email):
        if self.against_staging:
            session_key = create_session_on_server(self.server_host, email)
        else:
            session_key = create_pre_authenticated_session(email)

        ## to set a cookie we need to first visit the domain.
        ## 404 pages load the quickest!
        self.browser.get(self.server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/',
         ))
