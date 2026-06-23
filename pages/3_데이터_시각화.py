import streamlit as st

st.set_page_config(page_title="데이터 시각화", page_icon="📊")

st.markdown("# 📊 3. 데이터 시각화")
st.sidebar.header("3. 데이터 시각화")

st.write(
    """
    ### 탐색적 데이터 분석 (EDA)
    데이터의 특성과 변수 간의 관계를 시각적으로 파악한 결과를 보여줍니다.
    
    이곳에 `matplotlib`, `seaborn` 또는 `st.line_chart` 등을 활용한 그래프를 삽입하세요.
    """
)
