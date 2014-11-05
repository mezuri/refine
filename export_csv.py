import csv
import sys
from google.refine import refine

print sys.argv

project_id = sys.argv[1]
output_file = sys.argv[2]

server = refine.RefineServer()
refine = refine.Refine(server)

in_file = refine.open_project(project_id).export()
in_file_csv = csv.reader(in_file, dialect='excel-tab')

with open(output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(in_file_csv)

in_file.close()