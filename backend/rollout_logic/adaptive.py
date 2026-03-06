MIN_BATCH = 1
MAX_BATCH = 50

HIGH_FAILURE_THRESHOLD = 0.20
LOW_FAILURE_THRESHOLD = 0.05


def calculate_next_batch(current_size: int,
                         failed: int,
                         total: int) -> int:

    if total == 0:
        return current_size

    failure_rate = failed / total

    if failure_rate > HIGH_FAILURE_THRESHOLD:

        new_size = max(MIN_BATCH, current_size // 2)

        print(
            f"High failure rate {failure_rate:.0%}. "
            f"Reducing batch: {current_size} -> {new_size}"
        )

        return new_size

    elif failure_rate < LOW_FAILURE_THRESHOLD:

        new_size = min(MAX_BATCH, int(current_size * 1.5))

        print(
            f"Low failure rate {failure_rate:.0%}. "
            f"Increasing batch: {current_size} -> {new_size}"
        )

        return new_size

    print(
        f"Stable failure rate {failure_rate:.0%}. "
        f"Keeping batch: {current_size}"
    )

    return current_size