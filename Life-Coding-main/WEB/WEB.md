# 온라인 에디터
https://codesandbox.io/ - VSCode와 닮았고 Github 연동이 된다!! 간단한 페이지 구성보단, 작은 모델 개발에 적합

https://www.programiz.com/html/online-compiler/ - html, css, javascript 만 간단하게 써보기에 좋은 에디터


------------------
# WEB1 - HTML & Internet
- tag란?
    - html 문서를 구성하는 기본 단위

- html의 기본구조
    - head : html의 머리부분
        - title : 웹페이지의 이름. 가장 위에 나오는 부분
        - link : 연동할 파일의 링크 전달. CSS, js 파일 가져올 때 주로 사용
        - script : js를 html에서 작성하기 위한 태그
        - style : CSS를 html에서 작성하기 위한 태그
        - meta : title, link등이 알려주지 못한 메타데이터를 알려주는 부분
            - e.g. charset을 통해 문서를 읽을 언어를 정의할 수 있음
    - body : html의 몸통부분

- 줄바꿈 : br vs p
    - br : 단순 줄바꿈
    - p : paragraph tag로 '한 문단'을 의미  
          주로 p 태그를 많이 이용함

- div 태그 : 가상의 레이아웃 설계
    - Division의 약자로, 레이아웃을 나누는데 주로 사용됨
    - 다른 태그들과 달리, div 태그 자체에 의미가 있지는 않음
        - 대신에 주로 id 값 부여를 통해 특정한 레이아웃 나누기에 사용

- 링크 태그 : a vs link
    - a : anchor(닻) 이라는 의미로 html에서 다른 페이지와 연결할 때 사용
    - link : 문서나 외부 파일과 연결할 때 사용
    - _href_ : a, link 태그에서 연결할 파일의 URL을 명시
        - href의 속성 값 URL
            - 1. 절대주소 : href=“http://www.tcpschool.com/index.php”
            - 2. 상대주소 : href=“/lecture/logo.png”
            - 3. 같은 페이지 내에서 명시된 id를 가지고 있는 요소 : href=“#bottom”
            - 4. 스크립트 : href=“javascript:alert(‘반갑습니다!’)”
        - target = "_blank" 를 통해 클릭으로 새 페이지 띄우기를 할 수 있다

- 목록 태그 : ol, ul, dl 와 li  
    li는 list item의 약자로 목록을 만드는 태그
    - ol : ordered list의 약자로, 순서가 있는 목록을 만들 때 사용
    - ul : unordered list의 약자로, 순서가 필요 없는 목록을 만들 때 사용
    - dl : definition list의 약자로, 사전처럼 용어를 설명하는 목록을 만듬

- 사진(이미지) 태그 : img
    - src에 사진의 url을 넣어서 사진을 불러올 수 있다
    - width 등과 같은 속성을 통해 사진의 표현을 조절할 수 있다


------------------
# WEB2 - CSS
 - css 태그 : link vs style
    - link : URL을 통해 CSS 파일 연결. 이 방식을 주로 사용
    - style : html 파일에 직접 입력. 잘 안씀
        - __inline style__ : style="background-color:green" 처럼 사용하는 것. style 태그와는 다름

