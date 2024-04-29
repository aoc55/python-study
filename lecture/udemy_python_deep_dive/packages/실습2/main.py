# <방법1>
# - 일일히 구조에 따라서 직접 Import
# - import 도 구조에 따라서 직접 수행
import common.validators.date
import common.validators.boolean

# - 코드 호출 관점에서도 별로임
common.validators.date.is_date("aa")


# <방법2>
# - common.validators.__init__.py 에 import 구문 추가
#       "__init__.py"
#           import common.validators.boolean
#           import common.validators.date

# - 사용자 입장에서 import 는 한번만 수행
# import common.validators

# - 그러나 코드 호출 관점에서는 변경 없음
# common.validators.date.is_date("aa")


# <방법3>
# from common.validators import *
# - 위와 같은 방식 사용 지양
# - (모두 노출됨 네임스페이스 오버라이딩 오류 , 버그)


# <방법4>
# - common.validators.__init__.py 에 import 구문 시 * 사용
#       "__init__.py"
#           from .date import *
#           from .boolean import *
#           from .json import *
# - 물론 __init__ 사용 시 import * 주의 필요

# - 사용자 입장에서는 제일 깔끔함
# import common.validators as validators
#
# validators.date.is_date("aa")
# validators.is_json("")
# validators.is_date("")
# validators.is_boolean("")
# validators.boolean_helper_2()
#
# # - Global Namespace 내 validator Reference 의 Dict 조회 시 노출한 하위모듈 기능 있음
# for k in validators.__dict__.keys():
#     print(k)
#
#
# print("\n---\n")


import common.validators as validators
import common.models as models

# import common.models.posts.post
# john_post = common.models.posts.post.Post()

# import common.models.posts
# john_posts = common.models.posts.Posts()
# john_post = common.models.posts.Post()
#
# import common.models.users
# john_user = common.models.users.User()

# Nested 구조
john_posts = models.Posts()
john_post = models.Post()
john_user = models.User()


# __init__.py 에 있는 메서드 사용해보기
print(models.say_hello("hi"))

print("<< globals >>")
for k in dict(globals()).keys():
    print(k)
print("--\n\n")

print("<< validators >>")
for k in common.validators.__dict__.keys():
    print(k)
print("--\n\n")


print("<< models >>")
for k in common.models.__dict__.keys():
    print(k)
print("--\n\n")






