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