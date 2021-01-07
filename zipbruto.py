import zipfile
from tqdm import tqdm
import os

def banner():
    os.system('cls||clear')
    print("""_  _ ____ _  _ ___ ____ ____ ____ _ ___ 
|\/| |__|  \/   |  |___ |__/ |  | |  |  
|  | |  | _/\_  |  |___ |  \ |__| |  |""")
    print("==================================================")
    print("ZIP File Password Bruteforcer")
    print("==================================================")
    print(" Github   : https://github.com/maxteroit)")
    print(" Website  : https://maxteroit.com)")
    print("==================================================")

def get_info():
    banner()
    filename = input("Your zip file [ex: file.zip] : ")
    wordlist = input("Your wordlist [ex: rockyou.txt] : ")
    brute(filename,wordlist)

def brute(filename,wordlist):
    isFound = False
    try:
        with open(wordlist,"r") as word:
            for line in tqdm(word):
                try:
                    password = line.strip()
                    with zipfile.ZipFile(filename) as file:
                        file.setpassword(password.encode('ascii'))
                        file.extractall()
                        print("==================================================")
                        print(f'Password found !! The password is >>>> [{password}]')
                        print("========== Success Extract Zip File !! ===========")
                        print("==================================================")
                        isFound = True
                        break
                except NotImplementedError:
                    print("\nFile compression method is not supported yet.")
                    break
                except zipfile.BadZipFile:
                    print("\nBad zip file.")
                    break
                except RuntimeError:
                    pass
    except Exception as e:
        print(f"An error occured.\n{e}")
    if isFound == False:
        print("==================================================")
        print("=============== Password Not Found ===============")
        print("======= Failed to Extract the Zip File !! ========")
        print("==================================================")
    print("Finished..!")
get_info()
