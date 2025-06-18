# services/inn_lookup.py — логика поиска по ИНН через Dadata
# Путь: D:\telbot\services\inn_lookup.py

import requests
from config import DA_DATA_API_KEY

# Настройки
DA_DADATA_URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Token {DA_DATA_API_KEY}",
}

# Картинка статусов
STATUS_TRANSLATION = {
    "ACTIVE": "действующая",
    "LIQUIDATING": "ликвидируется",
    "LIQUIDATED": "ликвидирована",
}


def lookup_inn(inn: str) -> str:
    """
    Поиск организации по ИНН через DaData.
    Возвращает отформатированную строку с основными реквизитами или сообщение об ошибке.
    """
    # 1. Проверка формата ИНН
    if not inn.isdigit() or len(inn) not in (10, 12):
        return "❌ Неверный формат ИНН — должно быть 10 или 12 цифр."

    payload = {"query": inn, "count": 1}

    # 2. Запрос
    try:
        resp = requests.post(DA_DADATA_URL, json=payload, headers=HEADERS, timeout=5)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] HTTP error: {e}")
        return "⚠️ Не удалось подключиться к DaData. Попробуйте позже."

    # 3. Парсинг JSON
    try:
        data = resp.json()
    except ValueError as e:
        print(f"[ERROR] JSON parse error: {e}")
        return "⚠️ Некорректный ответ от сервиса. Попробуйте позже."

    suggestions = data.get("suggestions") or []
    if not suggestions or not suggestions[0].get("data"):
        return "❌ Организация с таким ИНН не найдена."

    org = suggestions[0]["data"]

    # 4. Сбор реквизитов
    name = org.get("name", {}).get("full_with_opf", "—")
    inn_val = org.get("inn", "—")
    kpp_val = org.get("kpp", "—")
    ogrn_val = org.get("ogrn", "—")

    state = org.get("state", {}) or {}
    status_en = state.get("status", "").upper()
    status_ru = STATUS_TRANSLATION.get(status_en, status_en.capitalize() or "—")

    addr = org.get("address", {}).get("value", "—")

    mgr = org.get("management") or {}
    mgr_name = mgr.get("name", "—")
    mgr_post = mgr.get("post", "")

    opf = org.get("opf", {}) or {}
    form = opf.get("full", "—")

    okved_code = org.get("okved", "—")
    okved_type = org.get("okved_type", "")
    okved = f"{okved_code}{f' — {okved_type}' if okved_type else ''}"

    # 5. Правильное получение сведений об ИФНС (authorities – объект, а не список)
    authorities = org.get("authorities") or {}
    fts_reg = authorities.get("fts_registration") or {}
    tax_authority = fts_reg.get("name", "—")

    # 6. Формируем ответ
    return (
        f"🏢 {name}\n"
        f"ИНН: {inn_val}\n"
        f"КПП: {kpp_val}\n"
        f"ОГРН: {ogrn_val}\n"
        f"Статус: {status_ru}\n"
        f"Адрес: {addr}\n"
        f"Руководитель: {mgr_name}{f' ({mgr_post})' if mgr_post else ''}\n"
        f"Форма: {form}\n"
        f"Сведения ИФНС: {tax_authority}\n"
        f"Основной ОКВЭД: {okved}"
    )
