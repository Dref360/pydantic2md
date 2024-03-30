from datetime import datetime
from typing import Dict, List, Optional, Union
from watchfiles import watch
from pydantic2md import core
from pydantic import BaseModel

import os
from importlib import reload


"""
Debug script that reloads on code change.
Useful when iteratively working on something.


Feel free to make Model/SubModel more complex as pydantic2md becomes more complex.
"""


class SubModel(BaseModel):
    field_a: Optional[int] = None
    field_b: Dict[str, Union[str, int]]


class Model(BaseModel):
    a: int
    b: float
    values: List[int]
    submodels: List[SubModel]


DATA = Model(
    a=1,
    b=0.53213,
    values=[1, 76, 93],
    submodels=[SubModel(field_b={"name": "potato", "age": 16}), SubModel(field_a=12, field_b={})],
)

for changes in watch("../pydantic2md"):
    os.system("clear")
    print(f"Reloaded {datetime.now()}")
    try:
        core = reload(core)
        out = core.pydantic2md(DATA)
        print(out)
    except Exception as e:
        print(e)
