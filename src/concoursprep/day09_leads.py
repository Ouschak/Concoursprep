from pprint import pprint
import requests
from bs4 import BeautifulSoup
import logging


def parse_position_count(raw: str | None) -> int | None:
    if raw is None:
        return None
    if raw.strip() == "":
        raise ValueError("string number of positions is empty")

    if len(raw.split()) != 2 or raw.split()[1].lower() not in ("postes", "poste"):
        logging.error("Number of postes need to be checked")
        raise ValueError("Number of postes need to be checked")

    number = int(raw.split()[0])
    if number < 0:
        raise ValueError("Number of positions cannot be negative")

    return number


logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(levelname)s--%(message)s--%(asctime)s",
)

concours = []

try:
    request = requests.get("https://www.emploi-public.ma/fr/concours-liste", timeout=10)

    logging.info("status code: %s", request.status_code)

    request.raise_for_status()

    response = BeautifulSoup(request.content, "html.parser")

    cards = response.select("#listing-switcher > div.row > div.s-item > a")

    if cards is None or len(cards) == 0:
        logging.error("NO LINK IS SELECT, PLEASE CHECK SELECTOR FOR LINK")
        raise SystemExit(1)

    for i, card in enumerate(cards):
        concour = {}

        try:
            concour["title"] = card.select_one("div.card-body > h2").text

        except AttributeError:
            logging.error("Selector error -- TITLE -- %d", i + 1)
            continue

        try:
            concour["ministre"] = card.select_one("div.card-text").text

        except AttributeError:
            logging.error("Selector error -- ministre --")
            concour["ministre"] = None

        try:
            concour["nombre_poste"] = card.select_one("div.card-footer > div").text

            concour["nombre_poste_INT"] = parse_position_count(concour["nombre_poste"])

        except AttributeError:
            logging.error("Selector error -- nombre_poste --")
            concour["nombre_poste"] = None
            concour["nombre_poste_INT"] = None

        except ValueError:
            concour["nombre_poste_INT"] = None
            logging.error("Number of positions isnt INT")

        try:
            concour["href"] = "https://www.emploi-public.ma" + card["href"]

        except (AttributeError, KeyError) as e:
            logging.exception("Selector error -- link -- %s", e)
            continue

        concours.append(concour)


except requests.exceptions.RequestException as e:
    logging.exception("Request failed %s", e)
    raise SystemExit(1)

pprint(concours)