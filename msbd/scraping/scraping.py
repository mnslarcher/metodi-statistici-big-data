from bs4 import BeautifulSoup
import argparse
import multiprocessing as mp
import os
import pickle
import requests
import time
import threading


def ottieni_contenuto_url(url, coda=None):
    id_processo = os.getpid()
    nome_processo = mp.current_process().name
    nome_thread = threading.current_thread().name
    
    print("[INIZIO]\nURL: {}\nID processo: {}\nNome processo: {}\nNome thread:"
        "{}\n".format(url, id_processo, nome_processo, nome_thread))

    try:
        risposta = requests.get(url)
        testo = BeautifulSoup(risposta.content, "lxml").get_text()
    except requests.exceptions.HTTPError as err:
        print("HTTP Error:", err)
    except requests.exceptions.ConnectionError as err:
        print("Connection Error:", err)
    except requests.exceptions.Timeout as err:
        print("Timeout Error:", err)
    except requests.exceptions.RequestException as err:
        print("Request Error",err)
        
    print("[FINE]\nURL: {}\nID processo: {}\nNome processo: {}\nNome thread:"
        "{}\n".format(url, id_processo, nome_processo, nome_thread))
    
    if coda is not None:
        coda.put(testo)
    else:
        return testo


def ottieni_contenuto_urls_multithread(urls, file):
    # ============== YOUR CODE HERE ==============
    raise NotImplementedError
    # ============================================


def ottieni_contenuto_urls_multiprocess(urls, file):
    coda = mp.Queue()
    
    processi = [mp.Process(target=ottieni_contenuto_url, args=(url, coda)) 
        for url in urls]
    
    for p in processi:
        p.start()

    contenuti = [coda.get() for p in processi]
    
    for p in processi:
        p.join()

    with open(file, 'wb') as f:
        pickle.dump(contenuti, f)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", help="file .txt contenente gli url di cui si "
        "vuole salvare il contenuto")
    parser.add_argument("--tipo", 
        help="uno tra sequenziale, multithread, multiprocess")
    parser.add_argument("--output", 
        help="file .pkl dove salvare i contenuti")
    args = parser.parse_args()

    with open(args.urls) as f:
        urls = f.read().split("\n")

    inizio = time.time()

    if args.tipo == "sequenziale":
        ottieni_contenuto_urls_sequenziale(urls, args.output)
    elif args.tipo == "multithread":
        ottieni_contenuto_urls_multithread(urls, args.output)
    elif args.tipo == "multiprocess":
        ottieni_contenuto_urls_multiprocess(urls, args.output)
    else:
        raise ValueError("{} non è un tipo valido.".format(args.tipo))

    fine = time.time()
    print("Durata: {:.2f}s".format(fine - inizio))
