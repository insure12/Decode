
import os


logo="""ʀᴜᴘ ᴀᴅʜɪᴋᴀʀʏ(ᴅᴇᴄᴏᴅᴇʀ)"""

def main():
    os.system("clear")
    print(logo)
    print("[A] Decode Zlib \n[B] Decode Base64\n\n")
    choice=input("[✓] input:")
    dec()

def dec():
    os.system("clear")
    print(logo)
    print(" Example RLG.py")
    file=input(" input file: ")
    ogge=str(open(file,"r").read())
    data=ogge.replace("exec","rup=")
    data2=f"""{data}\nopen(\"dec_done.py\",\"w").write(rup.decode(\'utf-8\')) """
    open(".dara.py","w").write(data2)
    os.system("python .dara.py")
    print(" file saved with dec_done.py")
    print(" Dec done [✓] ")
    

main()























