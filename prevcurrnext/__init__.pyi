from typing import Iterable, Literal, overload

@overload
def prevcurr[T](iterable: Iterable[T]) -> Iterable[tuple[T | None, T]]: ...
@overload
def prevcurr[T](
    iterable: Iterable[T],
    *,
    end_curr_on_none: Literal[False],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def prevcurr[T](
    iterable: Iterable[T],
    *,
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def prevcurr[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def prevcurr[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def prevcurr[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def prevcurr[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T, T | None]]: ...
@overload
def prevcurr[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True],
    end_curr_on_none: Literal[False],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def prevcurr[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True],
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def currprev[T](iterable: Iterable[T]) -> Iterable[tuple[T, T | None]]: ...
@overload
def currprev[T](
    iterable: Iterable[T],
    *,
    end_curr_on_none: Literal[False],
) -> Iterable[tuple[T, T | None]]: ...
@overload
def currprev[T](
    iterable: Iterable[T],
    *,
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def currprev[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def currprev[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True],
) -> Iterable[tuple[T, T | None]]: ...
@overload
def currprev[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def currprev[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def currprev[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True],
    end_curr_on_none: Literal[False],
) -> Iterable[tuple[T, T | None]]: ...
@overload
def currprev[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True],
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def currnext[T](iterable: Iterable[T]) -> Iterable[tuple[T, T | None]]: ...
@overload
def currnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
) -> Iterable[tuple[T, T | None]]: ...
@overload
def currnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def currnext[T](
    iterable: Iterable[T],
    *,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def currnext[T](
    iterable: Iterable[T],
    *,
    end_next_on_none: Literal[True],
) -> Iterable[tuple[T, T | None]]: ...
@overload
def currnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def currnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
    end_next_on_none: Literal[True],
) -> Iterable[tuple[T, T | None]]: ...
@overload
def currnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def currnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def nextcurr[T](iterable: Iterable[T]) -> Iterable[tuple[T | None, T]]: ...
@overload
def nextcurr[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def nextcurr[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def nextcurr[T](
    iterable: Iterable[T],
    *,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def nextcurr[T](
    iterable: Iterable[T],
    *,
    end_next_on_none: Literal[True],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def nextcurr[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def nextcurr[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
    end_next_on_none: Literal[True],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def nextcurr[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def nextcurr[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
) -> Iterable[tuple[T | None, T, T | None]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
) -> Iterable[tuple[T, T, T | None]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
    *,
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
    *,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T | None, T, T]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T, T]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T, T, T | None]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def prevcurrnext[T](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True],
    end_curr_on_none: Literal[True],
    end_next_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
) -> Iterable[tuple[T | None, T, T | None]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
) -> Iterable[tuple[T | None, T, T | None]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    start_next_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    end_prev_on_none: Literal[False],
) -> Iterable[tuple[T, T, T]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
    end_prev_on_none: Literal[False],
) -> Iterable[tuple[T, T, T]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False],
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    start_next_on_none: Literal[True],
    end_prev_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def nextcurrprev[T](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_curr_on_none: Literal[True],
    end_prev_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
