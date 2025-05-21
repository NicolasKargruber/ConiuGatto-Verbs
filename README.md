# conjugatto_verbs.json

## Overview
This repository contains a structured JSON database of Italian verb conjugations with English and German translations, designed for use in language learning applications. The database follows a versioned schema that allows for incremental updates and efficient client-side implementation.

---

## JSON Structure

### Root Level

```json
{
  "meta": {},
  "verbs": []
}
```

---

### Meta Information (`meta`)
Contains metadata about the entire dataset:

- `version`: Integer incremented with each update e.g. 1.0 
- `last_updated`: Flutter DateTime.toString() timestamp  
- `min_app_version`: Minimum client version required  
- `languages`: Supported languages (e.g., `["it", "en", "de"]`)

---

### Verbs Array (`verbs`)
Contains all verb entries with complete conjugation data.

#### Verb Object Structure:

```json
{
  "id": "verb_infinitive",
  "infinitive": {
    "it": "italian",
    "en": "english",
    "de": "german"
  },
  "auxiliary": ["avere", "essere"],
  "irregularities": ["stem change", "past participle", ...],
  "conjugations": {
    "mood": {
      "tense": {
        "pronoun": {
          "it": "Italian",
          "en": "English",
          "de": "German",
          ...
          (more translations)
        }
      },
      ...
      (more tenses)
    },
    ...
    (more moods)
  }
}
```

---

## Versioning Strategy

The `meta.version` integer is incremented with every change to ensure consistency between server and client.

Clients should:

- Store their last fetched version locally  
- Compare it with the server version before performing a full sync  
- Support delta updates when available  
