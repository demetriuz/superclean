import abc
from typing import Optional, List
import dtos
import entities


class INodeRepository(metaclass=abc.ABCMeta):
    def add_node(self, node: entities.Node) -> entities.Node:
        pass

    def get_node(self, id: int):
        pass

    def get_nodes(self, parent: Optional[entities.Node]) -> List[entities.Node]:
        pass

    def start_transaction(self):
        pass

    def commit(self):
        pass


class IUseCases(metaclass=abc.ABCMeta):
    def add_node(self, node: dtos.CreateRequestNodeDTO) -> dtos.ResponseNodeDTO:
        pass
