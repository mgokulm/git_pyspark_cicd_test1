from pathlib import Path
import pytest
from jobs.ops import *
import os

def __init__(self, main_module: str = 'jobs/ops.py'):
    self.__root_dir = str(Path(__file__).parent.parent)
    self.main_module = os.path.join(self.__root_dir, main_module)
    super().__init__()

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(2,3) == -1

def test_multiply():
    assert multiply(2,3) == 6

def test_divide():
    assert divide(12,3) == 4
