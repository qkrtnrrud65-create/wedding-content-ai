import streamlit as st
import google.generativeai as genai
from PIL import Image
from datetime import date

# ── 1. 페이지 레이아웃 & 스타일링 ──
st.set_page_config(
    page_title="예랑이의 올인원 콘텐츠 자동 공장 (Claude SEO Engine)",
    page_icon="💍",
    layout="wide"
)

st.markdown("""
<style>
    .main-header { font-size: 25px; font-weight: 800; color: #1E293B; margin-bottom: 4px; }
    .sub-header { font-size: 14px; color: #64748B; margin-bottom: 18px; }
    .stTabs [data-baseweb="tab-list"] { gap: 6px; }
    .stTabs [data-baseweb="tab"] { border-radius: 8px; padding: 8px 16px; font-weight: 700; font-size: 14px; }
    .dday-badge { background-color: #EEF2FF; color: #4F46E5; padding: 4px 10px; border-radius: 12px; font-weight: bold; }
    .seo-badge { background-color: #ECFDF5; color: #059669; padding: 4px 10px; border-radius: 12px; font-weight: bold; font-size: 12px; }
</style>
""", unsafe_allow_html=True)

# ── 2. 사이드바 (D-Day & 가이드) ──
st.sidebar.title("⚙️ 시스템 설정")
api_key = st.sidebar.text_input("Gemini API Key 입력", type="password", help="Google AI Studio 무료 API 키를 넣어주세요.")

today = date.today()
wedding_day = date(2026, 12, 13)
d_day = (wedding_day - today).days

st.sidebar.markdown(f"""
---
### 🤵 본식 D-Day 카운트
- **예식일**: 2026년 12월 13일
- **남은 일정**: <span class="dday-badge">D-{d_day}일</span>
- **체중 변화**: **82.0kg ➡️ 현재 진행형!**
---
### 🚀 탑재된 엔진
- **문체**: Claude 스타일 (생생한 인간미)
- **SEO**: <span class="seo-badge">claude-seo (E-E-A-T & GEO)</span>
---
**💰 파이프라인 팁**
- **쓰레드**: 1번 대댓글에 티스토리/제휴 링크
- **인스타**: 스토리에 링크 스티커
- **네이버**: 맛집/가전 협찬 (식비 0원)
- **티스토리**: 애드센스 고단가 달러 채굴
""", unsafe_allow_html=True)

# ── 3. 메인 입력 화면 ──
st.markdown('<div class="main-header">💍 예랑이의 원클릭 콘텐츠 공장 (Claude SEO Engine)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">다이어트, 데이트, 결혼준비, 신혼집 인테리어까지 구글 상위노출 최적화로 자동 작성됩니다.</div>', unsafe_allow_html=True)

col_in, col_out = st.columns([1, 1.25], gap="large")

