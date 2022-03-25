from pydantic import BaseModel, Field
from bson import ObjectId

from typing import Optional, List, Dict, Union
from datetime import timedelta, datetime


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class PlayerModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str = Field(...)
    telegram_name: str = Field(...)
    name: str = Field(...)
    level: float = Field(...)
    experience: float = Field(...)
    health: float = Field(...)
    energy: float = Field(...)
    strength: float = Field(...)
    agility: float = Field(...)
    intuition: float = Field(...)
    intelligence: float = Field(...)
    hero_class: str = Field(...)
    nation: str = Field(...)
    money: float = Field(...)
    items: List[str] = Field(...)
    mount: dict = Field(...)
    current_state: str = Field(...)

    class Config:
        allow_population_by_field_name = True
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


class RoadModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    from_obj: str = Field(...)
    to_obj: str = Field(...)
    name: str = Field(...)
    energy: float = Field(...)
    travelers: int = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Big forest route",
                "from_obj": "Ogrimmar",
                "to_obj": "Stormwind",
                "energy": "13.4",
                "travelers": 0,
            }
        }


class CountryModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    capital: str = Field(...)
    population: int = Field(...)

    class Config:
        allow_population_by_field_name = True
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


class ItemModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    characteristic: str = Field(...)
    type: str = Field(...)
    bonus: float = Field(...)
    city: str = Field(...)
    price: float = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Wood helmet",
                "characteristic": "strength",
                "type": "helmet",
                "bonus": 13.3,
                "city": "Stormwind",
                "price": 34.0,
            }
        }


class HorseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    bonus: float = Field(...)
    city: str = Field(...)
    price: float = Field(...)

    class Config:
        allow_population_by_field_name = True
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


class CityModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    country: str = Field(...)
    is_capital: bool = Field(...)
    market: bool = Field(...)
    academy: bool = Field(...)
    temple: bool = Field(...)
    tavern: bool = Field(...)
    menagerie: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
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


class HeroClassModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    characteristics: dict = Field(...)

    class Config:
        allow_population_by_field_name = True
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


class AdminModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "mezgoodle",
                "email": "mezgoodle@gmail.com",
                "password": "123456",
            }
        }


class DungeonModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    damage: float = Field(...)
    base_time: timedelta = Field(...)
    treasure: float = Field(...)
    members: Dict[str, datetime] = Field(...)

    class Config:
        allow_population_by_field_name = True
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


class RaidModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    members: Dict[str, Dict[str, Union[int, datetime]]] = Field(...)

    class Config:
        allow_population_by_field_name = True
        smart_union = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "dungeon",
                "description": "dungeon",
                "members": {
                    "mezgoodle": {"time": "2008-09-15T15:53:00+05:00", "level": 1}
                },
            }
        }


class RaidLevelModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    raid_name: str = Field(...)
    level: int = Field(...)
    description: str = Field(...)
    damage: float = Field(...)
    treasure: float = Field(...)
    base_time: timedelta = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "raid_level",
                "raid_name": "raid",
                "level": 1,
                "description": "dungeon",
                "damage": 1231.213,
                "treasure": 12312.323,
                "base_time": 133,
            }
        }


class TokenData(BaseModel):
    email: Optional[str] = None
