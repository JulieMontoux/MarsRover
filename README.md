# Mars Rover Exercice

Paul Carion, Mathieu Gaisnon, Yassin Farassi, Nicolas Daunac, Baptiste Mancel et Julie Montoux

## Lancement

Pour lancer le projet via les WebSockets il faut :

```bash
python main.py
```

Cette commande lancera l'ensemble du projet ainsi que le server du websocket.

Une fois lancé vous avez trois options:

### Le client Python

```bash
python3 src/WebSocket/client_test.py
```

C’est la meilleure solution pour tester dans le terminal.

### Un outil spécialisé comme WebSocket King

Ouvre <https://websocketking.com>

- Dans le champ URL, tape : *ws://localhost:8765*
- Clique sur "Connect"

Une fois connecté, tu peux envoyer A, G, POSITION…

⚠️ Il faut que le serveur WebSocket (main.py) tourne avant et que le navigateur autorise le localhost.

### Postman

Onglet "New"

Type "WebSocket Request"

Adresse : *ws://localhost:8765*
Clique sur "Connect", puis envoie des messages dans la console.

## Versionning

1.0.0 : Interaction CMD + renvoie de la position et de l'orientation

## 🧭 Schéma de l'architecture logicielle

![Schéma de dépendances WebSocket](./docs/schema%20archi.png)

*Ce schéma illustre les relations entre les modules principaux du projet : Rover, Mission Control, Communication et WebSocket.*
Nous avons donc changer notre schema pour accueillir un module qui va venir gérer la position et l'orientation : Géométrie. Ces deux vont gérer les orientations cardinales et 
la postion x et y du rover sur la planète

Module Rover : 
- Nous venons gérer dans ce module l'état du rover (postion et direction), il est l'élement principale du Rover
- Ce module dépend de la Géometrie pour fonctionner 
- Nous venons gérer également dans ce module le comportement du rover comme l'execution de la commande recu, la détection d'obstacle

Module WebSocket : 
- Ce module va venir gérer le serveur WebSocket. Pour chaque message recu, il va envoyer la commande au Rover ainsi que renvoyer une réponse au client avec l'emplcaement du rover sur la carte

Module MissionControl : 
- Il vient initailiser le rover à une postion, il vient également interpreter et executer les commandes ainsi que récuperer la position du rover et l'afficher sur la carte

### **État d'avancement du projet MarsRover**

| **Fonctionnalité**                                      | **Statut**        | **Détails** |
|---------------------------------------------------------|-------------------|-------------|
| **Initialisation du Rover**                            | ✅ Fait            | Le rover est bien initialisé avec une position `(x, y)` et une orientation (`N, S, E, W`). |
| **Déplacements (avancer/reculer)**                     | ✅ Fait            | Les commandes `A` et `R` fonctionnent correctement. |
| **Rotation (Gauche/Droite)**                           | ✅ Fait            | Les commandes `G` et `D` changent correctement l'orientation du rover. |
| **Planète Toroïdale (gestion des bords)**              | ✅ Fait            | Le rover "boucle" lorsqu'il atteint les limites de la grille. |
| **Détection des Obstacles**                            | ✅ Fait            | Le rover affiche un message lorsqu'il rencontre un obstacle. |
| **Tests unitaires de base**                            | ✅ Fait            | Il y a des tests unitaires couvrant `Position`, `Direction`, `EtatRover`, `ObstacleFixe` et `Rover`. |
| **Exécution d'une séquence de commandes**             | ⏳ Partiellement fait | Les commandes peuvent être enchaînées, mais il manque une gestion plus avancée des erreurs et des séquences longues. |
| **Blocage du déplacement si obstacle**                 | ✅ Fait       | Le rover **affiche un message** et **bloque son déplacement** lorsqu'un obstacle est rencontré. |
| **Affichage visuel de la carte en console**            | ✅ Fait        | Il y a **une grille ASCII** affichant la position du rover et des obstacles. |
| **Tests unitaires avancés (cas limites, entrées invalides)** | ❌ Non fait        | Il manque des tests pour les **commandes invalides, bords de la grille, et obstacles multiples**. |
| **Gestion dynamique des obstacles (mode découverte)**  | ❌ Non fait        | Les obstacles sont fixes et connus dès le début. Un mode où ils sont **découverts progressivement** pourrait être ajouté. |
| **Communication réseau (Rover Distribué)**             | ✅ Fait         | Le rover fonctionne via une **WebSocket** permettrait de lui envoyer des commandes à distance. |

### **Prochaines étapes**

1. **Améliorer les tests unitaires** en ajoutant des cas limites (ex: bords, obstacles, commandes invalides).
2. **Créer un mode "exploration"** où les obstacles ne sont découverts qu’au fur et à mesure.
