#!/usr/bin/env python

from google.appengine.tools import bulkloader
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
import models 

class MemberLoader(bulkloader.Loader):
    def __init__(self):
        bulkloader.Loader.__init__(self, 'Member',
                                    [
                                        ('fn', str),
                                        ('ln', str),
                                        ('dpt', str),
                                        ('sec', str),
                                        ('loc', str),
                                        ('faddr', str),
                                        ('lat', float),
                                        ('lng', float),
                                    ])

loaders = [MemberLoader]
