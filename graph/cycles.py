
def find_cycle(graph):
    #fill this in
    hashMap = {}
    for key, value in graph.items():
        # print(graph[key].keys())
        if key in hashMap:
            return True
        else:
            hashMap[key] = key
            for keys in graph[key].keys():
                if keys in hashMap:
                    return True
                else:
                    hashMap[keys] = keys

    return False

graph = {
  'a': {'a2':{}, 'a3':{} },
  'b': {'b2':{}},
  'c': {}
}
print(find_cycle(graph))
# False
graph['c'] = graph
print(find_cycle(graph))
# True