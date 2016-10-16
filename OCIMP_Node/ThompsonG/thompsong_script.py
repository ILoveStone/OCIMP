from ThompsonG import ThompsonG
import sys
sys.path.append("..")
import Report
from os.path import isfile, join

seed_size = 50

for iscontextual in [True, False]:
	for graph_file in ["subnethept.txt", "nethept.txt"]:
		if((graph_file == "subnethept.txt") and (iscontextual)):
			epochs = 5000
		elif((graph_file == "nethept.txt") and (iscontextual)):
			epochs = 5000
		elif((graph_file == "subnethept.txt") and (not iscontextual)):
			epochs = 1250
		elif((graph_file == "nethept.txt") and (not iscontextual)):
			epochs = 2500
		experiment_name = "contextual_" if(iscontextual) else "noncontextual_"
		experiment_name += graph_file[:-4]

		pathway = join("../../Misc/node_results", experiment_name, "thompsong_results.json")

		# Experiment is already done
		if(isfile(pathway)):
			continue

		thompsong = ThompsonG(seed_size, graph_file, epochs, iscontextual)
		thompsong()
		Report.report("thompsong", thompsong, experiment_name)
