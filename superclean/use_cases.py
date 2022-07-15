from dtos import CreateRequestNodeDTO, ResponseNodeDTO
from interfaces import INodeRepository, IUseCases
import entities


class UseCases(IUseCases):
    def __init__(self, repository: INodeRepository):
        self.rep = repository

    def add_node(self, node_dto: CreateRequestNodeDTO) -> ResponseNodeDTO:
        self.rep.start_transaction()

        if node_dto.parent_id:
            parent = self.rep.get_node(node_dto.parent_id)
        else:
            parent = None

        node = self.rep.add_node(
            node=entities.Node(
                value=node_dto.value,
                parent=parent
            )
        )

        self.rep.commit()
        return ResponseNodeDTO(
            id=node.id,
            value=node.value,
            parent_id=node.parent.id if node.parent else None
        )
