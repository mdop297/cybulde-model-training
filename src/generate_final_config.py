from src.utils.config_utils import get_config
from omegaconf import OmegaConf



@get_config(config_path="../configs", config_name="config")
def generate_final_config(config) -> None:
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    generate_final_config()
