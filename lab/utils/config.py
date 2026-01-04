from dataclasses import dataclass
from typing import Optional
import yaml


@dataclass
class ConfigFileInfo:
    dirpath: str
    filename: str

    @staticmethod
    def from_agent_env(agent_name: str, env_name: str) -> 'ConfigFileInfo':
        dirpath = f'config/agents/{agent_name}'
        filename = f'{env_name}.yaml'
        return ConfigFileInfo(dirpath=dirpath, filename=filename)


class ConfigHandler:
    def __init__(
        self,
        config_info: Optional[ConfigFileInfo] = None,
        agent_name: Optional[str] = None,
        env_name: Optional[str] = None
    ):
        if config_info is None:
            if agent_name is None or env_name is None:
                raise ValueError("Either config_info or both agent_name and env_name must be provided.")
            config_info = ConfigFileInfo.from_agent_env(agent_name, env_name)
        self.config_info = config_info
        self.config = self._load_config()


    def _load_config(self) -> dict:
        filepath = f"{self.config_info.dirpath}/{self.config_info.filename}"
        with open(filepath, 'r') as f:
            try:
                config_dict = yaml.load(f, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                raise RuntimeError(f"{self.config_info.filename} error: {exc}")
        return config_dict


    def get_config(self) -> dict:
        return self.config
