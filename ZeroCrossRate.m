

%过零率
function zcr=ZeroCrossRate(X,fn)
    zcr=zero(1,fn);
    for i=1:fn
        z=X(:,i);
        for j=1:(wlen-1)
            if z(j)*z(j+1)<0
                zcr(i)=zcr(i)+1;
            end
        end
    end
end

%短时能量
function stn=ShortTimeEnergy(X,fn)
    stn=zero(1,fn);
    for i=1 : fn
        u=X(:,i);              % 取出一帧
        u2=u.*u;               % 求出能量
        stn(i)=sum(u2);         % 对一帧累加求和
    end
end


%短时自相关函数,就是卷积
function output_signal=Convolution(input_signal,impulse_response)
    % Input:
    %    input_signal: the input signal
    %    impulse_response: the impulse response
    % Output:
    %    output_signal:the convolution result
    N=length(input_signal);%define length of signal
    K=length(impulse_response);%define length of impulse response
    output_signal=zeros(N+K-1,1);%initializing the output vector
    xp=[zeros(K-1,1);input_signal;zeros(K-1,1)];
    for i=1:N+K-1
        output_signal(i)=xp(i+K-1:-1:i)'*impulse_response;
    end
end


%短时平均幅度差
function staad=ShortTermAverageAmplitudeDifference(X,fn)
    staad=zero(1,fn);
    for i=1 : fn
        u=X(:,i);              % 取出一帧
        for k = 1:wlen
        staad(k) = sum(abs(u(k:end)-u(1:end-k+1)));%求每个样点的幅度差再累加
        end
    end
end

%语谱图
function d=FrequencyCal(x,nw,ni)
    n=nw;                                        %帧长
    h=ni;                                        %帧移量
    s0=length(x);
    win=hamming(n)';                             %加窗,hamming为例
    c=1;
    ncols=1+fix((s0-n)/h);                       %分帧，并计算帧数
    d=zeros((1+n/2),ncols);
    for b=0:h:(s0-n)
        u=win.*x((b+1):(b+n));
        t=fft(u);
        d(:,c)=t(1:(1+n/2))';
        c=c+1;
    end
end

%调用语谱图函数
% [signal,fsc] = wavread('tone4.wav');
% nw=512;ni=nw/4;
% d=FrequencyCal(signal',nw,ni);
% tt=[0:ni:(length(signal)-nw)]/fsc;
% ff=[0:(nw/2)]*fsc/nw*2;
% % imagesc(tt,ff,20*log10(abs(d)));
% imagesc(tt,ff,abs(d).^2);
% xlabel('Time(s)');
% ylabel('Frequency(Hz)')
% title('语谱图')
% axis xy

%常用对数谱
% imagesc(tt,ff,20*log10(abs(d)));
%imagesc(tt,ff,20*log10(C+abs(d)));%添加常数
% imagesc(tt,ff,abs(d).^2);




