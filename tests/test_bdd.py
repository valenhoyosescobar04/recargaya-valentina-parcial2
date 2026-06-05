# tests/test_bdd.py
from pytest_bdd import scenarios
from features.steps.recarga_steps import *

scenarios('../features/recarga.feature')