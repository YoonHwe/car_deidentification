import os
import cv2
import argparse
import cvlib as cv
from cvlib.object_detection import draw_bbox

import numpy as np
import imutils

parser = argparse.ArgumentParser() #parser 생성

parser.add_argument("--input", type=str, dest="input") #input으로 받고 싶은 명령행 옵션 지정
parser.add_argument("--output", type=str, dest="output") #output으로 받고 싶은 명령행 옵션 지정
args = parser.parse_args() #input과 output을 가진 객체 반환

input_name = args.input  #input 파일 이름은 input의 객체
output_name = args.output #output 파일 이름은 output의 객체

# input_name = "/Users/heoyoonhwe/Desktop/test.avi" #input 파일 이름은 input의 객체
# output_name = "/Users/heoyoonhwe/Desktop/test3.avi" #output 파일 이름은 output의 객체

cap = cv2.VideoCapture(input_name) #input 파일을 VideoCapture 타입의 객체로 받아 생성
fourcc = cv2.VideoWriter_fourcc(*'mp4v') #
out = cv2.VideoWriter(output_name, fourcc, 30.0, (1920,1080)) #기록할 동영상의 파일명은 output_name, 프레임률(30), 영상 크기(1920,1080)으로 지정
idx = 0 #index number
l = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) #총 프레임 수

while(cap.isOpened()): #비디오를 끝날 때까지 프레임별로 캡처
    if idx % 100 == 0:
        print(idx,"/",l) #index show
    
    status, frame = cap.read() #재생되는 input 파일을 한 프레임씩 읽는다. status은 프레임을 제대로 읽었는지에 대한 boolean 값, frame은 저장되는 내용

    if (status):  #프레임을 제대로 읽었다면
        idx += 1 #idx에 1 더함
        bbox, label, conf = cv.detect_common_objects(frame) #객체 탐지 수행(bbox는 탐지한 부분, label은 물체를 탐지한 라벨, conf는 label로 인식된 확률)
        for i, cla in enumerate(label):
            if cla == 'car' or cla == 'bus' or cla == 'truck': #탐지된 라벨이 car, bus, truck인 경우
                blur_h = int((bbox[i][3] - bbox[i][1]) * 1/3) #비식별화 처리(blurring)할 영역 설정
                if bbox[i][0] > 0 and bbox[i][1] > 0:
                    blur_area = frame[bbox[i][3] - blur_h:bbox[i][3] + int(blur_h/3), bbox[i][0]:bbox[i][2]]
                    blur_img = cv2.blur(blur_area, (7,7)) #blurring 수행
                    frame[bbox[i][3] - blur_h:bbox[i][3] + int(blur_h/3), bbox[i][0]:bbox[i][2]] = blur_img #output 영상에 해당 img 담기
        # draw bounding box over detected objects
        frame = draw_bbox(frame, bbox, label, conf, write_conf = True)

        # display output
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL) #새로운 윈도우 창(frame)을 띄워 내용 넣기 
        cv2.resizeWindow('frame', 1100, 1500) #프레임 창을 (1100, 1500)로 재설정
        cv2.imshow("frame", frame) #프레임을 화면에 디스플레이
        out.write(frame)  #output 영상에 프레임을 저장
        if cv2.waitKey(0) & 0xFF == ord('q'): #영상이 종료되거나 q가 입력되면
            break #종료
    else: #프레임을 제대로 읽지 못했다면
        break #종료
       
out.release() #output과 관련한 동작 종료
cap.release() #input 영상 사용 종료
cv2.destroyAllWindows() #윈도우 창 닫기