# Tello 드론 프로젝트 설정 가이드

## 1. 환경 설정

### 필수 요구사항
- Python 3.x
- 가상환경 (venv)
- Tello 드론

### 설치해야 할 패키지
```txt
djitellopy>=2.5.0
openai>=0.27.0
SpeechRecognition>=3.8.1
PyAudio>=0.2.11
```

### 설정 단계

1. **가상환경 생성 및 활성화**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

2. **필수 패키지 설치**
```bash
pip install -r requirements.txt
```

## 2. Tello 드론 연결

### 연결 준비
1. Tello 드론의 전원을 켭니다
2. 컴퓨터의 WiFi 설정에서 Tello 드론의 네트워크에 연결
   - SSID: 'TELLO-XXXXXX' 형식
   - 기본 비밀번호 없음

### 연결 테스트 코드
```python
from djitellopy import Tello
import time

# Tello 드론 객체 생성
tello = Tello()

try:
    # 드론에 연결
    tello.connect()
    
    # 배터리 잔량 확인
    battery = tello.get_battery()
    print(f"배터리 잔량: {battery}%")
    
    # 온도 확인
    temp = tello.get_temperature()
    print(f"드론 온도: {temp}°C")
    
except Exception as e:
    print(f"에러 발생: {str(e)}")
finally:
    # 연결 종료
    tello.end()
```

## 3. 연결 확인사항

드론 연결 전 다음 사항들을 확인하세요:
1. Tello 드론의 전원이 켜져 있는지 확인
2. 컴퓨터가 Tello 드론의 WiFi 네트워크에 연결되어 있는지 확인
3. 드론의 배터리가 충분한지 확인

## 4. 문제 해결

연결 실패 시 다음 사항들을 확인하세요:
1. WiFi 연결 상태 확인
2. 드론의 전원 상태 확인
3. 드론과의 거리가 너무 멀지 않은지 확인
4. 다른 WiFi 네트워크의 간섭 여부 확인 

# Cursor에서 "@" 문서 및 파일등을 참고하도록 인공지능에게 지시할 수 있는 기능을 제공