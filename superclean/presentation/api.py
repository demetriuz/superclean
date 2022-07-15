from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI, Depends, APIRouter

from container import Container
from entities import Node
from dtos import ResponseNodeDTO, CreateRequestNodeDTO
from interfaces import INodeRepository, IUseCases

router = APIRouter()


@router.get("/", response_model=List[Node])
@inject
def get_nodes(repository: INodeRepository = Depends(Provide[Container.repository])):
    nodes = repository.get_nodes(parent=None)
    return nodes


@router.post("/add", response_model=Node)
@inject
def add_node(
    node: CreateRequestNodeDTO,
    use_cases: IUseCases = Depends(Provide[Container.use_cases]),
) -> ResponseNodeDTO:
    return use_cases.add_node(node)


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()
    app.container = container
    app.include_router(router)
    container.wire(modules=[__name__])
    return app


app = create_app()
