import sys
from google.refine import refine

print sys.argv

project_file = sys.argv[1]
project_format = 'text/line-based/*sv'
project_options = {}

server = refine.RefineServer()
refine = refine.Refine(server)

print refine.new_project(project_file=project_file, project_format=project_format, **project_options).project_url()