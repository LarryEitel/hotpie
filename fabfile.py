#import wingdbstub
import time
import os, sys
from fabric.api import local, cd, run, env, sudo, require
import settings

db = settings.DATABASES['default']
fab = settings.FABRIC['live']


env.hosts = fab['HOSTS']
env.user = fab['ADMIN_USER']
env.admin_user = fab['ADMIN_USER']
env.dbname = db['NAME']
env.dbuser = db['USER']
env.dbpass = db['PASSWORD']


def hello():
    print("Hello world!")
    
#@run_once
def commit(msg):
    with cd(os.path.abspath(os.path.dirname(__file__))):
        local('git add .')
        local('git commit -am"%s"' % msg)
        local('git push origin master') # push local to repository
         