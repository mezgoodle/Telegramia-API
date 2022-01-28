from fastapi import FastAPI, status

from routers import player, road, country, item, city, heroclass, horse, dungeon, admin, authentication

description = """
Telegramia API helps you do awesome stuff. 🚀

## All items

You will be able to:

* **Read items** (without _authentication_).
* **Create, update and delete items** (with _authentication_).
"""

tags_metadata = [
    {
        'name': 'Admins',
        'description': 'Operations with admins. They have full access in this API.',
    },
    {
        'name': 'Cities',
        'description': 'Operations with cities. This are main objects in game.',
    },
    {
        'name': 'Countries',
        'description': 'Operations with countries. They summarize all objects in game world.',
    },
    {
        'name': 'Hero classes',
        'description': 'Operations with classes. They describe different classes that player can choose.',
    },
    {
        'name': 'Horses',
        'description': 'Operations with horses. They are main transport in game world.',
    },
    {
        'name': 'Items',
        'description': 'Operations with items. They help players to survive in game world.',
    },
    {
        'name': 'Players',
        'description': 'Operations with players. Information about all players in game.',
    },
    {
        'name': 'Roads',
        'description': 'Operations with roads. They connect all objects in game world.',
    },
    {
        'name': 'Dungeons',
        'description': 'Operations with dungeons. Here players can earn money and experiments.',
    },
]

app = FastAPI(
    title='Telegramia API',
    description=description,
    version='1.1.0',
    terms_of_service='https://github.com/mezgoodle/Telegramia-API/blob/master/CODE_OF_CONDUCT.md',
    contact={
        'name': 'Maxim Zavalniuk',
        'url': 'https://github.com/mezgoodle',
        'email': 'mezgoodle@gmail.com',
    },
    license_info={
        'name': 'MIT License',
        'url': 'https://github.com/mezgoodle/Telegramia-API/blob/master/LICENSE',
    },
    openapi_tags=tags_metadata
)

app.include_router(authentication.router)
app.include_router(player.router)
app.include_router(road.router)
app.include_router(country.router)
app.include_router(item.router)
app.include_router(city.router)
app.include_router(heroclass.router)
app.include_router(horse.router)
app.include_router(dungeon.router)
app.include_router(admin.router)


@app.get('/', status_code=status.HTTP_200_OK)
async def start_page():
    return {'Information': 'Too see all available methods visit /docs page'}
