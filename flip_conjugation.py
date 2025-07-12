import json
from pathlib import Path

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

    verbs = data["verbs"]

    for verb in verbs:
        # Replace "imperativo" "positivo" "german" "lui/lei" with "german" "loro"
        if "imperativo" in verb["conjugations"] and "positivo" in verb["conjugations"]["imperativo"] and "lui/lei" in verb["conjugations"]["imperativo"]["positivo"]:
            if verb["conjugations"]["imperativo"]["positivo"]["lui/lei"] and verb["conjugations"]["imperativo"]["positivo"]["loro"]:
                verb["conjugations"]["imperativo"]["positivo"]["lui/lei"]["german"] = verb["conjugations"]["imperativo"]["positivo"]["loro"]["german"]
                verb["conjugations"]["imperativo"]["positivo"]["loro"]["german"] = (verb["conjugations"]["imperativo"]["positivo"]["loro"]["german"]).lower()
                print(f"✅ Updated 'lui/lei' to 'loro' for {verb['infinitive']['italian']}")


    # Write updated file back
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ verbs.json updated")

if __name__ == "__main__":
    validate_and_update("coniugatto_verbs.json")