with col_in:
    st.subheader("📝 콘텐츠 정보 입력")
    
    mode = st.radio(
        "작성 모드 선택",
        ["📅 [실시간] 현재 다이어트 & 주말 데이트", 
         "🏠 [신혼집/인테리어] 발품·가전가구·셀프 수리/꾸미기",
         "⏪ [역주행] 82kg 시절 결혼 준비 에피소드",
         "📍 [쓰레드 특화] 지하철역/지역 핫플 큐레이션 코스"],
        index=0
    )
    
    selected_sub = ""
    station_name = ""
    
    if "신혼집/인테리어" in mode:
        selected_sub = st.selectbox(
            "신혼집 세부 주제 선택",
            [
                "🏠 [임장/계약] 신혼집 구하기 발품 데이트 & 대출 팁",
                "🔌 [신혼 가전] 가전 졸업 견적 비교 (LG vs 삼성 발품 후기)",
                "🛋️ [가구/소품] 내돈내산 매트리스·소파·식탁 실사용 후기",
                "🔨 [셀프 수리/DIY] 조명·수전·문고리·실리콘 셀프 시공기",
                "✨ [랜선 집들이] 좁은 공간 200% 살리는 수납/배치 꿀팁"
            ]
        )
    elif "역주행" in mode:
        selected_sub = st.selectbox(
            "웨딩 준비 에피소드 선택",
            [
                "Ep.0 [프롤로그] 82kg 찍고 웨딩박람회 갔다가 충격받은 썰",
                "Ep.1 [웨딩박람회] 첫 박람회 솔직 후기 & 호갱 탈출 체크리스트",
                "Ep.2 [웨딩홀 투어] 베뉴 투어 데이트 & 뷔페 시식 식단 방어 팁",
                "Ep.3 [웨딩 밴드] 종로/백화점 반지 투어 데이트 & 손가락 붓기 관리",
                "Ep.4 [맞춤 예복] 80kg대 핏 vs 70kg대 핏 비교 & 수트 가봉",
                "Ep.5 [스튜디오 촬영] 촬영 D-30 벼락치기 감량 & 촬영 도시락 꿀팁",
                "Ep.6 [마운자로 돌파] 정체기 극복과 73kg 안착 비결"
            ]
        )
    elif "핫플 큐레이션" in mode:
        station_name = st.text_input("지하철역 또는 지역명 입력", placeholder="예: 방배역, 서촌, 성수동 등")

    uploaded_files = st.file_uploader(
        "📷 사진 업로드 (음식, 체중계, 인테리어, 가구 등 다중 선택)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        cols = st.columns(min(len(uploaded_files), 4))
        for idx, file in enumerate(uploaded_files):
            with cols[idx % 4]:
                st.image(Image.open(file), use_container_width=True)

    current_weight = st.text_input("⚖️ 현재 체중 (kg)", value="73.35")
    place_name = st.text_input("📍 장소 / 상호명 / 제품명", placeholder="예: 방배동 루베르, 이케아 소파 등")
    user_memo = st.text_area(
        "✏️ 메모 / 추가 상황",
        placeholder="예: 닭볶음탕 건더기 위주로 먹고 크림라떼 반 잔 마심. 아침에 -0.9kg 빠져서 기분 좋았음!",
        height=80
    )
    
    generate_btn = st.button("🚀 5개 채널 콘텐츠 일괄 생성", type="primary", use_container_width=True)

# ── 4. 백엔드 시스템 프롬프트 ──
PROMPT_PAYLOAD = f"""
너는 Claude 특유의 세련되고 솔직한 인간미를 가진 상위 1% 전문 크리에이터이자, 'claude-seo' 표준을 준수하는 SEO 아키텍트야.
절대로 뻔한 AI 말투(교과서식 설명, '알아보겠습니다', '매우 중요합니다' 등)를 쓰지 말고, 2030 직장인이 친구에게 말하듯 위트 있고 생생한 어조를 유지해.

[작성자 페르소나]
- 12월 13일 본식을 앞둔 예비 신랑 (현재 본식 D-{d_day}일).
- 최고 몸무게 82.0kg에서 시작해 현재 {current_weight}kg까지 감량 성공 중.
- 맛있는 주말 외식 데이트와 신혼집 꾸미기(가전/가구/DIY)를 즐기며, 마운자로 치료 병행 + 고단백 식단 + 영양제로 체중을 방어함.
- 쓰레드 4,200명 팔로워를 보유하고 있으며, '번호 매김 핫플 큐레이션'으로 반응이 입증됨.
- 인스타그램은 지인들에게 비밀인 익명 부계정임.

[입력 데이터]
- 모드: {mode}
- 세부 항목: {selected_sub if selected_sub else station_name}
- 현재 체중: {current_weight} kg (시작: 82.0kg)
- 장소/제품: {place_name}
- 메모: {user_memo}

첨부된 사진과 위 정보를 바탕으로 아래 5개 섹션을 완벽하게 작성해줘.

---
### [작업 1: 핵심 분석/견적 표]
- 사진에 음식이 있다면: 1인분 기준 칼로리, 탄수화물, 단백질, 지방 영양 분석표 작성.
- 인테리어/가전/가구라면: [제품명/항목, 구매처, 예상 비용, 만족도, 실전 꿀팁] 요약표 작성.

### [작업 2: 쓰레드 (Threads)]
- 본문 (500자 이내): 
  * 핫플 모드: 서촌 서식 스타일 `📍 [지역/역] 힐링 데이트 & 핫플 코스 7~8곳` 번호 매김(1 매장명 - 특징).
  * 일반 모드: 82kg 감량 썰, D-Day, 외식 방어, 신혼집 꾸미기 썰을 특유의 담백하고 위트 있는 문체로 작성.
- 1번째 대댓글(타래): 티스토리 블로그 상세 후기 링크 유도 + 쿠팡/오늘의집/토스 추천 구매 링크(공정위 문구 포함).

### [작업 3: 인스타그램 (익명 부캐)]
- 첫 줄: 스크롤을 멈추게 하는 도파민 유발 후킹 카피 (Before & After, D-Day, 솔직 고백).
- 본문: 잡지 카드뉴스 스타일의 여백과 이모지(💍, ☕, ⚖️, 🏠). 모바일 최적화 줄바꿈.
- 스토리 24시간 링크 스티커 활용 가이드 + 저장/댓글 유도 CTA + 타깃 해시태그 15개.

### [작업 4: 네이버 블로그 (체험단 & 상위노출용)]
- 제목 3가지 추천 (지역 맛집/웨딩 키워드 + 다이어트 감량 스토리).
- 본문: 네이버 스마트에디터 감성(친근한 어투, 구분선, 인용구 박스). 사진 위치 [사진 1], [사진 2] 지정.
- 식당/제품의 디테일한 장단점 및 실전 방어 꿀팁.
- 하단 [견적/엑셀 시트 비밀댓글 나눔 이벤트] 문구 포함 (본문 내 직접 제휴 링크는 철저히 배제해 저품질 100% 방지).

### [작업 5: 티스토리 블로그 (claude-seo 표준 구글 최적화)]
- **H1 포스팅 제목**: 검색 사용자의 검색 의도를 100% 관통하는 구체적 롱테일 키워드 결합.
- **메타 디스크립션**: 150자 이내의 구글 SERP 노출용 요약문.
- **GEO(AI Search) 리치 스니펫 요약 Box**: 구글 AI 오버뷰와 Perplexity가 답변 출처로 인용할 수 있도록 [3줄 핵심 요약 + 1차 정량 데이터(체중, 감량치, 칼로리)] 박스 구성.
- **본론 구조**: H2, H3 시맨틱 태그 준수 및 애드센스 광고 삽입 앵커(`<!-- [애드센스 중간 광고] -->`).
- **FAQ 스키마 섹션**: 독자들이 가장 궁금해할 질문과 답변 2~3세트(Q&A) 작성.
- **하단 면책 조항 (Disclaimer)**: E-E-A-T 신뢰성을 위한 전문적 안내문 박스.

---
반드시 아래 구분자를 사용해서 순서대로 출력해줘:
<<<SUMMARY_SECTION>>>
(작업 1 내용)
<<<THREADS_SECTION>>>
(작업 2 내용)
<<<INSTAGRAM_SECTION>>>
(작업 3 내용)
<<<NAVER_SECTION>>>
(작업 4 내용)
<<<TISTORY_SECTION>>>
(작업 5 내용)
"""

# ── 5. AI 호출 및 결과 탭 출력 ──
with col_out:
    st.subheader("📄 플랫폼별 생성 결과")
    
    if generate_btn:
        if not api_key:
            st.error("⚠️ 사이드바에 Gemini API Key를 먼저 입력해주세요!")
        else:
            with st.spinner(f"Claude SEO 엔진이 5개 채널 콘텐츠를 최적화하여 작성 중입니다 (본식 D-{d_day})..."):
                try:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel("gemini-3-flash-preview")
                    
                    content_inputs = []
                    if uploaded_files:
                        content_inputs.extend([Image.open(f) for f in uploaded_files])
                    content_inputs.append(PROMPT_PAYLOAD)
                    
                    response = model.generate_content(content_inputs)
                    result_text = response.text
                    
                    sections = {}
                    current_tag = None
                    for line in result_text.splitlines(keepends=True):
                        if "<<<SUMMARY_SECTION>>>" in line:
                            current_tag = "SUMMARY"
                            sections[current_tag] = ""
                        elif "<<<THREADS_SECTION>>>" in line:
                            current_tag = "THREADS"
                            sections[current_tag] = ""
                        elif "<<<INSTAGRAM_SECTION>>>" in line:
                            current_tag = "INSTAGRAM"
                            sections[current_tag] = ""
                        elif "<<<NAVER_SECTION>>>" in line:
                            current_tag = "NAVER"
                            sections[current_tag] = ""
                        elif "<<<TISTORY_SECTION>>>" in line:
                            current_tag = "TISTORY"
                            sections[current_tag] = ""
                        else:
                            if current_tag:
                                sections[current_tag] += line
                                
                    st.session_state["claude_seo_output"] = sections
                    st.balloons()
                    st.success("🎉 Claude SEO 최적화 콘텐츠 생성이 완료되었습니다!")
                except Exception as e:
                    st.error(f"오류가 발생했습니다: {e}")

    if "claude_seo_output" in st.session_state:
        res = st.session_state["claude_seo_output"]
        
        tab_th, tab_ig, tab_nb, tab_ts, tab_sm = st.tabs([
            "🧵 쓰레드 (트래픽/수익)",
            "📱 인스타그램 (부캐)", 
            "🟢 네이버 블로그", 
            "🟠 티스토리 (Claude SEO)", 
            "📊 분석/견적 요약표"
        ])
        
        with tab_th:
            st.text_area("쓰레드 본문 & 1번 대댓글 복사용", value=res.get("THREADS", ""), height=450)
        with tab_ig:
            st.text_area("인스타그램 캡션 복사용", value=res.get("INSTAGRAM", ""), height=450)
        with tab_nb:
            st.text_area("네이버 블로그 본문 복사용", value=res.get("NAVER", ""), height=450)
        with tab_ts:
            st.text_area("티스토리 마크다운 (구글 SEO 최적화)", value=res.get("TISTORY", ""), height=450)
        with tab_sm:
            st.markdown(res.get("SUMMARY", "요약 데이터가 없습니다."))
    else:
        st.info("왼쪽에서 정보를 입력하고 '생성' 버튼을 누르면 5개 탭에 결과가 표시됩니다.")
