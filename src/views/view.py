import logging
from typing import List

from fastapi import APIRouter, BackgroundTasks

from src.models.postgres.images_info_model import ImagesInfoSchema
from src.operators.postgres import (
    create_database,
    data_insertion,
    drop_database
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
    create_database.execute()

    return 'Таблица успешно создана.'


@router.post("/insert_data")
async def insert_data(body: List[ImagesInfoSchema]):
    data_insertion.execute(body)

    return f'Успешно записано {len(body)} записи.'
