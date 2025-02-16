# 베이스 이미지 설정
FROM python:3.13-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 업데이트 및 Poetry 설치
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Poetry 설치
RUN curl -sSL https://install.python-poetry.org | python3 -

# PATH에 Poetry 추가
ENV PATH="/root/.local/bin:${PATH}"

# Poetry 가상 환경 비활성화 (컨테이너에서 실행하기 쉽게 만듦)
RUN poetry config virtualenvs.create false

# pyproject.toml과 poetry.lock 파일 복사
COPY pyproject.toml poetry.lock ./

# 의존성 설치
RUN poetry install --no-root --no-dev

# 프로젝트 소스 코드 복사
COPY . .

# Uvicorn을 사용해 ASGI 서버 실행
CMD ["uvicorn", "app.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
