def pipeline(stages: list[int], details: list[int]) -> list[int]:

    n = len(stages)
    end_times = [0] * n
    completion_times = []

    for detail_start in details:
        current_time = detail_start

        for i in range(n):
            current_time = max(current_time, end_times[i]) + stages[i]
            end_times[i] = current_time

        completion_times.append(current_time)

    return completion_times