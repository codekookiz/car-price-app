import streamlit as st

from ui.eda import run_eda
from ui.home import run_home
from ui.ml import run_ml


def main() :
    st.title('자동차 거래 가격 예측 앱')
    
    st.sidebar.title('SIDEBAR')
    menu = ['HOME', 'EDA', 'ML']
    choice = st.sidebar.selectbox('MENU', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()


if __name__ == '__main__' :
    main()