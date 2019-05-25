from bs4 import BeautifulSoup
import argparse
import multiprocessing as mp
import os
import pickle
import requests
import time
import threading


def ottieni_contenuto_url(url, coda=None, verboso=True):
    id_processo = os.getpid()
    nome_processo = mp.current_process().name
    nome_thread = threading.current_thread().name

    if verboso:
        print("[INIZIO]\nURL: {}\nID processo: {}\nNome processo: {}\nNome"
        "thread: {}\n".format(url, id_processo, nome_processo, nome_thread))

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
        print("Request Error", err)

    if verboso:
        print("[FINE]\nURL: {}\nID processo: {}\nNome processo: {}\nNome"
        "thread: {}\n".format(url, id_processo, nome_processo, nome_thread))

    if coda is None:
        return testo
    else:
        coda.put(testo)


def ottieni_contenuto_urls_sequenziale(urls, verboso=True):
    # ============== YOUR CODE HERE ==============
    raise NotImplementedError
    # ============================================

    return contenuti


def ottieni_contenuto_urls_threading(urls, verboso=True):
    coda = mp.Queue()

    threads = [threading.Thread(target=ottieni_contenuto_url, args=(url,),
        kwargs={"coda": coda, "verboso": verboso}) for url in urls]

    for t in threads:
        t.start()

    contenuti = [coda.get() for t in threads]

    for t in threads:
        t.join() # blocca il MainThread finché t non è completato

    return contenuti


def ottieni_contenuto_urls_multiprocessing(urls, verboso=True):
    # ============== YOUR CODE HERE ==============
    raise NotImplementedError
    # ============================================

    return contenuti
