import heapq
from knowledge import *


class KnowledgeNetworkDeductor:
    def __init__(self, knowledge_network: KnowledgeNetwork):
        self.knowledge_network = knowledge_network

    def find_path(
        self, start_inputs: Inputs, target_output: Output
    ) -> list[dict[Inputs, dict[str, any]]] | None:
        """
        Find the shortest path to transform start_inputs to target_output
        using the knowledge network.
        """
        # Use a tuple with a counter for stable sorting in heapq
        pq = [(0, 0, start_inputs, [])]
        visited = set()
        counter = 0

        while pq:
            current_cost, _, current_inputs, path_so_far = heapq.heappop(pq)

            # Convert inputs to a hashable representation for visited check
            inputs_key = current_inputs.sorted()
            if inputs_key in visited:
                continue
            visited.add(inputs_key)

            for inputs, data in self.knowledge_network.inner.items():
                if all(
                    input_elem in current_inputs.inner for input_elem in inputs.inner
                ):
                    new_inputs = Inputs(current_inputs.inner.union({data["output"]}))
                    new_path = path_so_far + [{"inputs": inputs, **data}]

                    if data["output"] == target_output:
                        return new_path

                    counter += 1
                    heapq.heappush(
                        pq, (current_cost + 1, counter, new_inputs, new_path)
                    )

        return None

    def deduce(self, start_inputs: Inputs, target_output: Output):
        """
        Public method to find the path of transformations.
        """
        return self.find_path(start_inputs, target_output)
