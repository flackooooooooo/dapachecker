import requests
import re
import os,sys,time
import json
from multiprocessing.dummy import Pool
from bs4 import BeautifulSoup
from time import time as timer

def checking(don):
    done = don.rstrip()
    #print(done)
    data = {
    'links[]': done,
    'url': '1',
    'domain': '0'
    }
    try:
        ten = requests.post("https://www.softo.org/ajax/dacheck", data = data)
        tenx = ten.content
        if '[]' in tenx:
            print("[!] Tidak Valid")
        else:
            da = re.findall('"domain_auth": (.*?),', tenx)
            pa = re.findall('"page_auth": (.*?),', tenx)
            ss = re.findall('"spam_score": (.*?),', tenx)
            tb = re.findall('"total_links": (.*?),', tenx)
            mr = re.findall('"m_rank": (.*?),', tenx)
            hasil = "[!] "+str(done)+"    | DA: "+str(da[0])+" | PA: "+str(pa[0])+" | MR: "+str(mr[0])+" | SS: "+str(ss[0])+"% | TB: "+str(tb[0])+" |"
            print(hasil)
            with open('ResultDaPa.txt', 'a') as o:
                o.writelines(hasil + '\n')
            pass
    except:
        pass
            
def Main():
        try:
            print("\n\t | DA PA Checker by flacka | ")
            print("\n\t\t Github : https://github.com/flackooooooooo")
            dom = raw_input("\n\nInput List Domain \t: ")
            thread = raw_input("Threads (Input 1) \t: ")
            print("\n\n")
            doms = open(dom, 'r').read().splitlines()
            pool = Pool(int(thread))
            results = pool.map(checking, doms)
        except:
            pass
        
if __name__ == '__main__':
	Main()
