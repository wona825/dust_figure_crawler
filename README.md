주제 : 지역별 미세먼지 수치

프로젝트 내용:
한국환경공단 에어코리아에서 제시하는 대기오염 정보에서 지역별 미세먼지 수치를 그래프로 나타내보기로 하였다.
구체적으로 지역이름과 미세먼지농도를크롤링하며 지역이름을 x축 미세먼지농도를 y축으로하여 막대그래프를 이용해 표현해보고자한다.


202155185 차지원 역할
크롤링 – 한국환경공단 에어코리아에서 제공하는 지역별 미세먼지 수치 데이터를 Beautiful Soup을 이용해 관련 정보를 포함하고 있는 전체 테이블을 찾아서 반환했다,
         또한 전체 테이블에서 지역 정보를 따로 추출하여 리스트로 만들었다


202155179 조동준 역할
크롤링 – 차지원이 찾은 전체 테이블에서 지역별 미세먼지 농도를 추출해 리스트로 만들었다.
그래프 – 지역별 미세먼지농도를 x축은 지역 y축은 미세먼지농도로하여 막대그래프를 나타내도록 코딩했다.

크롤링할 사이트 URL : https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%88%98%EC%B9%98+%ED%81%AC%EB%A1%A4%EB%A7%81&tqi=h5nGWwp0J1ZssEm7srNssssss3w-357383