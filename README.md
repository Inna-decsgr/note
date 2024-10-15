# QuickNote

### 프로젝트 이름
quicknote

### 프로젝트 설명
`QuickNote`는 Vue.js와 Django를 사용하여 만든 간편한 메모 웹 어플리케이션이다. 사용자는 메모를 생성, 수정, 삭제할 수 있으며, 중요 메모는 잠금 기능을 통해 안전하게 관리할 수 있다. 

### 프로젝트 목표
QuickNote의 주요 목표는 사용자가 쉽고 안전하게 메모를 작성하고 관리할 수 있는 환경을 제공하는 것이다. 
1. **사용자 친화적인 인터페이스** : 직관적이고 간단한 UI를 통해 누구나 쉽게 메모를 작성하고 관리할 수 있도록 한다.
2. **효율적인 메모 관리** : CRUD 기능과 사용자 맞춤형 중요 메모 잠금 기능을 통해 중요한 정보를 안전하게 보호할 수 있다.
3. **신뢰성 있는 데이터 처리** : Django와 MySQL로 데이터 일관성을 유지하며 API를 통해 안정적인 메모 관리를 지원한다.
4. **확장 가능성** : 프론트엔드와 백엔드를 구조적으로 분리하여 향후 기능 추가나 개선 사항에 대해 쉽게 확잘할 수 있도록 설계되었다.

### 사용 기술
- **프론트엔드**
    - **Vue.js**: 사용자 인터페이스 구성
    - **Vue Router**: 라우팅 관리
    - **Axios**: HTTP 클라이언트
    - **Bootstrap**: UI 스타일링
- **백엔드**
    - **Django**: 웹 프레임워크
    - **Django REST Framework** : API 구축
    - **MySQL** : 데이터베이스

### 구현 사항
- **프론트엔드**
    - **메모 작성 및 수정/삭제** : 새로운 메모 생성, 기존 메모 수정 및 삭제
    - **메모 잠금 기능** : 사용자가 선택한 메모를 잠그거나 해제할 수 있는 기능을 제공해 보호가 필요한 정보는 안전하게 관리
    - **메모 목록 조회** : 모든 메모를 리스트로 확인하고 선택하여 상세 내용 확인 가능
- **백엔드**
    - **메모 CRUD API** : 메모 생성, 조회, 수정, 삭제 API 제공
    - **메모 잠금 처리** : 잠긴 메모에 대해 비밀번호 확인 후 접근하도록 API 구현
 


### 문제 해결
* **🟥 문제 1 : POST 요청 시 `ERR_CONNECTION_REFUSED` 발생**
  
🫁 **문제 내용**: Vue.js에서 Django로 POST 요청을 보냈을 때 서버가 요청을 거부하여 `ERR_CONNECTION_REFUSED` 에러가 발생.

🫁 **원인 분석**: 프론트엔드와 백엔드 서버가 로컬에서 서로 다른 포트에서 실행되면서 CORS(Cross-Origin Resource Sharing) 문제가 발생한 것을 확인. 기본적으로 브라우저는 다른 도메인, 프로토콜, 포트로의 요청을 차단함.

🫁 **해결 방법**:  
(1) **Django에서 CORS 허용**: `django-cors-headers` 패키지를 설치하고, 설정 파일에 CORS 허용 도메인 설정
```js
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True
```

(2) **프론트엔드에서 백엔드 URL 일치**: Vue.js의 Axios 설정에서 백엔드 서버의 정확한 URL과 포트를 명시해서 요청 주소를 올바르게 맞춤

🫁 **결과**: CORS 문제를 해결한 후 `python manage.py runserver`로 Django 서버를 실행하니 POST 요청이 정상적으로 백엔드로 전달되었고, 데이터 처리가 성공적으로 이루어짐.  
🫁 **결론** : CORS 문제는 여러 포트를 사용하는 개발 환경에서 빈번하게 발생하는 이슈임을 인지하고, 이를 처리하는 방법을 학습할 수 있었음. 개발 환경에서의 보안 정책에 대한 이해를 높이는 기회가 되었음.  
🫁 **블로그 참고**: https://velog.io/@kimina/Django-MySQL-%EA%B5%AC%ED%98%84%ED%95%9C-%EA%B0%84%EB%8B%A8-%EB%A9%94%EB%AA%A8%EC%9E%A5-3-%EB%A9%94%EB%AA%A8-%EC%A0%80%EC%9E%A5-%EB%B0%8F-%EB%B6%88%EB%9F%AC%EC%98%A4%EA%B8%B0-MySQL%EC%9D%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EA%B0%84%EB%8B%A8%ED%95%9C-%EA%B5%AC%ED%98%84

