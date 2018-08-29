from __future__ import division

import cv2
import numpy as np
import track
import detect
import time
from grabscreen import grab_screen

ticks = 0
road_horizon=320
lt = track.LaneTracker()
vertices = np.array([[0, 256], [0, 220], [220, 150], [292, 150], [512, 200], [512, 256]], np.int32)
ld = detect.LaneDetector(vertices,road_horizon) #horizon line y coordinate
with open("Output.txt", "w") as text_file:
    while True:
            begin=time.time()
            precTick = ticks
            ticks = cv2.getTickCount()
            dt = (ticks - precTick) / cv2.getTickFrequency()

            frame = np.array(grab_screen(region=(10, 40, 810, 640)))
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            #frame = cv2.imread('C:/Users/shun.yang/Desktop/lane_detect/track/test.png')
            #frame = cv2.imread('C:/Users/shun.yang/Desktop/lane_detect/lane_alex/img/1.png')
            predicted = lt.predict(dt)

            lanes = ld.detect(frame)

            if predicted is not None:
                cv2.line(frame, (predicted[0][0], predicted[0][1]), (predicted[0][2], predicted[0][3]), (0, 0, 255), 5)
                cv2.line(frame, (predicted[1][0], predicted[1][1]), (predicted[1][2], predicted[1][3]), (0, 0, 255), 5)
                text_file.write(str(((predicted[0][0]+predicted[1][2])/2-400)/400*1.5)+' \n')

            elif lanes.count(predicted) == 0:
                cv2.line(frame, (int(lanes[0][0]), int(lanes[0][1])), (int(lanes[0][2]), int(lanes[0][3])), (0, 0, 255), 5)
                cv2.line(frame, (int(lanes[1][0]), int(lanes[1][1])), (int(lanes[1][2]), int(lanes[1][3])), (0, 0, 255), 5)

            lt.update(lanes)

            cv2.putText(frame, str(round(1/(time.time()-begin+0.01),2))+' FPS', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))

            cv2.resizeWindow("lane", 800, 600)
            cv2.imshow('lane', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
