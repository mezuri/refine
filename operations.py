import json

from google.refine import refine

server = refine.RefineServer()
refine = refine.Refine(server)

def save_all_operations(project_id, all_operations_fp):
    # Caution: This will return a different JSON than the web interface and will also include 'data set-specific' operations!
	# We'll still store this information for full provenance
	all_operations = server.urlopen_json(command='get-operations', project_id=project_id)

	# Write provenance to file
	with open(all_operations_fp, 'w') as outfile:
	    json.dump(all_operations, outfile)
	return

def compute_applicable_operations(all_operations_fp, operations_fp):
	# Compute operations (sub set) that can actually be applied to other data sets
	# TODO implement Python/JS function analog to the code in _showExtractOperationsDialog
	# https://github.com/OpenRefine/OpenRefine/blob/8517111fc4e2c940ff3c935d68d6acce53dd5c84/main/webapp/modules/core/scripts/project/history-panel.js
	return

def apply_operations(project_id, operations_fp):
	# Apply operations to different project
	project = refine.open_project(project_id)
	return project.apply_operations(operations_fp)

save_all_operations(2383091503974, 'all_operations.json')
# compute_applicable_operations()
# apply_operations(2338254275680, 'operations.json')