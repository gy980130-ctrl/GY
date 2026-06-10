import streamlit as st
st.title('안녕하세요 제목입니다')

# 마크다운
st.markdown('''
            # 이 글은 마크다운으로 작성됨
            1. 항목
            - **중요한 내용**
            ''')
# 탭
tab1, tab2, tab3 = st.tabs(["메뉴1", "메뉴2", "메뉴3"])

st.image('리쿠.jpg')
