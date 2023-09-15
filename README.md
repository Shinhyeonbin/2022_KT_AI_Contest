# 2022년 KT와 함께하는 상명 AI 경진대회

<img src="https://github.com/JHyun0302/2022_AI_Contest/assets/60764632/e53aabca-f803-40f8-a24e-d5c70470959d"  width="300" height="400">

## 문제 : AI를 활용해서 경제, 사회 문제 개선 및 해결

- 팀명 : 지니 PICK ME
- 팀장 : 신현빈
- 팀원 : 김덕륜, 이재현, 장태환
- 주제 : Ai를 이용한 가정 내 안전 지킴이
    - 선정 이유 : 해마다 증가하는 강력범죄 + 위급 상황 발생은 예측 불가능 -> 위급 상황 해결 프로그램 필요!

- [최종발표영상](https://www.youtube.com/watch?v=glDVWtJKXDs&list=PL-FC0SY-VRF6jXcQQkp-W2bsvuRQSWuNm&index=6)

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

 - 프로젝트 후 배운 점
    1. **일정관리**
    2. **To_Be 설계**
    3. **문제해결 및 팀원과의 협력**

 - 느낀점
   처음으로 하는 대회 출전이자 팀장으로서 일정을 관리하고 팀을 이끌어나가는 것은 쉬운 일이 아니라고 생각했다.
   특히, 일정관리 부분에서 많은 애로사항이 존재하였다. 예상한 것과 다르게 진행속도가 많이 느렸기 때문이다.
   그래도 많은 사람들 앞 발표와 팀원을 어떤 방식으로 의기투합을하여 문제를 해결하는 과정, 일정 설계 및 이행 등 많은 것을 배울 수 있는 대회라고 생각한다.



   


  
    


- [시연 영상](https://github.com/JHyun0302/2022_AI_Contest/assets/60764632/5e000bb3-2bed-474a-8452-94ab90245402)
  
