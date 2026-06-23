import streamlit as st

st.set_page_config(page_title="인공지능 모델링", page_icon="🤖")

st.markdown("# 🤖 4. 인공지능 모델링")
st.sidebar.header("4. 인공지능 모델링")

st.write(
    """
    ### 모델 학습 및 평가
    전처리된 데이터를 바탕으로 머신러닝/딥러닝 모델을 학습시키고 그 성능을 평가합니다.
    
    * **사용된 알고리즘:** Random Forest, XGBoost 등
    * **성능 지표:** Accuracy, F1-Score, RMSE 등
    """
)
