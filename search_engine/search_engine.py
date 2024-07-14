import re
import math

from search_engine.types.types import Document


def search(docs: list[Document], value: str) -> list[str]:
    """
    Поиск value в списке текстов docs
    Отсортировано по убыванию релевантности (TF-IDF)

    Использован обратный индекс (слово: документы где встречается)
    """

    search_terms = re.findall(r"[a-zA-Z0-9а-яА-я_]+", value.lower())

    if not docs or not search_terms:
        return []

    docs_map = get_term_docs_map(docs)
    docs_reversed_index = get_reversed_index(docs_map)
    result_docs: dict[str, float] = {}

    # ищем документы по search_terms и вычисляем их релевантность
    for term in search_terms:
        if term not in docs_reversed_index:
            continue

        for doc_id in docs_reversed_index[term]:
            relevant_value = get_tf_idf(
                term=term,
                doc_terms=docs_map.get(doc_id, []),
                docs_reversed_index=docs_reversed_index,
                docs_count=len(docs),
            )

            if doc_id in result_docs:
                result_docs[doc_id] += relevant_value
            else:
                result_docs[doc_id] = relevant_value

    # сортировка результата по релевантности
    search_result = [
        {
            "id": doc_id,
            "relevant_score": relevant
        } for doc_id, relevant in result_docs.items()
    ]
    search_result.sort(key=lambda doc: -doc["relevant_score"])

    return [doc["id"] for doc in search_result]


def get_tf_idf(
    term: str,
    doc_terms: list[str],
    docs_reversed_index: dict[str, set[str]],
    docs_count: int
) -> float:
    """
    Функция вычисления значения TF-IDF для слова term по документу doc
    """
    tf = doc_terms.count(term) / len(doc_terms)
    term_count = len(docs_reversed_index.get(term, set()))
    idf = math.log2(1 + (docs_count - term_count + 1) / (term_count + 0.5))

    return tf * idf


def get_reversed_index(docs: dict[str, list[str]]) -> dict[str, set[str]]:
    """
    Функция создания обратного индекса для набора документов с термами
    """
    reversed_index = {}

    for doc_id, doc_terms in docs.items():
        for term in doc_terms:
            if term in reversed_index:
                reversed_index[term].add(doc_id)
            else:
                reversed_index[term] = {doc_id}

    return reversed_index


def get_term_docs_map(docs: list[Document]) -> dict[str, list[str]]:
    """
    Возвращает словарь документов со списками терм их текстов
    """
    return {
        doc["id"]: re.findall(r"[a-zA-Z0-9а-яА-я_]+", doc["text"].lower())
        for doc in docs
    }
