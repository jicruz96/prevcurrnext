from typing import Iterable


def currprev[T](
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
        yield prev, None


def prevcurr[T](
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


def currnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None]]:
    iterator = iter(iterable)
    curr = None
    if not start_curr_on_none:
        curr = next(iterator)
    for _next in iterator:
        yield curr, _next
        curr = _next
    if end_next_on_none:
        yield curr, None


def nextcurr[T](
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


def prevcurrnext[T](
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
        prev = next(iterator)
        curr = next(iterator)
    elif not start_curr_on_none:
        curr = next(iterator)
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


def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: bool = False,
    start_next_on_none: bool = True,
    end_curr_on_none: bool = False,
    end_prev_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None, T | None]]:
    for prev, curr, _next in prevcurrnext(
        iterable,
        start_prev_on_none=start_curr_on_none,
        start_curr_on_none=start_next_on_none,
        end_curr_on_none=end_curr_on_none,
        end_next_on_none=end_prev_on_none,
    ):
        yield _next, curr, prev
