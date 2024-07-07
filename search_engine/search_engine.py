from search_engine.types.types import Document


def search(docs: list[Document], value: str) -> list[str]:
    return [doc["id"] for doc in docs if value in doc["text"].split(" ")]

