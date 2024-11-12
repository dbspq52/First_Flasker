# Fashion MNIST Image Classification



## 설치 및 실행 방법

### 1. 가상 환경 생성 및 활성화 (선택 사항)

가상 환경을 사용하여 의존성 충돌을 방지할 수 있습니다.

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

### 2. 의존성 설치

requirements.txt 파일에 정의된 라이브러리를 설치합니다. <br>

pip install -r requirements.txt<br>

### 3. 모델 파일 다운로드 및 설정
학습된 모델 가중치 파일인 F_mnist_model.pth가 필요합니다. 이 파일을 models/ 디렉토리에 추가해야 합니다. <br>

참고: 모델 파일이 없는 경우, 프로젝트와 함께 제공된 학습된 모델 파일을 다운로드하여 models/ 폴더에 넣어주세요.

## 실행 방법

### 1. Flask 서버 실행

Flask 서버를 실행하여 API 서버를 시작합니다. <br>
python app.py

## 주요 파일 설명
app.py: Flask 서버를 실행하고, 예측 요청을 처리하는 API를 제공합니다. <br>
models/F_mnist_model.pth: 학습된 CNN 모델 가중치 파일로, 모델이 Fashion MNIST 데이터셋을 통해 학습된 결과입니다. <br>
modules/model.py: CNN 모델 구조 및 예측 함수가 정의된 모듈입니다. <br>
requirements.txt: 프로젝트에 필요한 라이브러리와 버전이 명시된 파일입니다. <br>

## 참고 사항
requirements.txt 파일에 명시된 버전을 설치하여 환경을 동일하게 유지하면 재현성을 높일 수 있습니다. <br>
학습된 모델이 없는 경우 학습된 모델 파일을 별도로 다운로드하여 models/ 디렉토리에 넣어주세요. <br>
서버 실행 시 http://localhost:5000/predict 엔드포인트로 이미지를 POST 요청으로 전송하여 예측을 수행할 수 있습니다. <br>
이 README 파일은 프로젝트를 설치하고 실행하는 방법을 자세히 설명하여, 새로운 사용자도 쉽게 프로젝트를 실행해볼 수 있도록 돕습니다. <br>






