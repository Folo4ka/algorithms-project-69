import pytest

from search_engine.search_engine import search


documents = [
    {"id": "doc1", "text": "I can't shoot straight unless I've had a pint!"},
    {"id": "doc2", "text": "Don't shoot shoot shoot that thing at me."},
    {"id": "doc3", "text": "I'm your shooter."},
]

@pytest.mark.parametrize(
    argnames=["docs", "search_value", "expected"],
    argvalues=[
        (documents, "shoot", ["doc1", "doc2"]),
        (documents, "pint", ["doc1"]),
        ([], "shoot", [])
    ]
)
def test_search(docs, search_value, expected):
    # поисковый движок проводит поиск
    assert search(docs, search_value) == expected
