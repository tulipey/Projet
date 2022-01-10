=========================================
Informations générales Web e-sport projet
=========================================

:Auteur:            Valentin Carrion, Baptiste Tarte, Léonce Duquerroy
:Projet:            Web e-sport
:Version:           0.1.0
:Liens:             `Valentin <valentin.carrion@etu.univ-poitiers.fr>`_,
                    `Baptiste <baptiste.tarte@etu.univ-poitiers.fr>`_,
                    `Léonce <leonce.duquerroy@etu.univ-poitiers.fr>`_

####

Description
===========

    Ce projet permet d'analyser les statistiques d'une partie du jeu vidéo Rocket League.
    
####

Arborescence du projet
======================
::

    PROJETGitHUB
      ├── .git/               # ``.git`` le répertoire dédié à Git.
      ├── data/               # ``data`` le répertoire dédié à stocker différents fichiers de données récupérées et générées pour les besoin du projet.
      │   └── ...
      ├── docs/               # ``docs`` le répertoire dédié à stocker la documentation du projet au format retructuredText (répertoire généré automatiquement par sphinx-build).
      │     ├── build/
      │     │    └── html/
      │     └── source/ 
      │    	 ├── index.rst 
      │    	 ├── conf.py 
      │    	 ├── content/ 
      │    	 ├── _static/ 
      │          └── _templates/    
      ├── html/                          # ``html`` répertoire contenant le site web statique de présentation des résultats.
      │   └── ...
      ├── __init__.py                    # ``__init__.py`` fichier indiquant la version du projet.
      ├── nomprojet/                     # ``nomprojet`` le répertoire dédié aux fichiers source Python développés lors du projet.
      │    └── nomprojet.py
      ├── tests/                         # ``tests`` le répertoire dédié aux tests unitaires des fonctions développées dans le projet.
      │   ├── __init__.py
      │   └── test_programme_projet.py  
      ├── .gitignore                     # ``.gitignore`` le fichier permettant de configurer Git pour ne pas envoyer sur le dépôt distant les fichiers temporaires.
      ├── AUTHORS                        # ``AUTHORS`` le fichier indiquant le nom des auteurs et de leurs coordonnées.
      │ 
      └── requirements.txt               # ``requirements.txt`` fichier texte décrivant la version de Python utilisée et les dépendances du programme python.
