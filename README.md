# 2022년 KT와 함께하는 상명 AI 경진대회

<img src="https://github.com/JHyun0302/2022_AI_Contest/assets/60764632/e53aabca-f803-40f8-a24e-d5c70470959d"  width="300" height="400">

## 문제 : AI를 활용해서 경제, 사회 문제 개선 및 해결

- 팀명 : 지니 PICK ME
- 팀원 : 김덕륜, 신현빈, 이재현, 장태환
- 주제 : Ai를 이용한 가정 내 안전 지킴이
    - 선정 이유 : 해마다 증가하는 강력범죄 + 위급 상황 발생은 예측 불가능 -> 위급 상황 해결 프로그램 필요!

- 기존 프로그램의 단점
    1. MUM Algorithm : 수동적인 신고 기능
    2. NUGU : 정확한 상황 분석 불가

- 개발 목표 : **능동적**이고 **정확**한 **위급 상황 분석 신고 시스템**
    1. 위험 상황으로 판단한 경우 위급 상황 모델을 사용
    2. 즉각적인 신고 - 지정된 문장을 통한 문자 발송, 일반 신고 - 상황 점수에 따른 신고
    3. 평상시에는 감정 모델 사용
    4. 음악 추천 및 글귀(명언) 추천

- 개발 내용
    1. AI HUB 및 Google의 Open Api를 이용해 STT/TTS 기능 구현
    2. AI HUB의 위급상황 관련 [Open Data](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=170)를 이용해 데이터 전처리 및 AI 모델 생성 
    3. AI HUB의 감정 관련 [Open Data](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=86)를 통해 데이터 전처리 및 AI 모델 생성

- 프로그램 구조
    1. 사용자의 **음성에 반응**하고, **지정문장**을 통한 신고기능 탑재
    2. **모델 학습** : 사용자의 특징과 텍스트 추출
    3. **상황 조치** : 상황분석을 하여 알맞은 상황도출 

- 기대효과
    1. **능동적인 신고** : AI의 판단 하에 능동적인 신고 가능
    2. **상황 악화 방지** : 범죄 상황의 극단적 결과 예방 가능
    3. **맞춤형 케어 서비스 제공** : 사용자와 유대감을 형성

- [시연 영상](https://github.com/JHyun0302/2022_AI_Contest/assets/60764632/5e000bb3-2bed-474a-8452-94ab90245402)
  