# 1. 기본 이미지
FROM python:3.14.0-slim

# 2. 작업디렉토리 지정
WORKDIR /app

# 3. requirements.txt 복사
COPY requirements.txt .

# 4. requirements.txt 설치 명령 진행
RUN pip install -r requirements.txt

# 5. 원본소스(main.py) 복사
# COPY . . <- 통상 이 방식 더 많이 사용, .dockerignore 작성을 통해 필터링함
COPY main.py . 

# 6. 서버가동 => 도커 컴포즈로 이관, 여기서는 생략
# CMD ["uvicorn", "main:app", "--reload"]