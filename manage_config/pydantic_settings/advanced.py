"""
Date: 2022.07.27 14:26:40
LastEditors: Rustle Karl
LastEditTime: 2022.07.27 14:26:41
"""
import yaml
from pydantic import BaseSettings, Field
from pydantic.env_settings import SettingsSourceCallable
from typing import Any


def yml_config_setting(settings: BaseSettings) -> dict[str, Any]:
    with open("config.yml") as f:
        return yaml.safe_load(f)


class MediumConfig(BaseSettings):
    tier: str = "dev"
    log_level: str = "INFO"
    user: str = Field(..., env="user_name")

    class Config:
        env_prefix = "medium_"

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> tuple[SettingsSourceCallable, ...]:
            # Add load from yml file, change priority and remove file secret option
            return init_settings, yml_config_setting, env_settings


# Example useage with dummy config file created
import os

os.environ["medium_tier"] = "prd"
os.environ["user_name"] = "simon.hawe"

with open("config.yml", "w") as f:
    yaml.safe_dump({"user": "DevOps-Engineer"}, f)

print(MediumConfig())
# --> tier='prd' log_level='DEBUG' user='DevOps-Engineer'
