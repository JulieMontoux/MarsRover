# Mars Rover Exercice

Paul Carion, Mathieu Gaisnon, Yassin Farassi, Nicolas Daunac, Baptiste Mancel et Julie Montoux

## Versionning

1.0.0 : Interaction CMD + renvoie de la position et de l'orientation

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
| **Blocage du déplacement si obstacle**                 | ❌ Non fait        | Le rover **affiche un message** mais ne **bloque pas son déplacement** lorsqu'un obstacle est rencontré. |
| **Affichage visuel de la carte en console**            | ❌ Non fait        | Il n’y a **pas encore de grille ASCII** affichant la position du rover et des obstacles. |
| **Tests unitaires avancés (cas limites, entrées invalides)** | ❌ Non fait        | Il manque des tests pour les **commandes invalides, bords de la grille, et obstacles multiples**. |
| **Gestion dynamique des obstacles (mode découverte)**  | ❌ Non fait        | Les obstacles sont fixes et connus dès le début. Un mode où ils sont **découverts progressivement** pourrait être ajouté. |
| **Communication réseau (Rover Distribué)**             | ❌ Non fait        | Le rover fonctionne uniquement en local. Ajouter une **WebSocket** ou une **API** permettrait de lui envoyer des commandes à distance. |

### **Prochaines étapes**
1. **Corriger la gestion des obstacles** pour empêcher le rover de bouger s’il rencontre un obstacle.
2. **Ajouter une carte ASCII dynamique** affichant la position du rover et des obstacles.
3. **Améliorer les tests unitaires** en ajoutant des cas limites (ex: bords, obstacles, commandes invalides).
4. **Créer un mode "exploration"** où les obstacles ne sont découverts qu’au fur et à mesure.
5. **Ajouter une communication réseau** via **WebSocket** ou **API REST** pour permettre l’envoi de commandes à distance.
