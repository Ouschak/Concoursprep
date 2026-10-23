
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import logging


logging.basicConfig(filename="app.log",level=logging.DEBUG,format="%(levelname)s--%(message)s--%(asctime)s")

concours = []
try:
    request = requests.get("https://www.emploi-public.ma/fr/concours-liste",timeout=10)

    logging.info("status code: %s",request.status_code)

    request.raise_for_status()

    response = BeautifulSoup(request.content,"html.parser")

    cards = response.select("#listing-switcher > div.row > div.s-item > a")
    
    if cards is None or len(cards)==0 :
        logging.error("NO LINK IS SELECT, PLEASE CHECK SELECTOR FOR LINK")
        raise SystemExit(1)


    for i,card in enumerate(cards):
        concour ={}
        try :
            concour["title"] = card.select_one("div.card-body > h2").text

        except AttributeError:
            logging.error("Selector error -- TITLE -- %d",i+1)
            continue

        try:
            concour["ministre"] = card.select_one("div.card-text").text
        except AttributeError:
                    logging.error("Selector error -- ministre --")
                    concour["ministre"] = None
        try:
            concour["nombre_poste"] = card.select_one("div.card-footer > div").text
        except AttributeError:
                    logging.error("Selector error -- nombre_poste --")
                    concour["nombre_poste"] =None
        try:
            concour["href"] = "https://www.emploi-public.ma" + card["href"]
        except (AttributeError,KeyError) as e:
                    logging.exception("Selector error -- link -- %s",e)
                    continue

        concours.append(concour)


except requests.exceptions.RequestException as e :
    logging.exception("Request failed %s",e)
    raise SystemExit(1)

pprint(concours)

