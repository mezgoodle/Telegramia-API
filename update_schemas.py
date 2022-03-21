from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId

from typing import Optional, List, Dict, Union
from datetime import timedelta, datetime


class UpdatePlayerModel(BaseModel):
    user_id: Optional[str]
    telegram_name: Optional[str]
    name: Optional[str]
    level: Optional[float]
    experience: Optional[float]
    health: Optional[float]
    energy: Optional[float]
    strength: Optional[float]
    agility: Optional[float]
    intuition: Optional[float]
    intelligence: Optional[float]
    hero_class: Optional[str]
    nation: Optional[str]
    money: Optional[float]
    items: Optional[List[str]]
    mount: Optional[dict]
    current_state: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "user_id": "34344334",
                "telegram_name": "mezgoodle",
                "name": "Jane Doe",
                "level": 3,
                "experience": 45,
                "health": 100.0,
                "energy": 30.0,
                "strength": 11.4,
                "agility": 3.2,
                "intuition": 55.1,
                "intelligence": 34.0,
                "hero_class": "paladin",
                "nation": "Priaria",
                "money": 123.65,
                "items": ["wood shield", "helmet"],
                "mount": {"name": "Bob", "type": "horse", "bonus": 12},
                "current_state": "Stormwind",
            }
        }


class UpdateRoadModel(BaseModel):
    from_obj: Optional[str]
    to_obj: Optional[str]
    name: Optional[str]
    energy: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Big forest route",
                "from_obj": "Ogrimmar",
                "to_obj": "Stormwind",
                "energy": "13.4",
            }
        }


class UpdateCountryModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    capital: Optional[str]
    population: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Priaria",
                "description": "Big country",
                "capital": "Stormwind",
                "population": 0,
            }
        }


class UpdateItemModel(BaseModel):
    name: Optional[str]
    characteristic: Optional[str]
    bonus: Optional[float]
    city: Optional[str]
    price: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Wood helmet",
                "characteristic": "strength",
                "bonus": 13.3,
                "city": "Stormwind",
                "price": 34.0,
            }
        }


class UpdateCityModel(BaseModel):
    name: Optional[str]
    country: Optional[str]
    is_capital: Optional[bool]
    market: Optional[bool]
    academy: Optional[bool]
    temple: Optional[bool]
    tavern: Optional[bool]
    menagerie: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Stormwind",
                "country": "Alliance",
                "is_capital": True,
                "market": True,
                "academy": False,
                "temple": False,
                "tavern": True,
                "menagerie": True,
            }
        }


class UpdateHorseModel(BaseModel):
    name: Optional[str]
    bonus: Optional[float]
    city: Optional[str]
    price: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "White faster",
                "bonus": 13.3,
                "city": "Stormwind",
                "price": 34.0,
            }
        }


class UpdateHeroClassModel(BaseModel):
    name: Optional[str]
    characteristics: Optional[dict]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Воїн",
                "characteristics": {
                    "strength": 0.0,
                    "agility": 0.0,
                    "intuition": 0.0,
                    "intelligence": 0.0,
                },
            }
        }


class UpdateAdminModel(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "mezgoodle",
                "email": "mezgoodle@gmail.com",
                "password": "123456",
            }
        }


class UpdateDungeonModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    damage: Optional[float]
    base_time: Optional[timedelta]
    treasure: Optional[float]
    members: Optional[Dict[str, datetime]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "dungeon",
                "description": "dungeon",
                "damage": 1231.213,
                "base_time": 133,
                "treasure": 12312.323,
                "members": {"mezgoodle": "2008-09-15T15:53:00+05:00"},
            }
        }


class UpdateRaidModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    treasure: Optional[float]
    members: Optional[Dict[str, Dict[str, Union[datetime, int]]]]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "dungeon",
                "description": "dungeon",
                "treasure": 12312.323,
                "members": {
                    "mezgoodle": {"time": "2008-09-15T15:53:00+05:00", "level": 1}
                },
            }
        }


class UpdateRaidLevelModel(BaseModel):
    name: Optional[str]
    raid_name: Optional[str]
    level: Optional[int]
    description: Optional[str]
    damage: Optional[float]
    base_time: Optional[timedelta]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "dungeon",
                "raid_name": "raid",
                "level": 1,
                "description": "dungeon",
                "damage": 1231.213,
                "base_time": 133,
            }
        }
