import pprint
from sys import argv
from pathlib import PurePath
from knowledge import KnowledgeNetwork
from deductor import KnowledgeNetworkDeductor
from compute import Computer, ProblemParser

knowledges_path = "knowledges/knowledges.json"
knowledges_path = PurePath(knowledges_path)

knowledge_network = KnowledgeNetwork.from_json(knowledges_path)
deductor = KnowledgeNetworkDeductor(knowledge_network=knowledge_network)

input_filepath = PurePath(argv[1])
problem_parser = ProblemParser.from_json(input_filepath)
print(
    f"Problem\n\nInputs={pprint.pformat(problem_parser.input_with_values)}\nOutputs={pprint.pformat(problem_parser.output)}\n"
)

computation_path = deductor.deduce(
    problem_parser.input_with_values.to_inputs(), problem_parser.output
)

print("Computing steps")
pprint.pprint(computation_path)

computer = Computer(computation_path)
print(
    f"\nOutput value\n{problem_parser.output}={computer.compute_from(problem_parser.input_with_values, problem_parser.output)}"
)
