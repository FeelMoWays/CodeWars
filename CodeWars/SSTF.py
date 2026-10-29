def sstf(request_queue, initial_head_position):
    count = 0
    while request_queue:
        target = min(request_queue,key=lambda x: abs(x - initial_head_position))
        count += abs(target - initial_head_position)
        initial_head_position = target
        request_queue.remove(target)
    return count
print(sstf([98, 183, 37, 122, 14, 124, 65, 67],53))
