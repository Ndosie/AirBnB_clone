#!/usr/bin/python3
"""Defines user class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City"""

    state_id = ""
    name = ""
