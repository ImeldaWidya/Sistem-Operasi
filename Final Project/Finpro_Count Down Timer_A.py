import time 

def run(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 10)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 2

    print("Istirahat")

def push(time_secs):
    while time_secs:
        mins, secs = divmod(time_secs, 10)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_secs -= 1

    print("Next")

def sit(time_secs):
    while time_secs:
        mins, secs = divmod(time_secs, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_secs -= 1

    print("Next")
    
def back(time_secs):
    while time_secs:
        mins, secs = divmod(time_secs, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_secs -= 1
        
    print("Finish")
    
print ("============================================")
print (" Program dibuat oleh : Imelda Widya Ningrum ")
print (" NPM   : 21083010052 ")
print (" Prodi : Sains Data ")
print ("============================================")

print     ("************************")
print     (" COUNTDOWN TIMER SPORT  ")
print     ("************************")

print("|---------------------------------|")
print("|        Pilihan Olahraga         |")
print("|---------------------------------|")
print("|     1. Lari    (120 Detik)      |")
print("|     2. Push Up (30 Detik )      |")
print("|     3. Sit Up  (20 Detik )      |")
print("|     4. Back Up (10 Detik )      |")
print("|---------------------------------|")

x=input("Pilih Olahraga : ")

if x == "1":
    run(10)
elif x == "2":
    push(10)
elif x == "3":
    sit(60)
elif x == "4" :
    back(30)
else:
    print("Perintah Tidak Ditemukan")


print ("********************************************************")
print ("Tetap Semangat! Sehat Pikiran Berawal Dari Sehat Jasmani")
print ("********************************************************")
