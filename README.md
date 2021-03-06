KAPTCHA : 한국인들'만' 사용 가능한 튜링 테스트
=========
개요
---------

1. KAPTCHA란 무엇인가?
2. 작동 방식이 무엇인가?
3. 사용 용도는 어떻게 되는가?
4. 앞으로의 발전 방향은?
5. 필요한 패키지

***

## 1. KAPTCHA란 무엇인가?
기존에 있던 CAPTCHA(Completely Automated Public Turing test to tell Computers and Humans Apart)를 한국버전으로 만든</br>
KAPTCHA(Korean completely Automated Public Turing test to tell Computers and Humans Apart) 입니다.</br>

***

## 2. 작동 방식이 무엇인가?
쉽습니다! 다음 문장을 읽어보세요!</br>
<code>어니가머 촌동생과사 다는웃</code></br>
네, 맞습니다. 자연스럽게 <code>어머니가 사촌동생과 웃는다</code>로 읽게 되죠?</br>
이렇게 한글 순서를 무작위로 섞어도, 한국인들은 알아본다는 한글의 특징을 사용한 CAPTCHA입니다.</br>

그리고 다른 예시를 한번 볼까요?</br>
<code>동쌩이 화짱품을 빠른따</code></br>
이 문장 역시 읽게 되면 <code>동생이 화장품을 바른다</code>로 읽게 되죠?</br>
맞습니다! 일반 자음을 쌍자음으로 바꿔도, 한국인들은 언제나 알아본다는 한글의 특징도 사용한 CAPTCHA입니다.</br>

***

## 3. 사용 용도는 어떻게 되는가?
~아니 이걸 쓴다고요?~</br>
사용 용도는 다음과 같습니다!</br>
1. 한국인들'만' 인증시키고 싶을 때!
2. 색다른 신개념 CAPTCHA를 도입하고 싶을 때!
3. 안티캡차(Ex. 2captcha)를 무력화 시키고 싶을 때!

***

## 4. 앞으로의 발전 방향은?
일단 계획은 크게 새웠는데</br>
언제 업데이트 되고, 어떻게 수정될지, 또 정식지원을 할지는 모르겠습니다만...</br>
일단 계획은 다음과 같습니다!</br>

> 1. Python에서 기본적인 프로그래밍</br>
(문자 섞기나 이외 부분)
> 2. Python에서 단어를 불러오기</br>
(표준국어대사전 API를 사용한다던가...)
> 3. Python에서 문법에 맞게 일부 수정하기</br>
(아니 <code>어머니을 동생가 먹는다</code>나 <code>컴퓨터을 동생이 짝사랑한다</code> 등이 나오면 안되잖아요?)
~(근데 문법에 맞게는 못고칠것 같습니다... 예... 어차피 단어를 기준으로 잘라서 나오니, 읽는데는 문제가 없습니다 ㅎㅎ)~
> 4. 시간제한이나 최종 확인등 프로그래밍 마무리 하기
> 5. 서버를 이용해서 API 형태로 재공하기</br>
(만약 하게 되면 아마존 서버를 사용할 것 같습니다 ~(아마존 사랑해요)~ )

***

## 5. 필요한 패키지
"한글"을 Python으로 다루려고 하니, 많이 어려웠습니다...</br>
"한글"을 Python에서 다루는 기능까지 구현하려니 너무 힘들어서....</br>
"한글"을 다루는 Python 패키지를 가져왔습니다.</br>
따라서 필요한 패키지는 다음과 같습니다.

"Simple Toolkit for Hangul" - (hgtk)</br>
(출처 : https://github.com/bluedisk/hangul-toolkit)</br>
</br>

### INSTALL
<code>pip install hgtk</code></br>
<code>pip install six</code> - hgtk 패키지를 사용하기 위해서 필요합니다.</br>

***

언제 소리 없이 업로드돼서, 바람같이 완성되어 있을 수도 있으니,</br>
자주 오지 마시고 가끔!! 아---주 가끔 오셔서 확인해 주세요</br>
~(요즘 너무 바빠서... 아마도 이 프로젝트가 생존신고가 될 것 같습니다...)~</br>

</br></br> Made By K.S.H(김세현)
