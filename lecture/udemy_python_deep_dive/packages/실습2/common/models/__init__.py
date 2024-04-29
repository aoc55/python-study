
from .posts import *
from .users import *


# __all__ = (posts.__all__ + users.__all__)


# __init__.py 에 아래와 같이 메서드 추가할 수 있지만...
# 꼭 여기 있어야 하는가? (비즈니스 기능이)
# __init__.py는 순수히 초기화 역할만?
# 물론 standara library 에서도 아래와 같이 쓰는 경우도 있음
def say_hello(name):
    return f'Hello {name}'

import asyncio
import email
