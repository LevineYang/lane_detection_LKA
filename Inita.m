% clc;clear;
addpath C:/torcs-1.3.7/src/drivers/TORCSLink
fuzzy=readfis('fuzzy.fis');
ticks=0;
commandStr = 'python C:\Users\shun.yang\Desktop\lane_detect\track\TORCS_detect.py 2';
dt=0.01;
road_horizon=320;
vertices = [[0, 256], [0, 220], [220, 150], [292, 150], [512, 200], [512, 256]];
% global lt
% global ld
lt = py.track.LaneTracker();
ld = py.detect.LaneDetector(vertices,road_horizon);
tic
%system(commandStr)
% 
% net_weights = 'E:/caffe-master/examples/DeepLearningExample_VGG/data/Alex4SW/Alex_SW_iter_1630.caffemodel';
% net_model = 'E:/caffe-master/examples/DeepLearningExample_VGG/data/Alex4SW/deploy1.prototxt';

% net_weights = 'E:/caffe-master/examples/DeepLearningExample5/R_iter_5000.caffemodel';
% net_model = 'E:/caffe-master/examples/DeepLearningExample5/deploy1.prototxt';

% net_weights = 'E:/caffe-master/examples\DeepLearningExample_VGG/data/viktor/R2/R2_iter_5217.caffemodel';
% net_model = 'E:/caffe-master/examples/DeepLearningExample5/deploy1.prototxt';
% caffe.set_mode_gpu()
% net = caffe.Net(net_model, net_weights, 'test');