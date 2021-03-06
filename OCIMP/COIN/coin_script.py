from COIN import COIN
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

		pathway = join("../../Misc/results", experiment_name, "coin_results.json")

		# Experiment is already done
		if(isfile(pathway)):
			continue

		coin = COIN(seed_size, graph_file, epochs, iscontextual)
		coin()

		Report.report("coin", coin, experiment_name)
