# DemoStr.py 
data = "<<<  spam and ham  >>>"
result = data.strip("<> ")
print(data)
print(result)
result = result.replace("spam", "spam egg")
print(result)
print("---리스트로 변환")
lst = result.split() 
print(lst)
print("---하나의 문자열로 합치기---")
print(":)".join(lst))

strA = "python is very powerful"
print(len(strA))
print(strA.capitalize())
print(strA.upper())
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

#정규표현식 
import re 

#함정을 추가
result = re.search("[0-9]*th", "  35th")
#매칭 객체 리턴 
print(result)
print(result.group())
#블럭을 선택 주석처리:ctrl + / 
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())

result = re.search("\d{4}", "올해는 2024년입니다.")
print(result.group())

result = re.search("\d{5}", "우리동네는 52100")
print(result.group())

