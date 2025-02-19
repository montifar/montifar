graph = {

'flowg': ['aljames', 'hellmary'],
'aljames': ['abra', 'basilyo'],
'hellmary': ['loonie'],
'abra': [],
'basilyo': [],
'loonie': [],
}

def display_graph(graph):
    for node in graph:
        print(node, "->", graph[node])
        
        display_graph(graph)