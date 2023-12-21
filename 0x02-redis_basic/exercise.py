#!/usr/bin/env python3
"""
Building a simple cache
Create a store method that takes a data argument and returns a string. The
 method should generate a random key (e.g. using uuid), store the input data

"""
from typing import Callable, Optional, Union
import redis
import sys
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counter number of calls made to a method"""
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """decorator method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return counter


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs"""
    @wraps(method)
    def history_wrapper(self, *args, **kwargs):
        """set list keys to a wrapped function"""
        list_key = method.__qualname__ + ":inputs"
        out_list = method.__qualname__ + ":outputs"
        self._redis.rpush(list_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(out_list, str(output))
        return output
    return history_wrapper


def replay(method: Callable) -> None:
    """function displays the history of calls"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    server_oone = method.__self__._redis
    counter = server_oone.get(key).decode("utf-8")
    print(f"{key} was called {counter} times:")
    input_list = server_oone.lrange(inputs, 0, -1)
    output_list = server_oone.lrange(outputs, 0, -1)
    zipped_out = list(zip(input_list, output_list))
    for k, v in zipped_out:
        attr, result = k.decode("utf-8"), k.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache:
    """cache class"""
    def __init__(self) -> None:
        """ Instant of Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """this method takes data argument and returns a string"""
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """retieves value from server_oone, convert it to desired format"""
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_int(self, data_bytes: bytes) -> int:
        """convert data bytes from server_oone back to int"""
        return int.from_bytes(data_bytes, sys.byteorder)

    def get_str(self, data_bytes: bytes) -> str:
        """convert data bytes from server_oone back into str"""
        return data_bytes.decode('utf-8')
