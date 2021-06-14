import cv2
import time
import numpy as np
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
p = GPIO.PWM(4, 50)

def main():

capture = cv2.VideoCapture(1)

    while True:

         ret, frame = capture.read()
         
        if ret is False:
            print("cannot read image")
            continue

        # 位置を抽出
        pos = find_specific_color(
            frame,
            AREA_RATIO_THRESHOLD,
            LOW_COLOR,
            HIGH_COLOR
        )

        if pos is not None:
            # 抽出した座標に丸を描く
            cv2.circle(frame,pos,10,(0,0,255),-1)
        
        # 画面に表示する
        cv2.imshow('frame',frame)

        # キーボード入力待ち
        key = cv2.waitKey(1) & 0xFF

        # qが押された場合は終了する
        if key == ord('q'):
            break

    cv2.destroyAllWindows()