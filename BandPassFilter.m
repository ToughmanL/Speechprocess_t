
clear;
clc;
root_dir='E:\Data\original\44.1_16_downsample\';
new_dir='E:\Data\original\audition_phone\';
file_floder=fullfile(root_dir);
dir_output=dir(fullfile(file_floder,'*.wav'));
len=length(dir_output);

for nu =1:len
    oldfile=sprintf('%s%s',root_dir,dir_output(nu).name);
    newfile=sprintf('%s%s',new_dir,dir_output(nu).name);
   
    amp = 8;    %turn it up loudER
    [data, fs] = audioread(oldfile);
    new_data = data*amp;
    new_data = max( min(new_data, 1), -1 );   %clip when it gets too loud
    %audiowrite(newfile, new_data, fs);
    %[out_data,d]=bandpass(new_data,[500 3500],fs,'ImpulseResponse','iir','Steepness',[0.5 0.6]);
    Bandpass_phone=load('Bandpass_phone.mat');
    dataFiltered=filter(Bandpass_phone.Num,1,new_data);
    audiowrite(newfile, dataFiltered, fs);
end