**🟥문제 2: 403 Forbidden 오류 발생 (CSRF Token 문제)**  

🫁 **문제 내용**:  Vue.js에서 Django로 데이터를 전송할 때, 403 Forbidden 오류가 발생하며 서버에서 CSRF(Cross-Site Request Forgery) 토큰이 없다는 경고가 표시됨  

🫁 **원인 분석**: Django는 CSRF 보호를 기본적으로 활성화하고 있어서 POST 요청 시 CSRF 토큰이 포함되지 않으면 요청을 거부함. Vue.js는 기본적으로 CSRF 토큰을 자동으로 처리하지 않으므로 이 문제가 발생.  

🫁 **해결 방법**:  
(1) **CSRF Token 설정**: Django에서 CSRF 토큰을 프론트엔드로 전달할 수 있도록  HTML 내에서 CSRF 토큰을 포함시키고, Axios를 통해 요청 시 이 토큰을 헤더에 포함시킴.
- **CSRF Token을 위한 meta 태그 추가**
```js
<meta name="csrf-token" content="{{ csrf_token }}">
<script>
    const csrftoken = document.querySelector('meta[name="csrf-token"]').content;
    document.cookie = "csrftoken=" + csrftoken;
</script>
```
- **Axios에서 POST 요청 시 CSRF 토큰을 포함하도록 설정**
```js
headers: {
    'X-CSRFToken': this.csrfToken,
}
```
(2) **Django CORS 설정 수정**: CORS 정책을 수정해서 프론트엔드에서 오는 요청 허용함.
```js
axios.defaults.withCredentials = true;
```
🫁 **결과**: CSRF 토큰을 헤더에 포함해서 더 이상 403 Forbidden 오류 없이 데이터 전송이 가능하게 됨.  
🫁 **결론**: CSRF 보호는 웹 어플리케이션의 보안에서 매우 중요한 부분임을 알게 되었음. Django의 보안 기능을 활용하는 방법을 배울 수 있었고, CSRF 원리를 이해할 수 있는 기회가 되었음.  
🫁 **블로그 참고** : [https://velog.io/@kimina/%EC%98%81%ED%99%94-%EB%A6%AC%EB%B7%B0-%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%986-Vuex%EB%A1%9C-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%83%81%ED%83%9C-%EA%B4%80%EB%A6%AC-%EB%B0%8F-%EC%83%81%ED%83%9C-%EC%9C%A0%EC%A7%80%ED%95%98%EA%B8%B0](https://velog.io/@kimina/Django-MySQL-%EA%B5%AC%ED%98%84%ED%95%9C-%EA%B0%84%EB%8B%A8-%EB%A9%94%EB%AA%A8%EC%9E%A5-5-%EB%A9%94%EB%AA%A8-%EC%A6%90%EA%B2%A8%EC%B0%BE%EA%B8%B0-%EB%A9%94%EB%AA%A8%EB%B3%84-%EC%9E%A0%EA%B8%88-%EA%B8%B0%EB%8A%A5-MySQL%EC%9D%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EA%B0%84%EB%8B%A8%ED%95%9C-%EA%B5%AC%ED%98%84)


### 사용 방법
1. **Backend 의존성 설치 및 마이그레이션**
```js
python manage.py migrate
```
2. **개발 서버 실행**
   - **Frontend**
   ```bash
   npm run serve
   ```
   - **Backend**
   ```bash
   python manage.py runserver
   ```
3. **MySQL 서버 설정**: 로컬에서 MySQL 서버가 실행 중이어야 하며, `settings.py` 파일에서 MySQL 데이터베이스 설정을 맞춰주세요.
