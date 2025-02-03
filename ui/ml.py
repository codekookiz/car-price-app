import streamlit as st, joblib, numpy as np


def run_ml() :
    st.subheader('')

    st.header('ML (머신러닝)')
    st.text('')

    st.info('고객님의 정보를 바탕으로 예상 자동차 거래 가격을 알려드립니다. \n\n예측에 사용된 개인정보는 서비스 제공 이후 즉시 폐기됩니다.')
    st.text('')

    st.subheader('자동차 거래 가격 예측을 위해 하단 정보를 입력해주세요.')
    st.text('')

    gender = st.selectbox('성별을 선택하세요.', ['남성', '여성'])
    age = st.number_input('나이를 입력하세요.', min_value = 0, max_value = 150, value = 40)
    salary = st.number_input('연봉을 입력하세요.', min_value = 0, step = 10, value = 30000)
    debt = st.number_input('신용카드 부채를 입력하세요.', min_value = 0, step = 10, value = 5000)
    net = st.number_input('순자산을 입력하세요.', step = 10, value = 75000)
    st.subheader('')

    new_gender = 0
    if gender == '남성' :
        new_gender = 1
    elif gender == '여성' :
        new_gender = 0

    new_data = np.array([new_gender, age, salary, debt, net]).reshape(1, 5)
    regressor = joblib.load('model/regressor.pkl')
    pred = regressor.predict(new_data)[0].round(2)

    if st.button('예측 가격 확인') :
        if pred >= 0 :
            st.text('')
            pred = format(pred, ',')
            st.subheader(f'귀하의 자동차 예상 거래 가격은 {pred} 달러입니다.')
        else :
            st.subheader('예측이 불가능한 데이터입니다.')