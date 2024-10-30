from typing import Any, Iterable


def currprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    end_curr_on_none: bool = False,
) -> Iterable[tuple[T | None, T | None]]:
    prev: T | None = None
    for curr in iter(iterable):
        if prev is not None or start_prev_on_none:
            yield curr, prev
        prev = curr
    if end_curr_on_none and prev is not None:
        yield None, prev


def prevcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    end_curr_on_none: bool = False,
) -> Iterable[tuple[T | None, T | None]]:
    for curr, prev in currprev(
        iterable,
        start_prev_on_none=start_prev_on_none,
        end_curr_on_none=end_curr_on_none,
    ):
        yield prev, curr


def currnext[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None]]:
    iterator = iter(iterable)
    try:
        if not start_curr_on_none:
            curr = next(iterator)
        else:
            curr = None
    except StopIteration:
        return
    for _next in iterator:
        yield curr, _next
        curr = _next
    if end_next_on_none and curr is not None:
        yield curr, None


def nextcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None]]:
    for curr, _next in currnext(
        iterable,
        start_curr_on_none=start_curr_on_none,
        end_next_on_none=end_next_on_none,
    ):
        yield _next, curr


def prevcurrnext[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    start_curr_on_none: bool = False,
    end_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None, T | None]]:
    prev = None
    curr = None
    iterator = iter(iterable)
    if not start_prev_on_none:
        if start_curr_on_none:
            raise ValueError("start_curr_on_none=True requires start_prev_on_none=True")
        try:
            prev = next(iterator)
        except StopIteration:
            return
        try:
            curr = next(iterator)
        except StopIteration:
            yield prev, None, None
            return
    elif not start_curr_on_none:
        try:
            curr = next(iterator)
        except StopIteration:
            return
    for _next in iterator:
        yield prev, curr, _next
        prev = curr
        curr = _next
    if end_curr_on_none:
        if not end_next_on_none:
            raise ValueError("end_next_on_none=True requires end_curr_on_none=True")
        yield prev, curr, None
        yield curr, None, None
    elif end_next_on_none:
        yield prev, curr, None


def nextcurrprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    start_curr_on_none: bool = False,
    end_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None, T | None]]:
    for prev, curr, _next in prevcurrnext(
        iterable,
        start_prev_on_none=start_prev_on_none,
        start_curr_on_none=start_curr_on_none,
        end_curr_on_none=end_curr_on_none,
        end_next_on_none=end_next_on_none,
    ):
        yield _next, curr, prev
