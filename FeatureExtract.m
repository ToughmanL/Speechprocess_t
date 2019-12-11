
rootpath='E:\Data\other\far\near_enroll_near_verify\verify\13003977084\';
filename='13003977084_near_verify_1';
filewav=sprintf('%s%s.wav',rootpath,filename);
[audioIn,fs] = audioread(filewav);
win = hann(1024,"periodic");
[coeffs,delta,deltaDelta,loc] = mfcc(audioIn,fs,"LogEnergy","Ignore");
nbins = 60;
len=size(coeffs,2);
for i = 1:len
    figure('Visible','off');
    histogram(coeffs(:,i),nbins,"Normalization","pdf")
    title(sprintf("%sCoefficient %d",filename,i))
    figurepath=sprintf("%s%sCoefficient%d",rootpath,filename,i);
    saveas(gcf,figurepath,'png');
end

