streamlit run app.py
import streamlit as st
st.write('안녕하세요 리쿠 여친입니다.')

# 마크다운
st.markdown('''
# 이 글은 마크다운으로 작성됨
            1. 항목
            ** 중요한 내용**
            ''')


# 탭
st.tabs(["메뉴1", "메뉴2", "메뉴3"])
tab1, tab2, tab3 = st.tabs(["메뉴1", "메뉴2", "메뉴3"])

with tab1:
    st.write("첫 번째 탭입니다.")
    with st.expander("자세히보기:)" \
        st.write('숨겨진 내용')
        
        ")
with tab2:
    st.write("두 번째 탭입니다.")
    a = st.selectbox("기능", "복사","붙여넣기""자르기"])
    st.write()

with tab3:
    st.write("세 번째 탭입니다.")