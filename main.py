from sys import argv
from pathlib import PurePath
from knowledge import KnowledgeNetwork, Inputs, Output
from deductor import KnowledgeNetworkDeductor

try:
    knowledges_path = argv[1]
except:
    knowledges_path = "knowledges/knowledges.json"
finally:
    knowledges_path = PurePath(knowledges_path)

knowledge_network = KnowledgeNetwork.from_json(knowledges_path)
deductor = KnowledgeNetworkDeductor(knowledge_network=knowledge_network)
# print(knowledge_network[Inputs(["a", "b", "C"])].())

print(deductor.deduce(Inputs(["a", "C"]), Output("hb")))
