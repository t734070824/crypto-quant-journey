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


def validate_input(func):
    """装饰器: 验证输入参数是否合法"""
    def wrapper(*args, **kwargs):
        # 检查参数是否为空
        if not args:
            raise ValueError(f"{func.__name__} 需要至少一个参数")

        # 检查第一个参数是否为正数 (适用于周期参数)
        if len(args) > 0 and isinstance(args[0], (int, float)):
            if args[0] <= 0:
                raise ValueError(f"{func.__name__} 的第一个参数必须 > 0, 得到: {args[0]}")

        # 调用原函数
        return func(*args, **kwargs)
    return wrapper


@timer
def hello():
    print('hello')

@cache
def info(n):
    return n * 2

# 测试装饰器
print("=== 测试 @timer 装饰器 ===")
hello()

print("\n=== 测试 @cache 装饰器 ===")
print("第一次调用 info(1):", info(1))
print("第二次调用 info(1):", info(1))  # 这次会命中缓存

print("\n=== 测试 @validate_input 装饰器 ===")

@validate_input
def calculate_ma(period):
    """计算移动平均线 - 带输入验证"""
    return f"计算 {period} 日均线"

# 正常调用
print(calculate_ma(20))  # 正常工作

# 错误调用示例 (取消注释后会报错)
# print(calculate_ma(-5))   # 报错: 参数必须 > 0
# print(calculate_ma(0))    # 报错: 参数必须 > 0
