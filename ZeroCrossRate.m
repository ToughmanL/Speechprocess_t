

%������
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

%��ʱ����
function stn=ShortTimeEnergy(X,fn)
    stn=zero(1,fn);
    for i=1 : fn
        u=X(:,i);              % ȡ��һ֡
        u2=u.*u;               % �������
        stn(i)=sum(u2);         % ��һ֡�ۼ����
    end
end


%��ʱ����غ���,���Ǿ��
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


%��ʱƽ�����Ȳ�
function staad=ShortTermAverageAmplitudeDifference(X,fn)
    staad=zero(1,fn);
    for i=1 : fn
        u=X(:,i);              % ȡ��һ֡
        for k = 1:wlen
        staad(k) = sum(abs(u(k:end)-u(1:end-k+1)));%��ÿ������ķ��Ȳ����ۼ�
        end
    end
end

%����ͼ
function d=FrequencyCal(x,nw,ni)
    n=nw;                                        %֡��
    h=ni;                                        %֡����
    s0=length(x);
    win=hamming(n)';                             %�Ӵ�,hammingΪ��
    c=1;
    ncols=1+fix((s0-n)/h);                       %��֡��������֡��
    d=zeros((1+n/2),ncols);
    for b=0:h:(s0-n)
        u=win.*x((b+1):(b+n));
        t=fft(u);
        d(:,c)=t(1:(1+n/2))';
        c=c+1;
    end
end

%��������ͼ����
% [signal,fsc] = wavread('tone4.wav');
% nw=512;ni=nw/4;
% d=FrequencyCal(signal',nw,ni);
% tt=[0:ni:(length(signal)-nw)]/fsc;
% ff=[0:(nw/2)]*fsc/nw*2;
% % imagesc(tt,ff,20*log10(abs(d)));
% imagesc(tt,ff,abs(d).^2);
% xlabel('Time(s)');
% ylabel('Frequency(Hz)')
% title('����ͼ')
% axis xy

%���ö�����
% imagesc(tt,ff,20*log10(abs(d)));
%imagesc(tt,ff,20*log10(C+abs(d)));%��ӳ���
% imagesc(tt,ff,abs(d).^2);




