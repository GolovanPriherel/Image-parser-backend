from typing import List

from fastapi import APIRouter

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.operators.postgres import (
    CreateDataBase,
    DataInsertion,
    DropDataBase
)


router = APIRouter(prefix="")


@router.get("/")
async def root():

    return 'Сервис для хранения путей и информации о фотографиях.' \
           'Версия 0.0.1'


@router.get("/test_start")
async def root():
    # logging.warning("Проверяю все тесты...")
    # #TODO сделать проверку всех тестов

    return 'Сервис готов к работе.'


@router.get("/create_table")
async def create_table():
    CreateDataBase().execute()

    return 'Таблица успешно создана.'


@router.post("/insert_data")
async def insert_data(data: List[ImagesInfoSchema]):
    DataInsertion(data).execute()

    return f'Успешно записано {len(data)} записи.'


@router.get("/drop_table")
async def drop_table():
    DropDataBase().execute()

    return 'Таблица успешно удалена.'


