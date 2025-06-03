import json
from datetime import datetime
from pathlib import Path
import sys

supported_languages = ["italian", "english", "german"]
#supported_languages = ["italian", "english", "german", "spanish"]

def is_found_in_verbs(id, verbs):
    for v in verbs:
        if v["id"] == id:
            return True
    return False

def search_ids_in_verbs(file_path: str, verb_ids: list):
    path = Path(file_path)
    if not path.exists():
        print(f"❌ File not found: {file_path}")
        return

    with open(path, encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON: {e}")
            return

    verbs = data["verbs"]
    not_found_verbs = [id for id in verb_ids if not is_found_in_verbs(id, verbs)]

    if not_found_verbs:
        for verb in not_found_verbs:
            print(f"❌ Verb with id '{verb}' not found in verbs.")
        print(f"❌ Found {len(not_found_verbs)} invalid verb(s).")
        return
    
    else:
        print(f"✅ All {len(verbs)} id(s) already in verbs.")

if __name__ == "__main__":
    spelling = ["abbrancare", "arrecare", "attaccare", "bloccare", "cercare", "eduxcare", "elencare", "giocare", "imbarcare", "imbucare", "impaccare", "impiccare", "leccare", "locare", "mancare", "raffrescare", "sbarcare", "seccare", "sporcare", "sprecare", "stancare", "toccare"]
    spelling2 = ["allegare", "collegare", "coniugare", "elongare", "fregare", "fugare", "impiegare", "legare", "litigare", "navigare", "negare", "pagare", "piegare", "pregare", "spiegare", "vagare"]
    spelling3 = ["cucire", "scucire", "ricucire"]
    doppio = ["piovere", "fallire", "suonare", "valere", "ardere", "cuocere", "penetrare", "seguire", "mutare", "sbarcare", "scendere", "finire", "nevicare", "passare", "consistere", "appartenere", "trascorrere", "dolere", "servire", "cominciare", "giungere", "discendere", "versare", "correre", "guarire", "ritornare", "vivere", "volare", "saltare", "crescere", "giacere", "migliorare", "salire", "mancare", "durare", "bruciare", "interessare", "iniziare", "terminare", "aumentare", "diminuire", "peggiorare", "sfumare", "affogare", "avanzare", "esplodere", "invecchiare", "schizzare"]
    verbs111 = ["abitare", "accendere", "addormentarsi", "aiutare", "amare", "andare", "annoiarsi", "aprire", "arrivare", "ascoltare", "aspettare", "avere", "baciare", "ballare", "bere", "cambiare", "camminare", "cantare", "capire", "cenare", "cercare", "chiamare", "chiedere", "chiudere", "cominciare", "comprare", "conoscere", "continuare", "correre", "costare", "credere", "cucinare", "cuocere", "dare", "dimenticare", "dire", "diventare", "divorziare", "domandare", "dormire", "dovere", "entrare", "esistere", "essere", "fare", "finire", "giocare", "guardare", "imparare", "interessare", "lasciare", "lavare", "lavorare", "leggere", "mandare", "mangiare", "mettere", "morire", "nascere", "nevicare", "nuotare", "organizzare", "pagare", "parlare", "partire", "pensare", "perdere", "piacere", "piovere", "portare", "potere", "pranzare", "preferire", "prendere", "provare", "regalare", "ricordare", "ridere", "rimanere", "ripetere", "rispondere", "ritornare", "salire", "salutare", "sapere", "scendere", "scrivere", "scusare", "sentire", "spegnere", "sperare", "sposare", "stare", "studiare", "suonare", "svegliarsi", "telefonare", "tornare", "trovare", "usare", "uscire", "vedere", "vendere", "venire", "vestirsi", "viaggiare", "vietare", "visitare", "vivere", "volare", "volere"]
    #verbs_ids = ["essere", "avere", "fare", "venire", "stare", "volere", "andare", "dire", "conoscere", "sapere", "vedere", "trovare", "dare", "pensare", "parlare", "mettere", "prendere", "portare", "arrivare", "chiedere", "credere", "lasciare", "sentire", "tenere", "diventare", "capire", "rimanere", "passare", "entrare", "lavorare", "vivere", "ricordare", "usare", "chiamare", "morire", "piacere", "guardare", "aprire", "seguire", "aspettare", "decidere", "scrivere", "finire", "mangiare", "bere", "leggere", "unire", "cambiare", "offrire", "giocare", "perdere", "provare", "costruire", "rispondere", "indicare", "succedere", "chiudere", "aiutare", "amare", "scegliere", "aggiungere", "mancare", "ricevere", "guidare", "dimostrare", "significare", "incontrare", "pagare", "crescere", "spiegare", "cadere", "colpire", "ascoltare", "fermare", "studiare", "controllare", "mandare", "correre", "girare", "ritornare", "invitare", "dimenticare", "vendere", "descrivere", "salvare", "scusare", "tirare", "attraversare", "imparare", "preferire", "bastare", "durare", "cercare", "suonare", "prestare", "ringraziare", "insegnare", "spingere", "costare", "cantare", "dormire", "sedere", "giudicare", "visitare", "spostare", "comprare", "ridere", "volare", "ferire", "indossare", "guadagnare", "rompere", "piangere", "disegnare", "viaggiare", "sorridere", "camminare", "rubare", "abbassare", "accendere", "pescare", "bruciare", "riempire", "mentire", "pulire", "fallire", "riposare", "fumare", "supporre", "prenotare", "coltivare", "lavare", "baciare", "allenare", "esplorare", "riparare", "parcheggiare", "cucinare", "gridare", "nuotare", "svuotare", "pianificare", "asciugare", "friggere", "arrostire", "migliorare", "sembrare", "accettare", "partire", "dispiacere", "iniziare", "permettere", "vincere", "piovere", "riconoscere", "produrre", "cominciare", "insistere", "esprimere", "tentare", "ripetere", "svegliare", "noleggiare", "sognare", "preoccupare", "spaventare", "odiare", "confondere", "sperare", "saltare", "appartenere", "concordare", "immaginare", "restare", "toccare", "ballare", "filmare", "dipingere", "fotografare", "ricercare", "inviare", "telefonare", "stampare", "nevicare", "affittare", "votare"]
    search_ids_in_verbs("coniugatto_verbs.json",  verbs111)