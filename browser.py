##coded by blackkitty


import socket
import argparse
def browser(target,path,port=80):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    t=target.split('/')[2]
    
    client.connect((t,port))
    url=f"GET {path} HTTP/1.1\r\nHost: {t}\n\n".encode()
    
    client.send(url)
    while True:
        data=client.recv(1024)
        if len(data.decode()) < 1:
            
            print('______________end or response___________________')
            break
        print('\n'+data.decode())
    client.close()

if __name__=="__main__":
    parse=argparse.ArgumentParser(description="python simple browser")
    parse.add_argument('--target','-t',type=str,help='target url')
    parse.add_argument('--path','-p',type=str,help='url path')
    var=parse.parse_args()
   
    browser(var.target,var.path)

