'''
Created on 10.05.2011

@author: dfyz
'''
import os
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

PROJECT_PATH = os.path.dirname(__file__)

def template_pattern(temp):
    return os.path.join(PROJECT_PATH,'templates',temp)

def foto_parser(img_path=''):
    return os.listdir(os.path.join(PROJECT_PATH,img_path)) 

class Main(webapp.RequestHandler):
    def get(self):
        path = template_pattern('main.html')
        template_values = {'content_template':'dfyz.html'}           
        self.response.out.write(template.render(path, template_values))

class Contact(webapp.RequestHandler):
    def get(self):
        path = template_pattern('main.html')
        template_values = {'content_template':'contact.html'}
        self.response.out.write(template.render(path,template_values))        


class Foto(webapp.RequestHandler):
    def get(self):
        path = template_pattern('main.html')
        template_values = {'content_template':'foto.html'}
        self.response.out.write(template.render(path,template_values))
        
class Trip(webapp.RequestHandler):
    def get(self):
        path = template_pattern('main.html')
        template_values = {'content_template':'trip.html'}
        self.response.out.write(template.render(path,template_values))                

class Template(webapp.RequestHandler):
    def get(self):
        path = template_pattern('main.html')
        template_values = {'var':path}
        self.response.out.write(template.render(path,template_values))

application = webapp.WSGIApplication([('/$',Main),
                                      ('/contact$',Contact),
                                      ('/foto$',Foto),
                                      ('/trip$',Trip),
                                      ('/my$',Template)                                                                                                                                      
                                      ],
                                       debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
        