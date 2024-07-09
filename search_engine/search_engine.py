import re
from functools import reduce

from search_engine.types.types import Document


def search(docs: list[Document], value: str) -> list[str]:
    """
    Поиск value с учетом частоты встречи
    Сначала считается количество слов из искомого набора, затем сумма вхождений
    Отсортировано по убыванию релевантности
    """

    search_terms = re.findall(r"[a-zA-Z0-9а-яА-я_]+", value)

    # разбиваем текст на термы (обработанные слова от лишних символов)
    docs = [{
        "id": doc["id"],
        "terms": re.findall(r"[a-zA-Z0-9а-яА-я_]+", doc["text"]),
    } for doc in docs]

    # высчитываем количество слов из искомого набора и общую сумму вхождений
    docs = [{
        "search_terms_count": len(set(search_terms).intersection(set(doc["terms"]))),
        "all_entries_count": reduce(lambda acc, search_term: doc["terms"].count(search_term), search_terms, 0),
        **doc
    } for doc in docs]

    docs = [doc for doc in docs if doc["search_terms_count"] > 0]

    # сортировка результата по релевантности
    docs.sort(key=lambda doc: (-doc["search_terms_count"], -doc["all_entries_count"]))

    return [doc["id"] for doc in docs]
