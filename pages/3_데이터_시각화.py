import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="데이터 시각화", page_icon="📊")

st.markdown("# 📊 3. 데이터 시각화")
st.sidebar.header("3. 데이터 시각화")

st.write(
    """
    ### 탐색적 데이터 분석 (EDA)
    데이터의 특성과 변수 간의 관계를 시각적으로 파악한 결과를 보여줍니다.
    """
)

# 데이터 불러오기 (캐싱을 통해 속도 향상)
@st.cache_data
def load_data():
    # 데이터 파일 경로 (파일이 같은 폴더에 있다고 가정)
    df = pd.read_csv("sc_cust_info_txn_v1.5.csv")
    return df

# 데이터 로드
try:
    df = load_data()
    
    st.write("#### 🔍 변수 간 상관관계 분석 (히트맵)")
    st.write("수치형 변수들 간의 상관관계를 확인하여, 통신 서비스 이용 패턴이나 요금 등 데이터의 주요 특징 간 연관성을 파악합니다.")

    # 1. 상관관계 분석을 위한 데이터 전처리
    # '_' 같은 문자가 섞여 있어서 문자열로 인식된 컬럼들을 수치형으로 강제 변환
    numeric_df = df.copy()
    for col in numeric_df.columns:
        numeric_df[col] = pd.to_numeric(numeric_df[col], errors='coerce')
    
    # 모든 값이 NaN인 컬럼(수치형으로 변환 불가능한 문자열 컬럼 등) 제거
    numeric_df = numeric_df.dropna(axis=1, how='all')
    
    # 2. 상관계수 계산
    corr = numeric_df.corr()

    # 3. 히트맵 시각화
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        corr, 
        annot=True,          # 박스 안에 상관계수 숫자 표시
        fmt=".2f",           # 소수점 둘째 자리까지 표시
        cmap="coolwarm",     # 색상 팔레트 (파란색: 음의 상관관계, 붉은색: 양의 상관관계)
        vmin=-1, vmax=1,     # 상관계수 최소/최대값
        center=0,
        linewidths=0.5,
        ax=ax,
        annot_kws={"size": 8} # 숫자 크기
    )
    plt.title("Correlation Heatmap of Numeric Variables", fontsize=15)
    plt.xticks(rotation=45, ha='right')
    
    # 4. Streamlit 화면에 그래프 출력
    st.pyplot(fig)

    st.info("💡 **해석 팁:** 빨간색에 가까울수록 양의 상관관계(비례)가 강하고, 파란색에 가까울수록 음의 상관관계(반비례)가 강함을 의미합니다.")

except FileNotFoundError:
    st.error("데이터 파일을 찾을 수 없습니다. 'sc_cust_info_txn_v1.5.csv' 파일이 실행 경로에 있는지 확인해주세요.")
