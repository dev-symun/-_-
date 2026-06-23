import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="AI Data Project",
    page_icon="🏠",
    layout="wide"
)

st.title("데이터 분석 및 인공지능 모델링 프로젝트 🚀")

st.sidebar.success("왼쪽 메뉴에서 원하는 페이지를 선택하세요.")

st.markdown(
    """
    이 웹사이트는 문제 정의부터 인공지능 모델링까지의 전체 파이프라인을 보여주는 포트폴리오 템플릿입니다. 
    좌측 사이드바를 통해 각 단계별 상세 페이지로 이동할 수 있습니다.
    
    ### 👨‍💻 프로젝트 팀원
    * 20201 감현우
    * 20204 김서준
    * 20208 박재혁
    * 20210 오승우
    
    ---
    
    ### 📝 프로젝트 개요
    이곳에 프로젝트의 간단한 소개나 목표를 작성해주세요.
    """
)
