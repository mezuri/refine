import sys
from google.refine import refine

print 'launched load_csv.py'

print sys.argv

project_file = sys.argv[1]
project_format = 'text/line-based/*sv'
project_options = {}

server = refine.RefineServer()
refine = refine.Refine(server)

project_url = refine.new_project(project_file=project_file, project_format=project_format, **project_options).project_url()

with open('/tmp/refine_url', 'w') as text_file:
    text_file.write(project_url)