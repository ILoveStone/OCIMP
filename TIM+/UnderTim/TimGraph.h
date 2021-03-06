#ifndef TIMGRAPH_H
#define TIMGRAPH_H

#include "InfGraph.h"

class TimGraph: public InfGraph{
    public:
        TimGraph(string graph_file, int node_cnt, int edge_cnt, int seed_size,string model, vector<int> banned_nodes);
        double MgT(int u);
        double algo2();
        double KptEstimation();
        void RefindKPT(double epsilon, double ept);
        double logcnk(int n, int k);
        void NodeSelection(double epsilon, double opt);
        void EstimateOPT(double epsilon);
};

#endif
