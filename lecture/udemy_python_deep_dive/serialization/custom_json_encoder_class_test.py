import json
# [ json.dumps() 의 여러 Argument 테스트 ]

target = {
    'a': float('inf'),
    'b': float('nan'),
    1+1j: "complex Value"
}

# Skipkeys
try:
    print(json.dumps(target, skipkeys=False))       # False 가 Default
except TypeError as e:
    print(e)

print(json.dumps(target, skipkeys=True))

# Indent & Seperator 테스트
print(json.dumps(target, skipkeys=True, indent=5, separators=('*', "==")))

# 통신용 compact ? indext X , seperator로 공백 제거 (',',':')
print(json.dumps(target, skipkeys=True, indent=0, separators=(',', ':')))

print("--------------------------------------------------------")


# [ Custom JSON Encoder Class 실습 1 ]
# - json.dumps(...) 호출 시마다 argument 매번 정의하는 것이 아닌, 인코딩 클래스 생성
# - 즉, encode 함수의 default callable의 Argument 방식이 아닌 '클래스 자체'로 정의해서 전달
# - 기존 json.dumps(....arguent ... ) 주르륵 하는 것보다는? Encapsulation 등의 장점

# - Custom Encoder 클래스 정의
class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):         # dumps(..) 에서 전달해주는 argument 들에 대해 수신 필요 (args,kwargs)

        print(" ---> 전달되는 args", args)
        print(" ---> 전달되는 kwargs", kwargs)

        super().__init__(                       # Customizing!
            # skipkeys=True,
            skipkeys=kwargs['skipkeys'],
            allow_nan=False,
            indent=2,
            separators=('', ' = ')
        )

    def default(self, arg):                     # Customizing!
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)


# - Test
target_dict = {
    'time': datetime.utcnow(),
    1 + 1j : "complex Key",
    "name" : 'Python'
}

print(json.dumps(target_dict, cls=CustomEncoder, skipkeys=True))

print("--------------------------------------------------------")


# [ Custom JSON Encoder Class 실습 2 ]
# - Custom Encoder 클래스 정의
class CustomDateEncoder(json.JSONEncoder):

    # init 은 그대로 사용

    def default(self, arg):
        if isinstance(arg, datetime):
            # 아예 dict 를 만들어서 나가기
            obj = dict(
                datatype='datetime',
                iso=arg.isoformat(),
                date=arg.date().isoformat(),
                time=arg.time().isoformat(),
                year=arg.year,
                month=arg.month,
                hour=arg.hour,
                minutes=arg.minute,
                seconds=arg.second
            )
            return obj
        else:
            return super().default(arg)


target_dict = {'time': datetime.utcnow()}
print(json.dumps(target_dict, cls=CustomDateEncoder, indent=2))
