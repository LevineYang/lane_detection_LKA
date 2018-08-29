function [y] = LaneCal2()
y = [0];
ld = evalin('base', 'ld');
lt = evalin('base', 'lt');
    
frame=py.PIL.ImageGrab.grab([10,40,810,640]);
frame = py.numpy.array(frame);


dt=toc;
predicted = lt.predict(dt);
lanes = ld.detect(frame);

try
    predicted=py.numpy.asarray(predicted);
    data = double(py.array.array('f',py.numpy.nditer(predicted))); %d is for double, see link below on types
    data = reshape(data,[4 2])'; %Could incorporate x.shape here ...
catch
    data=zeros(2,4);
end

lt.update(lanes)
tic


y=((data(1,1)+data(2, 3))/2-400)/400*1.5-3.3;
