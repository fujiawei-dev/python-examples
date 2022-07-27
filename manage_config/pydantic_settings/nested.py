"""
Date: 2022.07.27 15:57:29
LastEditors: Rustle Karl
LastEditTime: 2022.07.27 16:06:32
"""
import os
from pydantic import BaseModel, BaseSettings


class DeepSubModel(BaseModel):
    v4: str


class SubModel(BaseModel):
    v1: str
    v2: bytes
    v3: int
    deep: DeepSubModel


class Settings(BaseSettings):
    v0: str
    sub_model: SubModel

    class Config:
        env_nested_delimiter = "__"


os.environ["V0"] = '0'
os.environ["SUB_MODEL"] = '{"v1": "json-1", "v2": "json-2"}'
os.environ["SUB_MODEL__V2"] = "nested-2"
os.environ["SUB_MODEL__V3"] = '3'
os.environ["SUB_MODEL__DEEP__V4"] = "v4"

print(Settings().dict())
