Web : statistiques sur l’e-sport
Cadre et objectif général
Le projet a pour objectif d’extraire des données de parties de Rocket League. Lorsqu’un match se termine, grace à un plugin du jeu, un fichier .csv est enregistré sur le site. Ce dernier indique un certain nombre d’informations pour chaque joueur : le score accumulé, l’équipe du joueur, le nombre de buts, de passes, d’arrêts, de tirs, de démolitions, etc; Il s’agit ici de récupérer automatiquement le fichier csv de la partie puis d’afficher sur une page web un résumé du match.

lire et extraire les données pertinentes des fichiers provenant des différents sites web ;

les traiter afin de pouvoir produire les données suivantes :
tableau de la liste des joueurs et de leur équipe :

Joueur	Equipe
Joueur1	 
…	…
Joueurn	 
pour chaque joueur un diagramme camembert qui présente les pourcentages de buts marqués, de passes, d’arrêts, de tirs, de démolitions, etc; relativement à toutes les actions du match

pour chaque équipe un camembert identique au précédent

de générer une page html/css sur laquelle seront présentées les données extraites et calculées. On pourra pour cela utiliser le module matplotlib et exporter les graphiques au format image .png.

Le projet doit :

utiliser l’outil de gestion de version Git et un IDE de développement Python ;

être structuré suivant l’arborescence indiquée ci-après

pouvoir s’exécuter sur le système Linux des salle de TP lors de la démonstration finale ;

être documenté :

description du projet au format restructuredText,
commentaires pertinents dans le code (si utile à la compréhension),
commentaires des fonctions développées
comporter un répertoire de test où toutes les fonctions Python développées auront un code test unitaire

Environnement de développement et dépôt GIT
Le projet est rattaché à un dépôt GIT que vous aurez créé sur GitHub et à la livraison de vos codes informatiques. Le versionnement étant tracé et daté, il servira de preuves pour le travail.

Langages de scripting/programmation
Le projet doit utiliser :

le langage de programmation Python (version > 3.7) pour les codes sources gérant la lecture, l’analyse, le traitement des données et la publication de leur analyse.
et/ou le langage de script bash pour les scripts permettant l’automatisation de certains traitements et de la publication des résultats (vu en R108-Base des systèmes d’exploitation)
Arborescence du projet
Votre projet doit :

être exécuté par le biais d’un script programme_projet.py. Ce script reprendra la structure classique des programmes vue en R107-Fondamentaux de la programmation et décrite dans le formulaire Python. Il prendra d’éventuels paramètres en arguments spécifiés ci-après.

respecter l’arborescence suivante (PROJETGitHUB désigne le répertoire auquel est rattaché votre projet et constitue la base du dépôt local Git) :

PROJETGitHUB
├── .git/
├── data/
│   └── ...
├── docs/
│     ├── build/
│     │    └── html/
│     └── source/
│          ├── index.rst
│          ├── conf.py
│          ├── content/
│          ├── _static/
│          └── _templates/
├── html/
│   └── ...
├── __init__.py
├── nomprojet/
│    └── nomprojet.py
├── tests/
│   ├── __init__.py
│   └── test_programme_projet.py
├── .gitignore
├── AUTHORS
│
└── requirements.txt
.git le répertoire dédié à Git.

data le répertoire dédié à stocker différents fichiers de données récupérées et générées pour les besoin du projet.

docs le répertoire dédié à stocker la documentation du projet au format retructuredText (répertoire généré automatiquement par sphinx-build).

html répertoire contenant le site web statique de présentation des résultats

__init__.py fichier indiquant la version du projet :
__version__ = '0.1.0'
nomprojet le répertoire dédié aux fichiers source Python développés lors du projet

tests le répertoire dédié aux tests unitaires des fonctions développées dans le projet

tests/__init__.py fichier vide

.gitignore le fichier permettant de configurer Git pour ne pas envoyer sur le dépôt distant les fichiers temporaires

AUTHORS le fichier indiquant le nom des auteurs et de leurs coordonnées

requirements.txt fichier texte décrivant la version de Python utilisée et les dépendances du programme python (modules et version des modules Python)

Warning

Les fichiers : .gitignore commence avec un point.
Note

Vous pouvez :

ajouter au besoin autant de modules que nécessaires, pour structurer votre code, en les stockant à la racine du répertoire nomprojet.
Paramètres en argument du programme principal
Votre programme devra prendre en argument le fichier csv de la partie et le répertoire dans lequel sera générée la page web :

$ ./programme_projet.py  --csv partie.csv --output-dir ./../html/
Documentation
La documentation générale du projet devra être écrite au format restructuredText. Vous pourrez pour cela vous appuyer sur le logiciel Sphinx ;
Il conviendra d’ajouter des commentaires doctrings en début de fonction afin de :
préciser ce que fait la fonction,
d’indiquer son auteur, ses dates de création et de dernière modification,
décrire ses paramètres et le cas échéant leurs types,
décrire les bornes d’utilisation de paramètres pour un bon fonctionnement de la fonction et exceptions qui sont suceptibles d’être levées,
ce qu’elle retourne
donner un exemple d’utilisation
Tests unitaires
En vous inspirant du TP sur les fonctions, vous devrez écrire un code de test de chaque fonction développée dans le projet. Celui-ci sera placé dans un programme Python du répertoire tests.