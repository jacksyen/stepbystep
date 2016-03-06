import sys
import jinja2
from jinja2.nodes import Template

__author__ = 'patrick'

from githubimporter import GitHubImporter

sys.path_hooks.append(GitHubImporter)
sys.path.append('github://mitsuhiko/jinja2')

jinja2.__file__
t=Template('Hello from {{ hell}}')
t.render(hell='Import Hook Hell')
