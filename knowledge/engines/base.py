from abc import ABC, abstractmethod


class MedicalNlpEngine(ABC):

    @abstractmethod
    def extract_entities(self, text: str):
        """
        Extract medical entities from text.
        """
        pass
    