import os
import subprocess
import time

def yt_down( InURL, OutDir):
	commd = "/usr/local/bin/yt-dlp/yt-dlp -f 'bv*[height<=720][ext=mp4]+ba' -P " + OutDir + " " + InURL
	#subprocess.Popen(["yt-dlp", "-f", "'bv*[height<=720][ext=mp4]+ba'", "-P", OutDir, InURL ],encoding="utf-8", shell=True, stdout=subprocess.PIPE)
	subprocess.run([commd ],encoding="utf-8", shell=True, stdout=subprocess.PIPE)
	print(f"Downloading is complite!")
	print("")
	print("")

def con_mp3(InURL, OutDir):
#    yt_down( InURL, OutDir)
    k = subprocess.check_output([f"find {OutDir} -type f -iname '*.mp4'"], shell=True,  encoding="utf=8")
#    k = subprocess.check_output(["find", OutDir, "-type", "f", "-iname", "*.mp4"], encoding="utf-8")
    l = k.split("\n")
#    print("l", l)
    f=[]
    ff=[]
    for tmp in l: f.append(os.path.basename(tmp))
    for tmp in f: ff.append(os.path.splitext(tmp)[0])
    print(l)
    print(f)
    print(ff)
    for pr in l[:-1]: print(pr)
    for pr in range(len(l)-1): 
        lastpath = f"{OutDir}/{ff[pr]}.mp3"
        sw = subprocess.run(["ffmpeg", "-y", "-i", l[pr], "-ab", "320k", lastpath])
        print(sw)
#    for pr in range(len(l)-1): os.system(f"ffmpeg -y -i '{l[pr]}' -ab 320k '{OutDir}/{ff[pr]}'.mp3");


#    await con_mp3(InURL, OutDir)

def main():
    default =os.getcwd()
    print("default: ",default)
    InURL = input ("URL: ")
    UserDir = input ("OutDir: ")
    if UserDir =="" :
        OutDir=default
    else:
        OutDir=UserDir
    print(f"Link: {InURL}  Directory: {OutDir}")
    yt_down(InURL, OutDir)
#    time.sleep(5)
    con_mp3(InURL, OutDir)

main()
