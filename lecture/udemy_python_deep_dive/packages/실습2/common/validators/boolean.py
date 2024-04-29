
# (2) from import * 시 노출하고 싶은 함수만 지정
__all__ = ['is_boolean', 'boolean_helper_2']

def is_boolean(value):
    pass

def xxx_bolean(value):          # 비노출 (__all__ 속성에 없음)
    pass


# (1) _ 로 시작시 from .. import * 에서 제외됨 (namespace 에 추가 안됨)
def _boolean_helper_1():        # 비노출
    pass


def boolean_helper_2():
    pass