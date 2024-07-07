import re

from search_engine.types.types import Document


def search(docs: list[Document], value: str) -> list[str]:
    return [doc["id"] for doc in docs if value in re.findall(r"[a-zA-Z0-9а-яА-я_]+", doc["text"])]
