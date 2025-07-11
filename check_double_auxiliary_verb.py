import json
from pathlib import Path

def is_found_in_verbs(id, verbs):
    for v in verbs:
        if v["id"] == id:
            return True
    return False

def is_double_auxiliary_verb(verb):
         try:
             # Auxiliaries
             assert isinstance(verb["auxiliaries"], list), "auxiliaries"
             assert set(verb["auxiliaries"]) == {"avere", "essere"}, "not a double auxiliary verb"
             return True
         except Exception as e:
             return False

def search_double_auxiliaries_in_verbs(file_path: str, verb_ids: list):
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
    found_verbs = [id for id in verb_ids if is_found_in_verbs(id, verbs)]

    if len(found_verbs) == len(verb_ids):
        print(f"✅ All {len(found_verbs)} id(s) already in verbs.")
    elif found_verbs:
        print(f"✅ The following verbs are in verbs: {json.dumps(found_verbs)}")

    double_auxiliary_verbs = [verb["id"] for verb in verbs if is_double_auxiliary_verb(verb)]

    print(f"🍒 {len(double_auxiliary_verbs)} total double auxiliary verbs found!")

    if double_auxiliary_verbs:
        print(f"Here they are: {json.dumps(double_auxiliary_verbs)}")

    if verb_ids:
        not_found_verbs = [id for id in verb_ids if id not in double_auxiliary_verbs]
        if not_found_verbs:
            print(f"❌ The following verbs are not double auxiliary verbs: {', '.join(not_found_verbs)}")
        else:
            print("✅ All specified verbs are double auxiliary verbs.")

if __name__ == "__main__":
    verbs_500 = ["piovere", "fallire", "suonare", "valere", "ardere", "cuocere", "penetrare", "seguire", "mutare", "sbarcare", "scendere", "finire", "nevicare", "passare", "consistere", "appartenere", "trascorrere", "dolere", "servire", "cominciare", "giungere", "discendere", "versare", "correre", "guarire", "ritornare", "vivere", "volare", "saltare", "crescere", "giacere", "migliorare", "salire", "mancare", "durare", "bruciare", "interessare", "iniziare", "terminare", "aumentare", "diminuire", "peggiorare", "sfumare", "affogare", "avanzare", "esplodere", "invecchiare", "schizzare"]
    verbs = ["aumentare", "cambiare", "cominciare", "crescere", "cuocere", "diminuire", "durare", "finire", "guarire", "iniziare", "migliorare", "passare", "peggiorare", "suonare", "terminare", "volare", "fiorire", "grandinare", "nevicare", "piovere", "scivolare", "vivere"]
    more_verbs = ["A",  "abbondare",  "abortire",  "accestire",  "accomodare",  "allegare",  "allignare",  "appartenere",  "appetire",  "approdare",  "arrossire",  "ascendere",  "assonare",  "avanzare",  "B",  "balenare",  "balzare",  "balzellare",  "brillare",  "bruciare",  "brulicare",  "C",  "calzare",  "campare",  "cessare",  "cestire",  "circolare",  "colare",  "cominciare",  "comparire",  "concorrere",  "confluire",  "consistere",  "continuare",  "convenire",  "convivere",  "correre",  "cuocere",  "D",  "degenerare",  "difettare",  "diluviare",  "diradare",  "discendere",  "disconvenire",  "disertare",  "dolere",  "dovere",  "durare",  "E",  "echeggiare",  "emigrare",  "equivalere",  "erbeggiare",  "esistere",  "espatriare",  "esplodere",  "esulare",  "evaporare",  "fallire",  "fiammeggiare",  "finire",  "fioccare",  "fiorire",  "folgorare",  "folgoreggiare",  "formicolare",  "frizzare",  "frullare",  "fulminare",  "fumare",  "G",  "garbare",  "gelare",  "gemere",  "germinare",  "germogliare",  "giovare",  "girare",  "gocciolare",  "gradire",  "gravare",  "gravitare",  "grondare",  "guizzare",  "gustare",  "I",  "impaludare",  "impazzare",  "imporrare",  "imporrire",  "importare",  "impuntare",  "incagliare",  "incespicare",  "inciampare",  "inciampicare",  "incominciare",  "incrudelire",  "indietreggiare",  "infellonire",  "inferocire",  "infierire",  "infiscalire",  "infrondire",  "ingemmare",  "ingrullire",  "insolentire",  "intoppare",  "invaiare",  "invaiolare",  "L",  "lampeggiare",  "luccicare",  "lustrare",  "M",  "mancare",  "migrare",  "mondare",  "muovere",  "mutare",  "N",  "naufragare",  "nevicare",  "P",  "perdurare",  "pesare",  "piovere",  "pioviscolare",  "potere",  "premere",  "prevalere",  "principiare",  "procedere",  "progredire",  "proseguire",  "pullulare",  "quadrare",  "R",  "rabbrividire",  "raccapricciare",  "raddoppiare",  "radiare",  "raggiare",  "ragnare",  "rampicare",  "recedere",  "refluire",  "regredire",  "retrocedere",  "ribaltare",  "ribalzare",  "ricorrere",  "ridondare",  "rifiorire",  "rifluire",  "rifolgorare",  "rifulgere",  "rigermogliare",  "rigirare",  "rigurgitare",  "rimbalzare",  "rimbombare",  "rimontare",  "rimpatriare",  "rinfronzire",  "rintoccare",  "rintronare",  "riparare",  "ripullulare",  "risaltare",  "risonare",  "risplendere",  "ritardare",  "rivivere",  "rombare",  "ronzare",  "ruzzolare",  "S",  "salire",  "salpare",  "saltare",  "sbavare",  "sbiecare",  "sbiettare",  "sbigonciare",  "sbolgiare",  "sbollire",  "scarseggiare",  "scattare",  "scendere",  "schiassolare",  "sciamare",  "scivolare",  "scomparire",  "sconfinare",  "scrosciare",  "sdrucciolare",  "servire",  "sfavillare",  "sfiatare",  "sfigurare",  "sfilare",  "sfogare",  "sfolgorare",  "sfollare",  "sfondare",  "sgelare",  "sgocciolare",  "sguizzare",  "slittare",  "soccorrere",  "somigliare",  "sonare",  "sovrabbondare",  "sovvenire",  "spatriare",  "spesseggiare",  "spigare",  "spillare",  "spirare",  "spiritare",  "spruzzare",  "squillare",  "stillare",  "strabalzare",  "straboccare",  "strapiombare",  "straripare",  "sudare",  "suppurare",  "sussistere",  "svampare",  "svariare",  "svicolare",  "sviluppare",  "tallire",  "tardare",  "tinnire",  "tintinnare",  "tintinnire",  "tonare",  "trabaltare",  "traboccare",  "tralignare",  "traripare",  "trasalire",  "trascendere",  "trascorrere",  "trasecolare",  "trasmigrare",  "traspirare",  "trasudare",  "V",  "vaiare",  "vaiolare",  "valere",  "vaporare",  "variare",  "vivere",  "volare",  "volgere",  "Z",  "zampillare"]
    not_so_more_verbs = ["cominciare", "continuare", "correre", "cuocere", "dolere", "dovere", "durare", "finire", "girare", "mancare", "muovere", "nevicare", "piovere", "potere", "riparare", "salire", "saltare", "scendere", "servire", "valere", "vivere", "volare"]
    search_double_auxiliaries_in_verbs("coniugatto_verbs.json", verbs_500)