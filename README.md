# Fin

Fin은 주식 종목 리스트와 주식 정보를 불러오는 Python 패키지입니다. 본 패키지는 pykrx, bs4, click, aiohttp, tqdm 등의 의존성을 사용하며, Python 3.8 이상에서 작동하도록 설계되었습니다. 설치 방법

Fin 패키지를 설치하려면, 아래의 pip 명령어를 사용하세요:

~~~bash
pip install fin
~~~
사용법

Fin 패키지는 다음의 스크립트 명령어를 제공합니다:

```
tickers: 주식 종목 리스트를 불러옵니다.
get_stockinfo_list: 주식 정보 리스트를 불러옵니다.
```

주식 종목 리스트 불러오기

주식 종목 리스트를 불러오려면, 다음 명령어를 실행하세요:

~~~bash
fin tickers
~~~
주식 정보 리스트 불러오기

특정 조건에 맞는 주식 정보 리스트를 불러오려면, 다음 명령어를 실행하세요:

~~~bash
fin get_stockinfo_list
~~~
개발자 정보

```
이름: David Cho
이메일: csi00700@gmail.com
```

기여하기

본 프로젝트에 기여하고 싶으신 분들은 깃허브를 통해 Pull Request를 보내거나, 이슈를 등록해 주세요. 라이선스

본 프로젝트는 MIT 라이선스 하에 제공됩니다.
