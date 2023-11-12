def dfs(graph, rootNode = 'A'):
  def _dfs(toVisit):
    if not toVisit:
      return
    node = toVisit.pop()
    print(str(node))
    children = graph[node]
    for child in children[::-1]:
      toVisit.append(child)
    _dfs(toVisit)
  toVisit = [rootNode]
  _dfs(toVisit)

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': [],
  'E': [],
  'F': [],
  'G': []
}
dfs(graph)
