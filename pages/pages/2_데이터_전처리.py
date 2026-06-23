import streamlit as st
import pandas as pd

st.set_page_config(page_title="데이터 전처리", page_icon="🧹")

st.markdown("# 🧹 2. 데이터 전처리")
st.sidebar.header("2. 데이터 전처리")

st.write(
    """
    ### 데이터 정제 과정
    수집한 원본 데이터를 분석에 적합한 형태로 가공하는 과정을 설명합니다.
    
    * 결측치(Missing Value) 처리
    * 이상치(Outlier) 제거
    * 데이터 인코딩 및 스케일링
    """
)

# 예시용 더미 데이터프레임
# df = pd.DataFrame({'예시 칼럼': [1, 2, 3]})
# st.dataframe(df)
