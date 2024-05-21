##function(include return)
##return을 통해 함수에서의 값을 다른 함수로 넘겨##(반환해) 줄 수 있다.
def input_name(name):
  return name


def input_age(age):
  return age


def input_number_no_010(number):
  fullnumber = "010" + number
  return fullnumber

##f" "안에 문자열과 {변수}구조를 연결해 ##string(문자열) format을 만들어 줄 수 있다.
def info(name, age, number):
  print(f"이름 : {name} \n나이 : {age} \n전화번호 : {number}")


info(input_name("Sunny"), input_age(100), input_number_no_010("12345678"))
