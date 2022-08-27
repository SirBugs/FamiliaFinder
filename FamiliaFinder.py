import requests, time, os, sys, re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from multiprocessing.pool import ThreadPool
from colorama import Fore, Back, Style
from datetime import datetime

banner = """
\t ______              _ _ _      ______ _           _           
\t |  ___|            (_) (_)     |  ___(_)         | |          
\t | |_ __ _ _ __ ___  _| |_  __ _| |_   _ _ __   __| | ___ _ __ 
\t |  _/ _` | '_ ` _ \| | | |/ _` |  _| | | '_ \ / _` |/ _ \ '__|
\t | || (_| | | | | | | | | | (_| | |   | | | | | (_| |  __/ |   
\t \_| \__,_|_| |_| |_|_|_|_|\__,_\_|   |_|_| |_|\__,_|\___|_|   
\t                                              V 1.0.7
\t                                              Familia V2
"""
print(Fore.MAGENTA + banner)

Subdomains = []
Done = 0
Sets = 0

def CheckDomainSubsMap(sub):
    global SavingSwitch, LimiterSwitch, SelectedDomain, AfterT, AfterL, AfterS, Done, Subdomains, sets
    try:
        req = requests.get("https://" + sub + "." + SelectedDomain, timeout=5, verify=False)
        if req.status_code == 200:
            print(Fore.GREEN + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Done)) + sub + "." + SelectedDomain)
        elif req.status_code == 301 or req.status_code == 302:
            print(Fore.WHITE + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Done)) + sub + "." + SelectedDomain)
        elif req.status_code == 400 or req.status_code == 401:
            print(Fore.CYAN + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Done)) + sub + "." + SelectedDomain)
        elif req.status_code == 403 or req.status_code == 404:
            print(Fore.RED + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Done)) + sub + "." + SelectedDomain)
        elif req.status_code == 405 or req.status_code == 406:
            print(Fore.BLUE + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Done)) + sub + "." + SelectedDomain)
        else:
            print(Fore.MAGENTA + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Done)) + sub + "." + SelectedDomain)
        if SavingSwitch == "ON":
            if sub+"."+SelectedDomain in Subdomains:
                pass
            else:
                Subdomains.append(sub+"."+SelectedDomain)
                file = open(AfterS+".txt", "a+")
                file.write(str(req.status_code) + ": " + sub + "." + SelectedDomain + "\n")
                file.close()
        Done+1
    except:
        #print "BAD: " + "https://" + sub + "." + SelectedDomain
        #print(Fore.RED + "\tBAD ({}) : ".format(str(Done)) + Fore.WHITE + sub + "." + SelectedDomain)
        pass
        Done+=1

def CheckDomainCRTSH(domain):
    global SavingSwitch, LimiterSwitch, SelectedDomain, AfterT, AfterL, AfterS, Done, Subdomains, Sets
    src = requests.get("https://crt.sh/?q=%25.{}".format(domain), verify=False).content
    #src = open("content.txt", "r").read()
    PayloadImports = re.findall("[a-z0-9]*.[a-z0-9]*.[a-z0-9]*.[a-z0-9]*.[a-z0-9]*.[a-z0-9]*.[a-z0-9]*.[a-z0-9]*.{}".format(domain), src)
    for i in PayloadImports:
        i = i.replace("<TD>", ""); i = i.replace("<TD>", ""); i = i.replace("<TD", ""); i = i.replace("<T", ""); i = i.replace("Ecrt.sh|%.", "")
        i = i.replace("TD>", ""); i = i.replace("Ecrt.sh | %", ""); i = i.replace('href="atom?q=', ""); i = i.replace("Ecrt.sh|%.", "")
        i = i.replace("<BR>", ""); i = i.replace(" A ", ""); i = i.replace("<BR", ""); i = i.replace('font-size:8pt" href="?q=', "")
        i = i.replace("BR>", ""); i = i.replace("  ", ""); i = i.replace("R>", ""); i = i.replace("&nbsp;&nbsp;Search: '", ""); i = i.replace("Ecrt.sh|%", "")
        i = i.replace("D>", ""); i = i.replace(' A href="?q=', ""); i = i.replace(">", ""); i = i.replace('nbsp;A href="?q=', "")
        i = i.replace("<", ""); i = i.replace('A href="?q=', ""); i = i.replace("   ", ""); i = i.replace("  ", ""); i = i.replace(" ", "")
        if i in Subdomains:
            pass
        else:
            if "@" in i:
                pass
            else:
                try:
                    req = requests.get("https://" + i, timeout=5, verify=False)
                    if req.status_code == 200:
                        print(Fore.GREEN + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Sets)) + i)
                    elif req.status_code == 301 or req.status_code == 302:
                        print(Fore.WHITE + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Sets)) + i)
                    elif req.status_code == 400 or req.status_code == 401:
                        print(Fore.CYAN + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Sets)) + i)
                    elif req.status_code == 403 or req.status_code == 404:
                        print(Fore.RED + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Sets)) + i)
                    elif req.status_code == 405 or req.status_code == 406:
                        print(Fore.BLUE + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Sets)) + i)
                    else:
                        print(Fore.MAGENTA + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + str(req.status_code) + " ({}) : ".format(str(Sets)) + i)
                    if SavingSwitch == "ON":
                        file = open(AfterS+".txt", "a+")
                        file.write(str(req.status_code) + ": " + i + "\n")
                        file.close()
                    Subdomains.append(i)
                    Sets+=1
                except Exception as e:
                    #print str(e) + "    " + i
                    print(Fore.RED + "\t[{}] ".format(datetime.now().strftime("%H:%M:%S")) + "FAIL" + " ({}) : ".format(str(Sets)) + i)
                    Subdomains.append(i)
                    Sets+=1
                    if SavingSwitch == "ON":
                        file = open(AfterS+".txt", "a+")
                        file.write("FAIL: " + i + "\n")
                        file.close()
                    pass

