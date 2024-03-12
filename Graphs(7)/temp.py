def create_graph(graph_file_path):
        # read graph.txt and create graph

        with open(graph_file_path) as f:
            line = f.readlines()
            for i in line:
                source, dest = i.strip().split(' ')
                print(source, dest)
                break

create_graph('graph.txt')