#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 15:23:51 2025

@author: moongwibok
"""

# 파일 이름: life_saju_app_v3.py
# 기존 파일 덮어쓰기 하거나 새로 만들어서 저장!

import streamlit as st
import random

# 리스트는 이전과 동일 (생략 없이 그대로 복사해서 써!)
past_lives = [
    "고대 이집트 피라미드 건축 감독관", "조선 시대 한양에서 한옥 대장장이", "중세 유럽 기사단의 전령",
    "고려 시대 개경에서 도공(옹기장)", "삼국시대 백제의 무역 상인", "바이킹 배의 항해사",
    "로마 제국의 검투사 훈련 교관", "실크로드 대상회의 낙타지기", "조선 선비이면서 몰래 시조 쓰는 시인",
    "일제강점기 독립군 연락원", "1960~70년대 서울 다방 DJ", "1980년대 PC통신 고수 해커",
    "1990년대 홍대 인디밴드 드러머", "2000년대 초반 스타크래프트 프로게이머", "2010년대 유튜브 1세대 먹방 크리에이터",
    "고려 말 왜구 토벌군 장군", "조선 중기 한양에서 약재 장수", "대한제국 시기 독립신문 기자",
    "신라 화랑이었던 무신", "백제 무령왕 시대 금속공예 장인", "고구려 벽화 그리는 화공",
    "조선 시대 몰래 천주교 서적 인쇄한 사람", "일제강점기 상하이 임시정부 요원", "6.25 때 학도병",
    "1970년대 공업고등학교 야간부 다니며 공장 근무", "1997년 IMF 때 사업 접고 재기한 자영업자",
    "2002년 월드컵 거리 응원 단골", "2016년 촛불집회 매주 나온 시민", "2020년 코로나 첫해 마스크 제작 봉사자",
    "2024년 파리 올림픽 펜싱 경기장에서 응원 온 아빠"
]

future_lives = [
    "2035년 달 기지에서 한국식 김치 재배 농부", "2040년 6G 시대 VR 콘텐츠 세계 1위 크리에이터",
    "2038년 자율주행 택시 회사의 한국 지사장", "2050년 노벨 문학상 받은 한국 SF 소설가",
    "2045년 AI 윤리 위원회 유일한 인간 위원", "2033년 웹툰 원작 드라마로 세계적 히트 친 작가",
    "2042년 메타버스 부동산으로 큰돈 번 투자자", "2030년 전기차 배터리 재활용 공장 창업자",
    "2055년 100세 넘게 살면서 유튜브 ‘할배 ASMR’ 운영", "2037년 K-팝 5세대 아이돌 프로듀서",
    "2048년 해저 도시 건설 프로젝트 한국 팀장", "2032년 올림픽 양궁 금메달리스트 코치",
    "2050년 기후난민 구호 활동으로 노벨평화상 후보", "2040년 우주여행 티켓 1호 당첨자",
    "2035년 AI가 만들어준 맞춤 향수 세계 판매 1위", "2060년 한국 최초 화성 이주민",
    "2039년 전국 팔도 음식 메타버스 박물관 관장", "2045년 AI 대통령 선거 출마 (농담 반 진담 반)",
    "2052년 은퇴 후 제주도에서 펭귄 카페 운영", "2031년 로또 1등 당첨 (진짜 될 수도?)",
    "2040년 넷플릭스 오리지널 한국 좀비 드라마 주연", "2058년 손자와 함께 e스포츠 대회 우승",
    "2036년 서울에서 가장 긴 장수 식당 3대째 이어받음", "2049년 전 세계 한글날 기념 강연 다니는 한글 전도사",
    "2033년 갑자기 떼돈 벌어서 전 재산 기부하고 수행길 떠남", "2055년 한국 최초 민간 우주정거장 건설 투자자",
    "2042년 AI랑 결혼해서 화제 된 사람", "2038년 전국에서 제일 맛있는 떡볶이 집 사장",
    "2050년 아직도 현역 프로그래머로 일하면서 후배들 멘토링", "2070년 72세에 대학 새내기 되는 늦깎이 대학생"
]

st.title("🔮 나의 전생 · 사주 · 미래 시뮬레이터 v3.0")
st.markdown("**이제 너가 직접 전생 고른다!**")

with st.sidebar:
    st.header("입력해줘")
    name = st.text_input("이름(별명)", "갑목이")
    birth_input = st.text_input("생년월일 8자리", "19980711")
    birth_hour = st.slider("출생 시간(대략)", 0, 23, 12)

    if st.button("운명 분석 시작!", type="primary"):
        if len(birth_input) != 8 or not birth_input.isdigit():
            st.error("생년월일을 8자리로 정확히 입력해줘!")
        else:
            year = int(birth_input[:4])
            random.seed(year + birth_hour + sum(ord(c) for c in name))  # 재현성

            # 10개 전생 후보 뽑기
            selected_past = random.sample(past_lives, 10)
            st.session_state.selected_past = selected_past
            st.session_state.name = name
            st.success("10개 전생 후보 생성 완료! 아래에서 골라봐")

# 전생 10개 보여주고 체크박스로 선택하게 하기
if "selected_past" in st.session_state:
    st.subheader("⏪ 태어나기 전 ~ 지금까지 가능한 10가지 삶")
    st.write("**마음에 드는 2~3개를 직접 골라봐!**")

    chosen = []
    for i, life in enumerate(st.session_state.selected_past, 1):
        if st.checkbox(f"{i}. {life}", key=f"past_{i}"):
            chosen.append(life)

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("이걸로 확정!", type="primary"):
            if len(chosen) < 2 or len(chosen) > 3:
                st.error("2~3개만 골라줘!")
            else:
                st.session_state.my_past = chosen
                st.success(f"확정! 너의 전생 TOP {len(chosen)}개")

    # 확정된 전생 보여주기
    if "my_past" in st.session_state:
        st.markdown("### ✅ 너가 선택한 전생")
        for i, life in enumerate(st.session_state.my_past, 1):
            st.write(f"**{i}위** → {life}")

        # 미래 10개는 선택한 전생 보고 랜덤 생성
        random.seed(sum(ord(c) for c in "".join(st.session_state.my_past)))
        selected_future = random.sample(future_lives, 10)

        st.markdown("### 🚀 지금부터 펼쳐질 10가지 미래 (너의 전생 영향 반영됨)")
        for i, life in enumerate(selected_future, 1):
            st.write(f"{i}. {life}")

        st.balloons()

st.caption("재미로 즐기는 시뮬레이터예요~ 실제 사주는 전문가분께!")