# conjugatto_verbs.json

## Overview
This repository contains a structured JSON database of Italian verb conjugations with English and German translations, designed for use in language learning applications. The database follows a versioned schema that allows for incremental updates and efficient client-side implementation.

---

## JSON Structure

### Root Level (Example)

```json
{
  "meta": {
    "version": 1.0,
    "last_updated": "2025-05-121 09:06:00",
    "min_app_version": "0.3.1",
    "languages": ["italian", "english", "german", "spanish"]
  },
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
  "id": "salire",
  "infinitive": {
    "italian": "salire",
    "english": "to go up",
    "german": "steigen"
  },
  "auxiliary": ["avere", "essere"],
  "irregularities": ["spelling change", "stem change", "past participle", "present gerund", "using -isc-"],
  "conjugations": {
       "indicativo": {
         "presente": {
           "io": {"italian": "salgo", "english": "go up"},
           "tu": {"italian": "sali", "english": "go up"},
           "lui/lei": {"italian": "sale", "english": "goes up"},
           "noi": {"italian": "saliamo", "english": "go up"},
           "voi": {"italian": "salite", "english": "go up"},
           "loro": {"italian": "salgono", "english": "go up"}
         },
         "imperfetto": {},
         "passato_remoto": {},
         "futuro_semplice": {}
       },
       "congiuntivo": {
         "presente": {},
         "imperfetto": {}
       },
       "condizionale": {
         "presente": {}
       },
       "imperativo": {
         "positivo": {}
       }
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
