from fastapi import FastAPI, status

from routers import player, road, country, item, city, heroclass, horse, admin, authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(player.router)
app.include_router(road.router)
app.include_router(country.router)
app.include_router(item.router)
app.include_router(city.router)
app.include_router(heroclass.router)
app.include_router(horse.router)
app.include_router(admin.router)


@app.get('/', status_code=status.HTTP_200_OK)
async def start_page():
    return {'Information': 'Too see all available methods visit /docs page'}
