from dependency_injector import containers, providers
from repository import memory
import use_cases


class Container(containers.DeclarativeContainer):
    repository = providers.Singleton(memory.NodeRepository)
    use_cases = providers.Factory(
        use_cases.UseCases,
        repository=repository
    )
