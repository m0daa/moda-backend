# Python 공식 이미지를 기반으로 합니다.
FROM python:3.13-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 업데이트 및 Poetry 설치
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Poetry 설치
RUN curl -sSL https://install.python-poetry.org | python3 -

# PATH에 Poetry 추가
ENV PATH="/root/.local/bin:${PATH}"

# pyproject.toml과 poetry.lock 파일 복사
COPY pyproject.toml poetry.lock ./

# 의존성 설치
RUN poetry install --no-root

# 프로젝트 소스 코드 복사
COPY . .

# 애플리케이션 실행 명령어
CMD ["poetry", "run", "gunicorn", "moda_backend.wsgi:application", "--bind", "0.0.0.0:8000"]