import os
from typing import Union
from dotenv import load_dotenv

from fastapi import FastAPI

from .adapters.mealie import MealieAdapter

load_dotenv()

app = FastAPI()

mealie_adapter = MealieAdapter(
    base_url=os.getenv("MEALIE_BASE_URL"), api_key=os.getenv("MEALIE_API_KEY")
)


@app.get("/")
def read_root():
    return mealie_adapter.get_version()


@app.get("/recipes")
def read_recipes():
    return mealie_adapter.get_recipes()
