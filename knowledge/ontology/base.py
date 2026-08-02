from abc import ABC, abstractmethod


class OntologyEngine(ABC):

    @abstractmethod
    def link(self, entity):
        """
        Link a medical entity to an ontology.
        """
        pass