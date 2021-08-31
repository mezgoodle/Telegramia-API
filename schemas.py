from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId

from typing import Optional


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
    items: list = Field(...)
    mount: dict = Field(...)
    current_state: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                'user_id': '34344334',
                'telegram_name': 'mezgoodle',
                "name": "Jane Doe",
                "level": 3,
                "experience": 45,
                'health': 100.0,
                'energy': 30.0,
                "strength": 11.4,
                "agility": 3.2,
                'intuition': 55.1,
                'intelligence': 34.0,
                'hero_class': 'paladin',
                'nation': 'Priaria',
                'money': 123.65,
                'items': ['wood shield', 'helmet'],
                'mount': {'name': 'Bob', 'type': 'horse', 'bonus': 12},
                'current_state': 'Stormwind'
            }
        }


class RoadModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    from_obj: str = Field(...)
    to_obj: str = Field(...)
    name: str = Field(...)
    energy: float = Field(...)

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
                'country': 'Alliance',
                "is_capital": True,
                'market': True,
                'academy': False,
                'temple': False,
                'tavern': True,
                'menagerie': True
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
                "name": 'Воїн',
                "characteristics": {
                    'strength': 0.0,
                    'agility': 0.0,
                    'intuition': 0.0,
                    'intelligence': 0.0
                }
            }
        }


class UpdatePlayerModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    course: Optional[str]
    gpa: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
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
    pass


class UpdateItemModel(BaseModel):
    pass


class UpdateCityModel(BaseModel):
    pass


class UpdateHorseModel(BaseModel):
    pass
