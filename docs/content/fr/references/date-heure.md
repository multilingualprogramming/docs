---
page_id: reference__datetime
locale: fr
title: Date et heure
path_segments:
- references
- date-heure
source_hash: 4e5871b97df0
status: translated
permalink: /fr/docs/references/date-heure/
---

`multilingual` fournit des classes de date et d'heure multilingues capables d'analyser et de formater les dates selon les conventions des langues prises en charge.

---

## `MPDate`

Classe de date multilingue avec analyse et formatage localisés.

{{snippet:reference__datetime__py01}}

---

## `MPTime`

Classe d'heure multilingue.

{{snippet:reference__datetime__py02}}

---

## `MPDatetime`

Classe combinée pour la date et l'heure.

{{snippet:reference__datetime__py03}}

---

## Exemples de mois

| Numéro | Anglais | Français |
|--------|---------|-----------|
| 1 | January | janvier |
| 2 | February | février |
| 3 | March | mars |
| 4 | April | avril |
| 5 | May | mai |
| 6 | June | juin |
| 7 | July | juillet |
| 8 | August | août |
| 9 | September | septembre |
| 10 | October | octobre |
| 11 | November | novembre |
| 12 | December | décembre |

---

## Fichiers de ressources

Les ressources de date et d'heure sont stockées dans :

```text
multilingualprogramming/resources/datetime/
├── months.json      # Noms des mois
├── weekdays.json    # Noms des jours
├── eras.json        # Noms des ères
└── formats.json     # Formats par langue
```

---

## Littéraux de date dans les programmes

Les programmes `multilingual` prennent en charge les littéraux de date via des délimiteurs dédiés :

{{snippet:reference__datetime__py04}}

---

## Intégration avec `datetime`

`MPDate` et `MPTime` sont interopérables avec le module standard `datetime` de Python :

{{snippet:reference__datetime__py05}}
