## Set up a Virtual Environment with Pipenv

> pip install --user pipenv

> export PATH="$PATH:/Users/your-user-name/Library/Python/3.9/bin"

or

> py -m pip install pipenv

## Install package

> pipenv install fastapi

> pipenv install "uvicorn[standard]"

> pipenv install pydantic

> pipenv install sqlalchemy

## Run server

> pipenv run uvicorn main:app --reload