- Selector(선택자), Property(속성), Value(값)
    ```
        a {
            font-size: 50px;
            text-align: center;
        }
    ```
    - Selector : a 에 해당
        - 종류 : 기본 선택자(a), 클래스 선택자(.a), id 선택자(#a)
            - 여기서 id 선택자는 단 하나를 지정해주는 것이기 때문에  
                한번 등장한 id는 그 페이지에서 다시 사용하지 않는 것이 규약임  
                    (동작은 하지만, 규약 위반이기 때문에 하지 말자)
    - Property : font-size, text-align 에 해당
    - Value : 50px, center 에 해당
        - Property : Value;  의 형태로 사용. ';'은 줄 구분용 문자임
        - Declaration(효과) = Property : Value
    - 세부 적용 : #grid ol {} 이라고하면, id="grid" 아래에 ol 태그가 오면 적용하는 style 의미

- CSS 반영 우선순위
    - !important > inline style > id 선택자 > class 선택자 > 기본 선택자
        - !important : 속성값 뒤에 중요표시
        - inline style : 태그 안에 style='' 로 적은 부분

- 박스 모델
    문서의 레이아웃을 계산할 때, 사각형 박스로 영역을 나누는 것
    - content < padding < border < margin 순으로 넓어짐
        - content area(콘텐츠 영역) : 실제 내용을 포함하는 부분
        - padding area(안쪽 여백 영역)
        - border area(테두리 영역)
        - margin area(바깥 여백 영역) : 테두리와 인근 요소 사이의 빈 공간 의미

- display 속성 : inline, block, inline-block, none
    - inline : 줄바꿈 X  (span, a, em 등)
        - width, height 속성은 지정해도 무시됨  
            (태그가 마크업하고 있는 컨텐트의 크기만큼만 공간을 차지하도록 되어있기 때문)
        - margin, padding 속성은 좌우 간격만 반영, 상하는 반영 X
    - block : 전후 줄바꿈 O  (div, p, h1 등)
        - inline과 달리 width, height, margin, padding 모두 반영 O
    - inline-block : 하이브리드 느낌  (button, input, select 등)  
            inline element 처럼 전후 줄바꿈 없이 한 줄에 다른 엘리먼트들과 나란히 배치  
            blcok element처럼 width, height, margin, padding 속성 지정 가능
    - none : 해당 컨텐트가 안보이게 함

- CSS 레이아웃 : flex vs grid
    - flex : 한 방향 레이아웃 시스템 (1차원)
    - grid : 두 방향(가로-세로) 레이아웃 시스템 (2차원)
        - display: grid; 로 사용 (flex면 grid 대신 flex)
    ```
        #grid {
            display: grid;
            grid-template-columns: 150px 1fr;
        }
    ```

- 미디어 쿼리 : css의 if문
    - 페이지의 변화에 css가 반응하도록 해줌
    ```
        @media (조건) {
            스타일
        }
    ```
    - 예를 들어 화면의 폭이 600px보다 작을 때 반응하게 하고싶다면,  
        max-width:600px 을 조건에 넣어주면 된다


------------------
# WEB2 - JavaScript
- script 태그 : js 사용하기
    - script 태그를 통해 js를 html안에 적을 수 있음
    - html과 달리 js는 값을 동적으로 계산함
        - html에서 1+1은 2가 아니지만, js에서는 1+1은 2임

- Event 란?
    - onclick, onchange, onkeydown 등과 같이  
        웹브라우저에서 일어나는 여러 사건들
    - event에 js 코드를 입력해서 원하는 동작을 html에 지정할 수 있음
        - onclick=" 여기서 js 코드 입력 "

- querySelector() 란?
    - CSS 선택자로 요소를 선택하게 해주는 메서드  
        주의할 점은 선택자에 해당하는 첫번째 요소만 선택한다는 것
    - 예를 들어, document.querySelector('.container') 라고하면  
        클래스 값이 container인 첫번째 요소에 접근함

- ReFactoring(리팩토링) 이란?
    - 코드의 중복된 부분을 제거하는 작업  
            다시(re) 공장(factoring) 작업하는 과정
    - 함수, 변수를 통해 중복된 부분 제거

- this, self 의 의미
    - this : 함수를 호출할 때 생성되는 실행 컨텍스트 객체  
        - this가 가리키는 대상은 어떻게 this가 호출되는지에 따라 다름  
            참고 : https://eunjinii.tistory.com/104
    - self : 함수에서 this를 받기위한 매개변수로 주로 사용 (자세한 내용은 구글에서..)  
        - 예시 : function func1(self) {}

- 객체 란?
    - 코드를 잘 정리하기 위한 수납도구(?), Body가 객체
    ```
        var Body: { 
            /* property : methods 의 구조 */
            setColor: function (color) {
                document.querySelector('body').style.color = color;
            },
            setBackgroundColor:function (color) {
                document.querySelector('body').style.backgroundColor = color;
            }
        }
    ```

### Library vs Framework
- Framework : 반쯤 완성된 제품 안에 들어가서 필요한 부분을 고치는 느낌 (뼈대라고 생각)
- Libaray : 내가 필요한 부품을 가져오는 느낌
    - jQuery 가 js의 대표적인 라이브러리
    - jQuery는 script 태그를 통해 가져오고, $를 함수명으로 사용함
        - $('a').css('color', color);  
            모든 a 태그의 'color'을 매개변수 color로 바꾼다는 의미

### UI vs API
- UI : User Interface  
        사용자가 시스템을 제어하기 위해서 사용하는 조작 장치 (button 등)
- API : Application Programming Interface  
        애플리케이션을 만들기 위해서 프로그래밍을 할 때 사용하는 조작 장치 (alert 등)
    - api 예시 (객체 검색)
        - document : 태그 활용
        - DOM : document 상위 객체
        - window : 웹브라우저 제어
        - ajax : 웹페이지 리로드 없이 정보 변경
        - cookie : 웹페이지가 리로드 되어도 현재 상태 유지
        - offline web application : 인터넷이 끊겨도 동작하는 웹페이지
        - webRTC : 화상 통신 웹
        - webGL : 3차원 그래픽으로 게임 등 제작
        - webVR : 웹 가상현실
        - speech : 사용자의 음성 인식, 음성 정보 전달
