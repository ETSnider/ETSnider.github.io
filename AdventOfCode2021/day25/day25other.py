from functools import wraps
from time import sleep, time
from typing import Any, List, Sequence, Tuple
 
 
def move(arr: Sequence[str], cucumber_type: str) -> List[str]:
    new_arr = list(arr)
    for i in range(len(arr)):
        next_index = i + 1 if i != len(arr) - 1 else 0
        if arr[i] == cucumber_type and arr[next_index] not in (">", "v"):
            new_arr[i], new_arr[next_index] = ".", cucumber_type
    return new_arr
 
 
def move_right(arr: List[str]) -> List[str]:
    return list(move(arr, ">"))
 
 
def move_down(arr: Tuple[str, ...]) -> Tuple[str, ...]:
    return tuple(move(arr, "v"))
 
 
def transpose(arr: Sequence[Sequence[Any]]) -> List[Tuple[Any, ...]]:
    return list(zip(*arr))
 
 
def step(input: str) -> str:
    input_arrays = [list(line) for line in input.splitlines()]
 
    right_arrays: List[List[str]] = []
    for input_array in input_arrays:
        right_arrays.append(move_right(input_array))
 
    transpose_right_down_arrays: List[Tuple[str, ...]] = []
    transpose_right_arrays = transpose(right_arrays)
    for i, transpose_right_array in enumerate(transpose_right_arrays):
        transpose_right_down_arrays.append(move_down(transpose_right_array))
 
    right_down_strings: List[str] = []
    right_down_arrays = transpose(transpose_right_down_arrays)
    for right_down_array in right_down_arrays:
        right_down_strings.append("".join(right_down_array))
    output = "\n".join(right_down_strings)
    return output
 
 
def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        output = fn(*args, **kwargs)
        print(fn.__qualname__, "in", time() - start_time, "sec")
        return output
 
    return wrapper
 
 
@timer
def count_steps(state_before: str) -> int:
    i = 0
    while True:
        state_after = step(state_before)
        i += 1
        if state_before == state_after:
            open("day25otherout.txt",'w').writelines(state_after)
            return i
        # print(i)
        # print(state_after, "\n\n\n")
        # sleep(0.1)
        state_before = state_after
 
 
if __name__ == "__main__":
    with open("day25input.txt", "r") as f:
        real_input = f.read().strip()
    print(count_steps(real_input), "steps")
 
"""
count_steps in 2.3781538009643555 sec
400 steps
"""