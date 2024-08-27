import re

def is_valid_email(email):
    # 이메일 주소의 유효성을 검사하는 정규 표현식
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # 정규 표현식과 이메일 주소를 매칭시켜 유효성 검사
    return re.match(email_regex, email) is not None

# 샘플 이메일 주소 10개
sample_emails = [
    "valid.email@example.com",      # 유효한 이메일
    "invalid-email.com",            # @ 기호가 없는 이메일
    "another.valid.email@domain.org", # 유효한 이메일
    "user@.com",                    # 도메인 부분이 잘못된 이메일
    "user@domain.com.",             # 도메인 끝에 마침표가 있는 이메일
    "user@domain..com",             # 도메인에 연속된 마침표가 있는 이메일
    "user.name@domain.co.in",       # 유효한 이메일
    "user-name@domain.co.uk",       # 유효한 이메일
    "@missingusername.com",         # 사용자 이름이 없는 이메일
    "username@domain.c",            # 최상위 도메인이 너무 짧은 이메일
]

# 이메일 주소 검사
for email in sample_emails:
    if is_valid_email(email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is NOT a valid email address.")
