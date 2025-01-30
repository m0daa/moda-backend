# Moda Backend

### 설정

```.env```파일 생성 후
```
KAKAO_CLIENT_ID=your_kakao_client_id_key
KAKAO_CLIENT_SECRET_ID=your_kakao_client_secret_id_key
```

### API 예시

#### Curation

```
GET /api/v1/curation?limit=10
** limit은 기본값이 10, 없어도 호출 가능

[
  {
    "id": 1,
    "title": "캐주얼룩",
    "seasons": [
      "봄",
      "여름",
      "가을",
      "겨울"
    ],
    "colors": [
      "블루",
      "그레이"
    ],
    "products": [
      {
        "name": "맨투맨",
        "price": "50000.00",
        "image_url": "https://naver.com"
      },
      {
        "name": "청바지",
        "price": "70000.00",
        "image_url": "https://naver.com"
      }
    ],
    "likes": 0,
    "created_at": "2025-01-30T06:51:28.329660+00:00"
  }
]
```