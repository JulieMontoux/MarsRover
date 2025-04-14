# Justification de l’architecture logicielle du projet **MarsRover**

L’architecture logicielle adoptée dans ce projet repose sur une séparation claire des responsabilités, une modularité forte et une évolutivité facilitée par l’utilisation d’un canal de communication centralisé. L’objectif est de permettre une **interaction fluide et temps réel** entre les différents acteurs de la mission, tout en garantissant un système **maintenable et extensible**.

## Structure modulaire

Le système repose sur quatre modules principaux :

| Module | Rôle |
|--------|------|
| `Mission Control` | Interface de contrôle centralisée, capable d’envoyer des commandes au rover |
| `Rover` | Entité réceptrice des commandes, responsable des déplacements, de l’état et des interactions terrain |
| `WebSocket` | Canal de communication bidirectionnel temps réel |
| `Communication (secret)` | Couche intermédiaire sécurisée et abstraite, masquant la complexité du protocole réseau |

## Raison du découplage

L’architecture met en place une **inversion de dépendances** : ni le `Rover` ni `Mission Control` ne dépendent directement du protocole réseau (ici WebSocket). Ces modules utilisent une interface commune, `Communication`, qui **centralise et uniformise** les échanges.

Ainsi :

- `Mission Control` envoie des commandes via `Communication`, sans se soucier du transport (WebSocket, REST, etc.)
- `Rover` reçoit les commandes et y répond via la même interface
- `Communication` encapsule la logique de sérialisation, de filtrage, de routage, etc.

Cette **abstraction** favorise :

- La **testabilité** (on peut simuler `Communication`)
- La **maintenabilité** (on peut changer de protocole réseau sans tout réécrire)
- L’**évolutivité** (on peut intégrer des logs, de la sécurité, du chiffrement, etc.)

## Pourquoi le module “Communication (secret)” ?

Le nom “secret” reflète la volonté de **masquer l’implémentation réelle** du canal réseau. Cela répond à plusieurs principes :

- **Encapsulation** : seuls les modules autorisés accèdent au transport
- **Single Responsibility Principle (SRP)** : chaque module a un rôle bien défini
- **Open/Closed Principle (OCP)** : on peut modifier ou remplacer `WebSocket` sans modifier `Rover` ou `Mission Control`

## Alignement avec les besoins fonctionnels

D’après les objectifs du projet :

- Le rover doit pouvoir exécuter des ordres depuis une interface distante
- Le retour d’informations doit être rapide, fluide, interactif
- Le système doit pouvoir évoluer vers des environnements plus réalistes (réseau instable, exploration, IA…)

L’utilisation de **WebSocket encapsulé dans une couche `Communication` abstraite** est donc cohérente avec :

- L’objectif pédagogique (bonne pratique de découplage)
- Les besoins techniques (temps réel)
- L’ouverture à des fonctionnalités futures

## Conclusion

Cette architecture permet :

- Une communication claire et fiable entre le rover et le centre de contrôle
- Une séparation forte entre logique métier et transport réseau
- Une facilité d’évolution pour intégrer d’autres canaux ou d'autres acteurs (robots multiples, API, IA...)
