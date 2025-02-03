import streamlit as st


def run_home() :
    st.text('')

    st.subheader('과거 데이터를 기반으로 자동차 거래 가격 예측이 이루어집니다.')
    st.info('데이터 출처 : Car_Purchasing_Data.csv (Kaggle)')
    st.text('')

    st.text('EDA 탭에서는 과거 데이터 분석을 실시하며, ML 탭에서는 신규 데이터 예측을 실시합니다.')
    st.subheader('')
    
    st.image('image/car2.jpg', use_container_width = True)