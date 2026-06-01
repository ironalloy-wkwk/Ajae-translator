import streamlit as st
from google import genai
from google.genai import types

# 1. 웹페이지 설정
st.set_page_config(page_title="AI 아재투 변환기", page_icon="👴", layout="centered")

# 2. 구글 AI Studio에서 발급받은 API 키를 여기에 입력하세요!
# (무료로 발급 가능합니다)
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

st.title("👴 휴먼틀딱체 도우미")
st.caption("제미나이 AI가 문맥을 파악해 실시간으로 완벽한 아재 톤을 구사합니다;; 허허;;")
st.markdown("---")

# 3. 입력창
user_input = st.text_area(
    "원래;;;;; 문장을;;;;;; 입력;;;;하세여;;;", 
    value="음,,, 무엇을;;, 번역;; 해; 드려야;; 됄까나여;; 허허허,,, 총총,,",
    height=150
)

# 4. 변환 버튼
if st.button("✨ 아재 톤으로 변환하기,,,!!", use_container_width=True):
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY":
        st.error("API 키를 코드의 GEMINI_API_KEY 칸에 입력해주셔야 작동함돠;; 쿨럭;;")
    elif user_input.strip() == "":
        st.warning("문장을 입력해 주셔야,,, 변환을 하든가 말든가 함돠;;;")
    else:
        with st.spinner("아재가 돋보기안경 쓰고 생각 중,,,쿨럭"):
            try:
                # 최신 Google GenAI 클라이언트 초기화
                client = genai.Client(api_key=GEMINI_API_KEY)
                
                # 가성비 최고 + 속도 광속인 gemini-2.5-flash 모델 사용
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input,
                    config=types.GenerateContentConfig(
                        system_instruction=(
                            "너는 인터넷 커뮤니티나 네이버 밴드를 열심히 하는 60대 아저씨야. "
                            "입력받은 문장을 아주 킹받고 극단적인 '휴먼틀딱체(아재 말투)'로 변환해줘.\n\n"
                            " [필수 지침]\n"
                            "1. 문장 단어 사이사이에 쉼표(,)와 세미콜론(;)을 아주 많이 쑤셔 넣을 것. (예: 문장,,, 중간에;;; 이렇게)\n"
                            "2. '회원님들'은 '횐님덜'로 바꾸고, '좋나요'는 '낳나여'나 '됴으나여'처럼 맞춤법을 미묘하게 파괴할 것.\n"
                            "3. 문장 끝에는 무조건 '허허,,,', '~~!!!', ' 쿨럭,,;', ' 총총,,,' 같은 아재식 감탄사나 말줄임표를 붙여서 마무리할 것.\n"
                            "4. 원문의 뜻(질문이나 정보)은 완벽히 유지해야 함."
                        )
                    )
                )
                
                # 결과 출력
                st.markdown("### 👴아재의 답변인듸,,,")
                st.success(response.text)
                
            except Exception as e:
                st.error(f"오류가 발생했음돠;; 주소록 확인 요망;;: {e}")
