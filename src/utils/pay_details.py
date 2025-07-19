import re
import uuid
import hashlib
import datetime

from .logger import setup_logger

from core.config import settings

logger = setup_logger(__name__)


def generate_order_number():
    # Генерируем UUID (универсальный уникальный идентификатор)
    order_id = uuid.uuid4()
    # Преобразуем UUID в строку и убираем дефисы
    order_number = str(order_id).replace("-", "")
    # Обрезаем строку до 30 символов, если она слишком длинная
    order_number = order_number[:30]
    return order_number


def get_receipt():
    data = {
        "Taxation": "usn_income",
        "Email": "test@mail.ru",
        "Items": [
            {
                "Name": "Подписка",
                "Price": 1000,
                "Quantity": 1.0,
                "Amount": 100000,
                "PaymentMethod": "full_payment",
                "PaymentObject": "service",
                "Tax": "none",
            },
        ],
    }
    return data


def create_token(payment_id):

    tokentr = (
        settings.pay.tinkoff_secret + payment_id + settings.pay.tinkoff_terminal_key
    )
    tokensha256 = str(hashlib.sha256(tokentr.encode()).hexdigest())
    return tokensha256


def generate_token(data, password):

    # Добавляем пароль
    data["Password"] = password

    # Исключаем вложенные объекты и массивы
    filtered_data = {k: v for k, v in data.items() if not isinstance(v, (dict, list))}

    # Сортируем данные по ключам
    sorted_data = sorted(filtered_data.items(), key=lambda x: x[0])

    # Конкатенируем значения
    concatenated_values = "".join(str(value) for _, value in sorted_data)

    # Генерируем SHA256-хеш
    hashed_token = hashlib.sha256(concatenated_values.encode("utf-8")).hexdigest()

    return hashed_token


def check_payment_date(data: str) -> bool:
    today = datetime.datetime.today().date()
    pattern = r":\s*(\d{4}-\d{2}-\d{2})"

    # Извлекаем дату из строки, если она присутствует
    match = re.search(pattern, data)
    if match:
        string_date = match.group(1)
        # Преобразование строки даты в объект datetime
        pay_date = datetime.datetime.strptime(string_date, "%Y-%m-%d").date()
        if pay_date == today:
            return True
    return False


def check_payment(payment) -> bool:
    return True if payment["Status"] == "CONFIRMED" else False
