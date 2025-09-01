# When you use yield instead of return, your function becomes a generator.
# A generator does not give you everything at once.
# Instead, it produces a sequence of values one by one, each time you ask for the next value.
# After yield, the function pauses and remembers its state (variables, loop counters, etc.).
# When you call it again, it continues right where it left off.


def ft_tqdm(lst: range) -> None:
    """
    A minimal tqdm-like generator for ranges.
    Yields each element of lst while printing an in-place progress bar.
    """
    total = len(lst)
    if total == 0:
        return

    bar_width = 110
    for i, elem in enumerate(lst):
        progress = (i + 1) / total
        percent = int(progress * 100)
        filled = int(progress * bar_width)

        if filled == 0:
            bar = ">" + " " * (bar_width - 1)
        elif filled >= bar_width:
            bar = "=" * (bar_width - 1) + ">"
        else:
            bar = "=" * (filled - 1) + ">" + " " * (bar_width - filled)

        print(f"\r{percent:3d}%|[{bar}]| {i+1}/{total}", end="", flush=True)
        yield elem
