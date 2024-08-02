#!/usr/bin/python3
"""Defines user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
