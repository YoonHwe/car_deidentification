# car_deidentification
 지능형 CCTV를 위한 딥러닝 기반 자동차 번호판 비식별화 연구

This paper identifies whether a vehicle exists by receiving image or photo data. Using deep learning techniques, it shows how likely a specific object is a vehicle and what type of vehicle it is. When the vehicle is recognized, the vehicle area is displayed by displaying a box on the corresponding data. Vehicle license plate de-identification is performed by blurring the lower part of the displayed area.

총 세 가지의 비식별화 방식
1) video_blur.ipynb
Blurring 기법을 이용한 자동차 번호판 비식별화
결과: https://youtu.be/fFyahjTxhS0
2) video_color.ipynb
Line 기법을 통한 색 입히기를 이용한 자동차 번호판 비식별화
3) video_mosaic.ipynb
확대/축소 기법을 통한 Mosaic를 이용한 자동차 번호판 비식별화
