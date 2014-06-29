#!/usr/bin/env python

from distutils.core import setup

setup(name='OERPLog',
      version='1.0',
      description='Display Log of OpenERP in ',
      author='Yanina Aular',
      author_email='yaniaular@gmail.com',
      url='http://www.yanina.com.ve',
      packages=['oerplog'],
      scripts=['bin/oerplog'],
      package_data={'oerplog': [
            'openerp_log.css',
          ]},

#~      entry_points="""
#~      [console_scripts]
#~      oerplog=oerplog.oerplog:run
#~      """,
      #py_modules=['oerplog'],
     )
