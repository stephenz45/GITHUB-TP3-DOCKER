# TP 3 : premiers conteneurs avec Docker

Cours : Introduction au Cloud, L3 SI (BDGL), séance 3

**Auteurs :** TRA BI TRA Christian David et Kouadio Yao Boffouo Siedou

## Contenu du dépôt
- [`TP3.md`](TP3.md) : compte rendu du TP (commandes, sorties, captures, tableau de comparaison, réponses aux questions, difficultés, conclusion)
- `api/` : l'API fil rouge (`app.py`, `requirements.txt`, `Dockerfile`, `.dockerignore`)
- `images/` : captures d'écran utilisées dans le compte rendu
- `TP3_Presentation.pptx` : présentation détaillée du TP


## Image publiée
`ghcr.io/stephenz45/api-fil-rouge:1.1`

## Résumé
Installation de Docker dans la VM `ubuntu-srv`, lancement et inspection de conteneurs (`hello-world`, Nginx), volume, comparaison conteneur et VM, conteneurisation d'une API Flask (Dockerfile, cache de build, versions 1.0 et 1.1), publication de l'image sur GitHub Container Registry, récupération depuis le registre et nettoyage.
