
import streamlit as st
st.write('안녕하세요 리쿠 여친입니다.')

st.markdown('''
    앤시티위시 아랑해
            1. nctwish
            ** 중요한 내용**
            ''')

st.tabs(["메뉴1", "메뉴2", "메뉴3"])
tab1, tab2, tab3 = st.tabs(["메뉴1", "메뉴2", "메뉴3"])


with tab1:
    st.write("첫 번째 탭입니다.")
    with st.expander("자세히보기"):
        st.write('숨겨진 내용')
        
with tab2:
    st.write("두 번째 탭입니다.")
    a = st.selectbox("기능", ["복사", "붙여넣기", "자르기"])
    st.write("선택한 기능:", a)

with tab3:
    st.write("세 번째 탭입니다.")
if st.button('버튼누르기'):
    st.write('버튼이 눌렸습니다.')
