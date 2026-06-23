import streamlit as st

st.set_page_config(page_title="문제 정의 및 데이터 수집", page_icon="🎯")

st.markdown("# 🎯 1. 문제 정의 및 데이터 수집")
st.sidebar.header("1. 문제 정의 및 데이터 수집")

st.write(
    """
    ### 문제 정의
    해결하고자 하는 비즈니스 문제나 연구 목표를 여기에 서술합니다.
    
    ### 데이터 수집
    * **데이터 출처:** 캐글(Kaggle), 공공데이터포털 등
    * **수집 방법:** API, 웹 크롤링, CSV 파일 다운로드 등
    """
)
