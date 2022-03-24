# 1.2.1 (24.03.22)

- Update **Item** model.

**Full Changelog**: https://github.com/mezgoodle/Telegramia-API/compare/v1.2.0...v1.2.1

# 1.2.0 (24.03.22)

- Create **Raid** and **RaidLevel** models.
- Update code format with [black](https://github.com/psf/black).
- Create two seperate _routers_ and _tests_ for **raids** and **raid levels**.
- Rename some route paramaters, such as `name -> route_name`.
- Add parametr _city_name_ for **horse** routes: _update_, _get_ and _delete_.
- Update the routes' descriptions.

**Full Changelog**: https://github.com/mezgoodle/Telegramia-API/compare/v1.1.2...v1.2.0

# 1.1.2 (07.02.22)

- Change _timedelta_ to _datetime_ in **Dungeon** models.

# 1.1.1 (01.02.22)

- Change _SecretStr_ to _str_ in **Admin** models.

# 1.1.0 (28.01.22)

- Add dungeons model.

# 1.0.1 (24.09.21)

- Clean up the code.

# 1.0.0 (18.09.21)

- Here is the first release of Telegramia API. You can get all items and create, update and delete them(with authentication).
