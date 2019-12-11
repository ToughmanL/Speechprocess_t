
clear;
clc;
root_dir='E:\Data\original\44.1_16_downsample\';
new_dir='E:\Data\original\Filterphone\Boll3\';
file_floder=fullfile(root_dir);
dir_output=dir(fullfile(file_floder,'*.wav'));
len=length(dir_output);

for nu =1:len
    oldfile=sprintf('%s%s',root_dir,dir_output(nu).name);
    newfile=sprintf('%s%s',new_dir,dir_output(nu).name);
    
    amp = 1.8;    %turn it up loudER
    [data, fs] = audioread(oldfile);
    newdata = data*amp;
    newdata = max( min(newdata, 1), -1 );   %clip when it gets too loud
    %wfdata=WienerScalart96(newdata,fs,0.05);%ά���˲�
    %0.1 eer 0.038
    sfdata=SSBoll79(newdata,fs,0.12);
    Hd = Filterphone;%�����˲���ģ��绰�ŵ�
    fpdata=filter(Hd,sfdata);
    audiowrite(newfile, fpdata, fs);
end
