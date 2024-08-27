import re

def is_valid_email(email):
  """
  주어진 이메일 주소가 유효한 형식인지 검사합니다.

  Args:
    email: 검사할 이메일 주소 문자열

  Returns:
    bool: 유효한 이메일이면 True, 아니면 False
  """

  # 일반적인 이메일 형식에 대한 정규 표현식
  email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

  return re.match(email_regex, email) is not None

# 샘플 이메일 리스트
emails = [
  "valid@example.com",
  "invalid@example",
  "another.valid@mail.co.kr",
  "with+symbols@example.com",
  "numbers123@domain.org",
  "too.many.dots@something.com",
  "no.at.sign",
  "underscore_is_ok@domain.com",
  "hyphen-is-also-ok@domain.com",
  "numbers-and_symbols@123.com"
]

# 각 이메일 검사
for email in emails:
  if is_valid_email(email):
    print(f"{email} is a valid email address.")
  else:
    print(f"{email} is not a valid email address.")