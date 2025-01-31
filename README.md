# Moda Backend

### 설정

```.env```파일 생성 후
```
KAKAO_CLIENT_ID=your_kakao_client_id_key
KAKAO_CLIENT_SECRET_ID=your_kakao_client_secret_id_key
```

### API 예시

### 기본 요청
```
GET /api/v1/...
Authorization: Bearer YOUR_JWT_TOKEN
```

#### Curation

```
GET /api/v1/curation?limit=10
** limit은 기본값이 10, 없어도 호출 가능

[
  {
    "id": 1,
    "title": "힙스러운 코디",
    "seasons": [
      "봄",
      "가을"
    ],
    "colors": [
      "베이지",
      "올리브"
    ],
    "products": [
      {
        "name": "헤어리 그래픽 로고 오버핏 자카드 니트 (BLUE)",
        "brand": "트릴리온",
        "price": "36900",
        "image_url": "https://image.msscdn.net/images/goods_img/20240814/4328686/4328686_17249552459456_500.jpg"
      },
      {
        "name": "베이직 청바지 3 Color [ULZD_0001]",
        "brand": "유라이프지",
        "price": "31400",
        "image_url": "https://image.msscdn.net/images/goods_img/20241025/4557442/4557442_17298165185522_500.jpg"
      },
      {
        "name": "프렌치 울 트위드 블레이저",
        "brand": "수아레",
        "price": "109900",
        "image_url": "https://image.msscdn.net/images/goods_img/20240829/4384039/4384039_17258778553515_500.jpg"
      },
      {
        "name": "푸마 클럽 2 에라 - 블랙:화이트 / 397447-02",
        "brand": "푸마",
        "price": "58990",
        "image_url": "https://image.msscdn.net/images/goods_img/20240709/4240657/4240657_17217005570257_500.jpg"
      },
      {
        "name": "R EYE 192 베타 티타늄 안경 [4color]",
        "brand": "로우로우",
        "price": "169000",
        "image_url": "https://image.msscdn.net/images/goods_img/20241022/4543177/4543177_17295737498693_500.jpg"
      },
      {
        "name": "트위스터 스타 스트라이프 비니 - 블루/라이트블루",
        "brand": "웹하우스",
        "price": "20300",
        "image_url": "https://image.msscdn.net/images/goods_img/20241013/4511248/4511248_17350157028050_500.jpg"
      }
    ],
    "likes": 0,
    "created_at": "2025-01-31T06:05:03.614003+00:00"
  }
]
```

### 크롤링 예시

#### 무신사

무신사 랭킹 상의, 하의를 크롤링한다

```
python manage.py crawl_products_from_musinsa
```