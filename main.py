#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.ext import db
import Model
import os
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = "Welcome, %s!" % user.nickname()
            url = users.create_logout_url("/")
            action = "Sign out"
            resume = Model.Resume(key_name=user.user_id(), g_user=user)
            resume.emails.append(db.Email(user.email()))
            resume.put()
        else:
            greeting = "Log in or Register!"
            url = users.create_login_url("/")
            action = "Sign in"

        template_values = {'greeting': greeting,
                           'url': url,
                           'content': 'frontpage.html',
                           'sign_inout': action
                           }
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
