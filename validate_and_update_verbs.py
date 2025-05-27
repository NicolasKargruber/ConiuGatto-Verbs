import json
from datetime import datetime
from pathlib import Path
import sys

supported_languages = ["italian", "english", "german"]
#supported_languages = ["italian", "english", "german", "spanish"]

def is_valid_verb_structure(verb):
    try:
        # Infinitive
        assert isinstance(verb["id"], str), "id"
        assert isinstance(verb["infinitive"], dict), "infinitive"
        assert all(lang in verb["infinitive"] for lang in supported_languages), "infinitive"
        # Regularity
        assert isinstance(verb["regularity"], str), "regularity"
        # Irregularities
        assert isinstance(verb["irregularities"], list), "irregularities"
        allowed_irregularities = ["spelling change", "stem change", "past participle", "present gerund", "using -isc-"]
        assert all(item in allowed_irregularities for item in verb["irregularities"]), "irregularities"
        # Auxiliaries
        assert isinstance(verb["auxiliaries"], list), "auxiliaries"
        assert all(item in ["avere", "essere"] for item in verb["auxiliaries"]), "auxiliaries"
        # Conjugations
        assert isinstance(verb["conjugations"], dict), "conjugations"
        validate_conjugations_structure(verb["conjugations"])
        # Past Participle
        assert isinstance(verb["participio_passato"], dict), "participio_passato"
        assert all(lang in verb["participio_passato"] for lang in supported_languages), "participio_passato"
        # Gerundio
        assert isinstance(verb["gerundio_presente"], dict), "gerundio_presente"
        assert all(lang in verb["gerundio_presente"] for lang in supported_languages), "gerundio_presente"
        return True
    except Exception as e:
        print("Verb: " + verb["infinitive"]["italian"])
        print(f"Assertion failed: {e}")
        return False
    
def validate_conjugations_structure(conjugations):
    conjugation_structure = {
        "indicativo": [
            "presente",
            "imperfetto",
            "passato_remoto",
            "futuro_semplice"
        ],
        "congiuntivo": [
            "presente",
            "imperfetto"
        ],
        "condizionale": [
            "presente"
        ],
        "imperativo": [
            "positivo"
        ]
    }
    pronouns = ["io", "tu", "lui/lei", "noi", "voi", "loro"]

    assert isinstance(conjugations, dict), "conjugations must be a dictionary"
    assert set(conjugations.keys()) == set(conjugation_structure.keys()), f"moods mismatch: found {list(conjugations.keys())}"

    for mood, tenses in conjugation_structure.items():
        assert mood in conjugations, f"missing mood: {mood}"
        assert set(conjugations[mood].keys()) == set(tenses), f"{mood} tenses mismatch: found {list(conjugations[mood].keys())}"
        for tense in tenses:
            entries = conjugations[mood][tense]
            if entries:  # only check structure if tense is not empty
                assert isinstance(entries, dict), f"{mood} -> {tense} should be a dictionary"
                assert set(entries.keys()) == set(pronouns), f"{mood} -> {tense} pronouns mismatch"
                for pronoun, forms in entries.items():
                    if forms is not None:
                        assert isinstance(forms, dict), f"{mood} -> {tense} -> {pronoun} should be a dictionary"
                        assert all(lang in forms for lang in supported_languages), f"{mood} -> {tense} -> {pronoun} missing translations"


def is_valid_meta(meta):
    try:
        assert isinstance(meta["version"], (float, int))
        assert isinstance(meta["last_updated"], str)
        assert isinstance(meta["min_app_version"], str)
        assert isinstance(meta["languages"], list)
        return True
    except (AssertionError, KeyError):
        return False

def validate_and_update(file_path: str):
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

    if "meta" not in data or "verbs" not in data:
        print("❌ Missing required top-level keys: 'meta' and 'verbs'")
        return

    if not is_valid_meta(data["meta"]):
        print("❌ Invalid meta format.")
        return

    verbs = data["verbs"]
    invalid_verbs = [v for v in verbs if not is_valid_verb_structure(v)]

    if invalid_verbs:
        print(f"❌ Found {len(invalid_verbs)} invalid verb(s).")
        return
    
    else:
        print(f"✅ All {len(verbs)} verb(s) checked.")

    # ✅ Update meta version and last_updated
    version = data["meta"]["version"]
    if not isinstance(version, float):
        print("❌ meta.version must be a float.")
        return

    major = int(version)
    minor = int(round((version - major) * 10))
    minor += 1
    new_version = float(f"{major}.{minor}")
    data["meta"]["version"] = new_version
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["meta"]["last_updated"] = timestamp

    # Write updated file back
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ verbs.json validated and updated to version {new_version}")
        print(timestamp)

if __name__ == "__main__":
    validate_and_update("coniugatto_verbs.json")
