from dataclasses import field
from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from src.config_schemas.infrastructure.infrastructure_schema import InfrastructureConfig


@dataclass
class Config:
    infrastructure: InfrastructureConfig = field(default_factory=InfrastructureConfig)


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)
