import pytest

from search_engine.search_engine import search


@pytest.mark.parametrize(
    argnames=["docs", "expected"],
    argvalues=[
        (
            [
                {'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"},
                {'id': 'doc2', 'text': "Don't shoot shoot shoot that thing at me."},
                {'id': 'doc3', 'text': "I'm your shooter."},
            ],
            ["doc1", "doc2"]
        ),
        ([], [])
    ]
)
def test_search(docs, expected):
    # поисковый движок проводит поиск
    assert search(docs, "shoot") == expected