import sys
import os

import ablog

from sunpy_sphinx_theme.conf import *

sys.path.append(os.path.abspath('exts'))
extensions = ['sphinx.ext.githubpages', 'ablog', 'sphinxcontrib.rawfiles', 'cards',
              'sphinx.ext.intersphinx', 'sphinx.ext.imgmath', 'nbsphinx']
templates_path = [ablog.get_html_templates_path()]

intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'sunpy': ('http://docs.sunpy.org/en/stable', None),
                       'astropy': ('http://docs.astropy.org/en/stable', None),
                       'ndcube': ('http://docs.sunpy.org/projects/ndcube/en/stable', None),
                       'drms': ('http://docs.sunpy.org/projects/drms/en/stable/', None)}

rawfiles = ['jitsi.html']

disqus_shortname = 'sunpy-org'
blog_baseurl = 'https://sunpy.org/blog.html'
blog_feed_fulltext = True
blog_feed_length = 10
blog_feed_archives = True

source_suffix = '.rst'
exclude_patterns = ['posts/*/.ipynb_checkpoints/*']
master_doc = 'index'
project = u'SunPy'
author = 'SunPy Project'
copyright = 'SunPy Project'
show_sphinx = True
version = u''
release = u''
language = None

pygments_style = 'sphinx'

default_role = 'obj'

html_title = ''
html_static_path = ['_static']
html_theme_options.update({
    'base_url': 'sunpy.org',
    'seo_description': 'SunPy',
    'navbar_pagenav': False,
    'globaltoc_depth': 1,
    'on_rtd': False,
    'copyright_html': """
<a style= "padding-left: 10px;" rel="licence" href="http://creativecommons.org/licenses/by/4.0/">
<img src="https://i.creativecommons.org/l/by/4.0/80x15.png">
</a>
"""
})
html_sidebars = {
    'index': None,
    'about': ['localtoc.html'],
    'contribute': ['localtoc.html'],
    'blog': ['searchbox.html', 'categories.html', 'archives.html'],
    'blog/**': ['searchbox.html', 'categories.html', 'archives.html'],
    'help': ['localtoc.html'],
    'posts/**': ['postcard.html'],
    'team': ['localtoc.html'],
    'newcomers': ['localtoc.html']
}
