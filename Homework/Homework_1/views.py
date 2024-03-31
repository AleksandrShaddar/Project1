from django.shortcuts import render
from django.http import HttpResponse
import logging

# Create your views here.
logger = logging.getLogger(__name__)

def main(request):
    html = """ <h1>Немного информации о моем опыте</h1>
    <p>До обучения в GB самостоятельно никогда не писал сайты и т.п.</p> 
    <p>Замостоятельно занимался изученияем языка Python, но далеко не продвинулся.</p> 
    <p>Первую html-страницу написал на курсе "Знакомство с веб-технологими".</p>
    """
    logger.info("Переход на страницу 'Главная'")
    return HttpResponse(html)


def about(request):
    html = """ <h1>Давайте знакомиться!</h1>
    <ul>Информация о себе:
        <li>Имя: Александр.</li>
        <li>Возраст: 27 лет.</li>
        <li>Город: Курск.</li>
        <li>Увлечения: гейминг, криптовалюты, IT.</li>
    </ul> 
    """
    logger.info("Переход на страницу 'О себе'")
    return HttpResponse(html)