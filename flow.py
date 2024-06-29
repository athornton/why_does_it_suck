import mermaid as md
from mermaid.graph import Graph

suck_diagram = """
flowchart TD
    A[This thing sucks] --> B{When did it start to suck?}
    B --> |Before 1980| C[Racism]
    B --> |1980-2010| D[Ronald Reagan (implies racism)]
    B --> |After 2010| E[Private Equity (implies Reagan)]
"""

graph: Graph = Graph("Why does it suck?", suck_diagram)

output: md.Mermaid = md.Mermaid(graph)
print(output)
