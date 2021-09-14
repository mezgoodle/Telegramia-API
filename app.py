from fastapi import FastAPI

from routers import player, road, country, item, city, heroclass, horse, admin

app = FastAPI()

app.include_router(player.router)
app.include_router(road.router)
app.include_router(country.router)
app.include_router(item.router)
app.include_router(city.router)
app.include_router(heroclass.router)
app.include_router(horse.router)
app.include_router(admin.router)

