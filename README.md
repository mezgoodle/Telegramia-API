<h1 id="project-title" align="center">
  Telegramia-API <img alt="logo" width="40" height="40" src="https://raw.githubusercontent.com/mezgoodle/images/master/MezidiaLogoTransparent.png" /><br>
  <img alt="language" src="https://img.shields.io/badge/language-python-brightgreen?style=flat-square" />
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/mezgoodle/Telegramia-API?style=flat-square" />
  <img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/mezgoodle/Telegramia-API?style=flat-square" />
  <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/mezgoodle/Telegramia-API?style=flat-square" />
  <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/mezgoodle/Telegramia-API?style=flat-square" />
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/mezgoodle/Telegramia-API?style=flat-square">
</h1>

<p align="center">
🌟Hello everyone! This is the repository of Telegramia-API.🌟
</p>

## Motivation :exclamation:

[Telegramia](https://github.com/mezidia/Telegramia-API) is the game in _Telegram_ and with this API you can take information from the game

## Build status :hammer:

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration):

[![Python application](https://github.com/mezgoodle/Telegramia-API/actions/workflows/python-package.yml/badge.svg)](https://github.com/mezgoodle/Telegramia-API/actions/workflows/python-package.yml)
[![Python application](https://gitlab.com/mezgoodle/Telegramia-API/badges/master/pipeline.svg)](https://gitlab.com/mezgoodle/Telegramia-API/-/pipelines)
 
## Screenshots :camera:

- `/docs` page

![/docs page](https://raw.githubusercontent.com/mezgoodle/images/master/telegramia_api.png)

## Tech/framework used :wrench:

**Built with**

- [FastAPI](https://fastapi.tiangolo.com/)
- [bcrypt](https://pypi.org/project/bcrypt/)
- [passlib](https://pypi.org/project/passlib/)
- [pymongo](https://pymongo.readthedocs.io/en/stable/)
- [motor](https://motor.readthedocs.io/en/stable/)

## Features :muscle:

On the site you can **create**, **update**, **read** and **delete** different information about Telegramia game.

## Code Example :pushpin:

- Router example:

```python
from fastapi import APIRouter, status, HTTPException, Body, Depends
from database import get_object, create_document, get_all_objects, update_object, delete_object
from schemas import AdminModel, UpdateAdminModel, ShowAdminModel
from typing import Optional, List
from hashing import Hash
from oauth2 import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['Admins']
)


@router.post('', response_description='Add new admin', response_model=AdminModel,
             status_code=status.HTTP_201_CREATED)
async def create_admin(admin: AdminModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Create an API admin with all permissions:

    - **current user** should be admin
    - **name**: admin name
    - **email**: admin email
    - **password**: admin password
    """
    admin.password = Hash.bcrypt(admin.password)
    return await create_document(admin, 'admins')


@router.get('s', response_description='List all admins', response_model=List[ShowAdminModel],
            status_code=status.HTTP_200_OK)
async def list_admins():
    """
    Get all admins
    """
    admins = await get_all_objects('admins')
    return admins


@router.get('', response_description='Get a single admin', response_model=ShowAdminModel,
            status_code=status.HTTP_200_OK)
async def show_admin(identifier: Optional[str] = None, admin_name: Optional[str] = None):
    """
    Get admin by name:

    - **name**: admin name
    """
    variables = locals()
    options = {'identifier': '_id', 'admin_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await get_object({options[key]: variables[key]}, 'admins')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.put('', response_description='Update an admin', response_model=UpdateAdminModel,
            status_code=status.HTTP_200_OK)
async def update_admin(identifier: Optional[str] = None, admin_name: Optional[str] = None,
                       admin: UpdateAdminModel = Body(...), current_user: AdminModel = Depends(get_current_user)):
    """
    Update an API admin:

    - **current user** should be admin
    - **name**: admin name
    - **email**: admin email
    - **password**: admin password
    """
    variables = locals()
    options = {'identifier': '_id', 'admin_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await update_object({options[key]: variables[key]}, admin, 'admins')
    raise HTTPException(status_code=404, detail='Set some parameters')


@router.delete('', response_description='Delete an admin',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_admin(identifier: Optional[str] = None, admin_name: Optional[str] = None,
                       current_user: AdminModel = Depends(get_current_user)):
    """
    Delete an API admin:

    - **current user** should be admin
    - **name**: admin name
    """
    variables = locals()
    options = {'identifier': '_id', 'admin_name': 'name'}
    for key in variables.keys():
        if variables[key] is not None:
            return await delete_object({options[key]: variables[key]}, 'admins')
    raise HTTPException(status_code=404, detail='Set some parameters')

```

## Installation :computer:

1. Clone this repository:

```bash
git clone https://github.com/mezgoodle/Telegramia-API.git
```

2. Install all packages:

```bash
pip install -r requirements.txt
```

3. Set environment variables in `config.py`

4. Run tests:
```bash
pytest 
```

## Fast usage :dash:

Just run the server with _uvicorn_:

```bash
uvicorn app:app --reload
```

## Contribute :running:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also look at the [CONTRIBUTING.md](https://github.com/mezgoodle/Telegramia-API/blob/master/CONTRIBUTING.md).

## Credits :cat::handshake:

Links to videos which help me built this project:

[FastAPI Tutorial from freecodecamp](https://www.youtube.com/watch?v=tLKKmouUams)

[FastAPI Tutorial](https://www.youtube.com/watch?v=7t2alSnE2-I)

## License :bookmark:

MIT © [mezgoodle](https://github.com/mezgoodle)
