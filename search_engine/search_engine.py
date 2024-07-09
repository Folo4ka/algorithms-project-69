import re

from search_engine.types.types import Document


def search(docs: list[Document], value: str) -> list[str]:
    """
    Поиск value с учетом частоты встречи
    """

    # разбиваем текст на термы (обработанные слова от лишних символов)
    docs = [{
        "id": doc["id"],
        "terms": re.findall(r"[a-zA-Z0-9а-яА-я_]+", doc["text"]),
    } for doc in docs]

    # высчитываем релевантность каждого текста относительно искомой строки (по кол-ву вхождений)
    docs = [{
        "relevant_score": doc["terms"].count(value),
        **doc
    } for doc in docs if value in doc["terms"]]

    # сортировка результата по релевантности
    docs.sort(key=lambda doc: doc["relevant_score"], reverse=True)

    return [doc["id"] for doc in docs]
