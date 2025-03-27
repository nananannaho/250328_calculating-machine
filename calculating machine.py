import streamlit as st


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Negation"
    return x / y

def quo(x, y):
    return int(x) // int(y)

def rem(x, y):
    return int(x) % int(y)

st.title("🧮 간단한 계산기")


api_key = st.text_input("API 키를 입력하세요:")

if api_key:
    st.write("API 키가 입력되었습니다.")
else:
    st.write("API 키를 입력해주세요.")
    

st.write("두 숫자를 입력하고 원하는 연산을 선택하세요.")

num1 = st.number_input("첫 번째 숫자", value=0)
num2 = st.number_input("두 번째 숫자", value=0)

operation = st.selectbox(
    "연산을 선택하세요",
    ("덧셈", "뺄셈", "곱셈", "나눗셈", "몫 구하기", "나머지 구하기")
)


if st.button("계산하기"):
    if operation == "덧셈":
        result = add(num1, num2)
        st.success(f"결과: {num1} + {num2} = {result}")
    elif operation == "뺄셈":
        result = sub(num1, num2)
        st.success(f"결과: {num1} - {num2} = {result}")
    elif operation == "곱셈":
        result = mul(num1, num2)
        st.success(f"결과: {num1} * {num2} = {result}")
    elif operation == "나눗셈":
        result = div(num1, num2)
        st.success(f"결과: {num1} / {num2} = {result}")
    elif operation == "몫 구하기":
        result = quo(num1, num2)
        st.success(f"결과: {num1} // {num2} = {result}")
    elif operation == "나머지 구하기":
        result = rem(num1, num2)
        st.success(f"결과: {num1} % {num2} = {result}")
else:
    st.warning("계산을 하려면 '계산하기' 버튼을 눌러주세요.")
