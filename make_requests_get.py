import requests

def download(filename):
    print(filename)
    url = 'http://119.3.37.112:9090/download'
    param = {'filepath': filename}
    r = requests.get(url, params=param, stream=True)
    f = open('1.wav','w')
    
    return 0

if __name__=='__main__':
    filename = '/DATA/kuaishang/uploads//1550546969.2570128_17_8000/c1.wav'
    download(filename)