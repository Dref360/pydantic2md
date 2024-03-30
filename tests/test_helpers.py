from typing import List

from pydantic import BaseModel
from pydantic2md.core import get_type_name


class Hero(BaseModel):
    name: str
    age: int

def test_get_type_name():
    assert get_type_name(List) == "List"
    assert get_type_name(List[str]) == "List[str]"
    assert get_type_name(List[Hero]) == "List[Hero]"
    assert get_type_name(Hero) == "Hero"
