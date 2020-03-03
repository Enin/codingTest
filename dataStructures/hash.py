# hash()함수 사용(내장)
kim = hash('Kim')
john = hash('john')

print(kim, john)

# hash()함수는 프로그램 재시작 마다 해시값이 변경된다.
# 고정된 해시값이 필요할 경우에는 hashlib 라이브러리를 사용한다.
import hashlib  # 배터리 인클루드. 필요한것은 기본 내장되어있다.

h = hashlib.sha256()
h.update(b'Kim')


str1 = b'name' # 하지 않으면 TypeError: Unicode-objects must be encoded before hashing 에러가 발생.
# 해싱 이전에 항상 유니코드 인코딩을 수행해 주어야함.
# 방법은 문자열 앞에 b 혹은 str1.encode('utf-8') 과같은 식으로 인코딩 수행.
# b'name'에서 b는 문자열을 byte형으로 변경해줌.
h.update(str1)
result = h.hexdigest()
print(result)