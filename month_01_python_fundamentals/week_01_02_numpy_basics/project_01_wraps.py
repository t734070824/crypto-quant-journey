import time


def timer(func):
    """装饰器: 计算函数执行时间"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {(end - start)*1000:.2f}ms")
        return result
    return wrapper


def cache(func):
    my_cache = {}
    def wrapper(*args):
        if args in my_cache:
            print("Hit Cache, returning")
            return my_cache[args]
        result = func(*args)
        my_cache[args] = result
        return result
    return wrapper

@timer
def hello():
    print('hello')

@cache
def info(n):
    return n * 2

hello()
print(info(1))
print(f"info_1")
print(info(1))