subdomains = requests.get("https://noisyyy.xyz/subs.doms.xmap.txt", verify=False).content.split("\n")
Args = len(sys.argv)

options = ['-h', '-s', '-l', '-t']
inst = """
\t -s
\t    This switch would be followed by the .txt file name you wanna save in
\t -l
\t    This switch is selecting limit of the subs have to be checked
\t -h
\t    This switch is only submitted one
\t -t
\t    This switch is cotrolling the threads number (Suggested=50)
\t *
\t    All switches are written in SMALL letters normally
\t *
\t    This tool list is getting updated day by day, adding more stuff, options, subs, etc..
\t *
\t    For more info aboue HTTP STATUS CODES, Visit: https://github.com/SirBugs/FamiliaSubFinder/StatusCodes.txt
"""

SavingSwitch = "OFF"
LimiterSwitch = "OFF"
SuggestedThreads = 50

BashLine = ""
for arg in sys.argv:
    if ".py" in arg: pass
    else: BashLine = BashLine + arg + " "

if Args == 1 or "-h" in BashLine:
    print inst
    quit()
if Args == 2 and "-h" not in BashLine:
    pass
if Args >= 2:
    SelectedTool = sys.argv[1]
    SelectedDomain = sys.argv[2]
    if "-s" in BashLine:
        AfterS = BashLine.split("-s ")[1]
        try:
            AfterS = AfterS.split(" ")
            AfterS = AfterS[0]
        except:
                pass
        SavingSwitch = "ON"
    if "-l" in BashLine:
        AfterL = BashLine.split("-l ")[1]
        try:
            AfterL = AfterL.split(" ")
            AfterL = AfterL[0]
        except:
            pass
        LimiterSwitch = "ON"
    if "-t" in BashLine:
        AfterT = BashLine.split("-t ")[1]
        try:
            AfterT = AfterT.split(" ")
            AfterT = AfterT[0]
        except:
            pass
        SuggestedThreads = int(AfterT)
    CheckDomainSubsMap(SelectedDomain)
    # // Checking Function
    if SelectedTool == "SUB":
        try:
            if __name__ == '__main__':
                pool = ThreadPool(SuggestedThreads)
                print(Fore.YELLOW + "\tCurrent InUse Tool: " + Fore.CYAN + SelectedTool + "\n")
                print(Fore.YELLOW + "\tSubdomains List Current Size: " + Fore.CYAN + str(len(subdomains)) + "\n")
                print(Fore.YELLOW + "\tMethod: "  + Fore.CYAN + "GET" + "\n")
                print(Fore.YELLOW + "\tThreads: " + Fore.CYAN + str(SuggestedThreads) + "\n")
                print(Fore.YELLOW + "\tTarget: "  + Fore.CYAN + SelectedDomain + "\n")
                print(Fore.MAGENTA + "\t[{}] STARTING BRUTE!\n".format(datetime.now().strftime("%H:%M:%S")))
                ree = requests.get("https://noisyyy.xyz/subs.doms.xmap.txt", verify=False).content.split("\n")
                for _ in pool.imap_unordered(CheckDomainSubsMap, ree):
                    if LimiterSwitch == "ON" and Done == int(AfterL):
                        #print str(Done) + " Limiter: " + LimiterSwitch
                        print(Fore.GREEN + str(Done) + " Limiter: " + LimiterSwitch)
                        quit()
                    pass
                print(Fore.MAGENTA + "\n\t[{}] STARTING CRT.SH Search!\n".format(datetime.now().strftime("%H:%M:%S")))
                CheckDomainCRTSH(SelectedDomain)
        except:
            pass
    elif SelectedTool == "DIR":
        print "Dir Tools Starting!"
    else:
        print "Not A Tool To Use!"
