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
        (documents, "shoot", ["doc2", "doc1"]),
        (documents, "pint", ["doc1"]),
        (documents, "shoot at me", ["doc2", "doc1"]),
        ([], "shoot", [])
    ]
)
def test_search(docs, search_value, expected):
    assert search(docs, search_value) == expected
