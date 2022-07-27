from pydantic import BaseSettings, Field


class MediumConfig(BaseSettings):
    tier: str = "dev"  # default value is given
    log_level: str = "INFO"

    # no default value, env var name different from variable
    user: str = Field(..., env="username")

    class Config:
        env_prefix = "medium_"


# Option 1 set variables using the class initializer + default values
cfg = MediumConfig(user="hans-maulwurf")

print(cfg)
# --> tier='dev' log_level="INFO" user='hans-maulwurf'

# Option 2 set variables using the class initializer + env vars
import os

os.environ["medium_tier"] = "prd"
os.environ["medium_log_level"] = "DEBUG"
os.environ["user_name"] = "simon.hawe"

cfg = MediumConfig(log_level="ERROR")  # overrule value from env var

print(cfg)
# --> tier='prd' log_level="INFO" user='simon.hawe'
