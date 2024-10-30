import pytest

from prevcurrnext import currnext, currprev, prevcurrnext


def test_currprev():
    assert list(currprev([1, 2, 3])) == [(1, None), (2, 1), (3, 2)]
    assert list(currprev([1])) == [(1, None)]
    assert list(currprev([1], end_curr_on_none=True)) == [
        (1, None),
        (None, 1),
    ]
    assert list(currprev([])) == []  # type: ignore


def test_prevcurrnext():
    assert list(prevcurrnext([1, 2, 3])) == [
        (None, 1, 2),
        (1, 2, 3),
        (2, 3, None),
    ]
    assert list(prevcurrnext([1])) == [(None, 1, None)]
    assert list(prevcurrnext([])) == []
    assert list(prevcurrnext([1, 2])) == [(None, 1, 2), (1, 2, None)]
    assert list(
        prevcurrnext([1, 2, 3], start_prev_on_none=False, end_next_on_none=False)
    ) == [
        (1, 2, 3),
    ]
    with pytest.raises(ValueError):
        list(
            prevcurrnext(  # pyright: ignore[reportCallIssue, reportUnknownArgumentType]
                [1, 2, 3],
                start_prev_on_none=False,
                start_curr_on_none=True,  # pyright: ignore[reportArgumentType]
            )
        )
    with pytest.raises(ValueError):
        list(
            prevcurrnext(  # pyright: ignore[reportCallIssue, reportUnknownArgumentType]
                [1, 2, 3],
                start_prev_on_none=True,
                start_curr_on_none=False,  # pyright: ignore[reportArgumentType]
            )
        )


def test_currnext():
    assert list(currnext([])) == []
