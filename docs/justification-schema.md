# Justification de l’architecture logicielle du projet **MarsRover**

L’architecture logicielle du projet MarsRover repose sur une **séparation claire des responsabilités**, une **modularité forte** et une **communication centralisée** assurant l’échange fluide entre les différents modules. Cette structure permet de **gérer efficacement les déplacements du rover**, tout en garantissant un système **fiable, maintenable et extensible**.

---

## Structure modulaire

Le projet est organisé autour de plusieurs modules indépendants et spécialisés, chacun ayant une responsabilité bien définie.

| Module              | Rôle                                                                 |
|---------------------|----------------------------------------------------------------------|
| `MissionControl`    | Centre de coordination des commandes et interface de pilotage logique du Rover |
| `Rover`             | Entité mobile, capable de se déplacer, détecter des obstacles, et signaler sa position |
| `Géométrie`         | Fournit les classes `Position` et `Direction`, utilisées pour calculer les déplacements |
| `Obstacle`          | Gère la présence d'obstacles fixes sur la carte et leur interaction avec le Rover |
| `Communication`     | Interface d’échange abstraite et sécurisée entre la couche réseau et la logique applicative |
| `WebSocket`         | Canal réseau temps réel bidirectionnel entre le client et le serveur Python |

---

## 🔁 Logique de dépendances

L'architecture met en place une **hiérarchie de dépendances maîtrisée** :

- `MissionControl` orchestre les déplacements en manipulant un objet `Rover`
- `Rover` s’appuie sur :
  - le module `Géométrie` pour la position et l’orientation
  - le module `Obstacle` pour vérifier la validité des déplacements
- `Communication` agit comme un pont entre la logique de commande (`MissionControl`) et le réseau (`WebSocket`)
- `WebSocket` relaie les messages depuis/vers un client distant (navigateur, simulateur, etc.)

---

## Principe de découplage

Un point fort de l’architecture est son **découplage entre logique métier et infrastructure réseau**. Grâce au module `Communication` :

- Le protocole réseau (WebSocket) est **abstrait** du reste de l'application
- `MissionControl` et `Rover` n’ont **aucune dépendance directe** vers WebSocket
- On peut facilement :
  - simuler la communication en local
  - changer de protocole (ex : REST, MQTT) sans impact majeur
  - intégrer de nouvelles fonctionnalités (logs, sécurité, etc.)

---

## Focus : le module “Communication (secret)”

Le nom “secret” n’est pas anodin : il souligne que ce module agit comme une **boîte noire** sécurisée entre la logique de commande et la couche réseau.

Ce design respecte plusieurs principes **SOLID** :

- **Encapsulation** : Le détail du transport réseau est masqué
- **SRP** (Single Responsibility Principle) : La logique de communication est isolée
- **OCP** (Open/Closed Principle) : La couche réseau est interchangeable sans impacter le cœur applicatif

---

## 🎯 Alignement avec les objectifs du projet

Les choix architecturaux correspondent aux **exigences fonctionnelles et pédagogiques** du projet :

- Le Rover doit recevoir et exécuter des ordres depuis un client distant
- Le retour d'information doit être fluide, rapide, en quasi-temps réel
- Le système doit rester ouvert à des évolutions futures :
  - Exploration de nouveaux terrains
  - Simulation de réseaux instables
  - Intégration d’une IA décisionnelle
  - Multi-rovers collaboratifs

---

## ✅ Conclusion

Cette architecture logicielle garantit :

- Une **communication fluide et fiable** entre les modules
- Une **modularité forte** favorisant les tests, la maintenance et l’évolution
- Une **capacité d’adaptation** à de futurs besoins, sans compromettre la stabilité du cœur du système

Elle respecte également les **bonnes pratiques de génie logiciel**, en proposant une base solide pour la simulation et l’expansion du système MarsRover.
