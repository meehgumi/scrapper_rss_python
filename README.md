# 📰 Scraper de flux RSS asynchrone

Ce projet Python permet de parcourir une grande liste de flux RSS à la recherche d'articles contenant des mots-clés spécifiques. Il est optimisé grâce à un traitement asynchrone pour une performance maximale.

## ✅ Fonctionnalités

- Chargement des URLs de flux RSS depuis `rss_list.txt`
- Lecture des mots-clés depuis `mots_cles.txt`
- Récupération asynchrone des flux avec `aiohttp`
- Parsing des flux avec `feedparser`
- Filtrage des articles contenant au moins un mot-clé
- Affichage clair dans le terminal
- Sauvegarde dans le fichier `resultat.txt`
- Log des erreurs dans `scraper.log`

## 🧰 Dépendances

Installe les bibliothèques nécessaires avec :

```bash
pip install aiohttp feedparser
