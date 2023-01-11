import logging
from typing import List, Optional, Dict

from fastapi import APIRouter, BackgroundTasks

from src.models.postgres.rule34_images_info import (
    Rule34ImagesInfoModel,
    Rule34ImagesInfoSchema,
    Rule34ImagesInfoListSchema,
    InputURLs,
)
from src.operators.postgres import (
    create_database,
    data_insertion,
    rule34_insertion,
    rule34_urls_insertion
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
async def insert_data(params: dict):
    rule34_insertion.execute(params["data"])


@router.post("/insert_urls")
async def insert_urls(params: InputURLs):
    params = params.data
    rule34_urls_insertion.execute(params)
