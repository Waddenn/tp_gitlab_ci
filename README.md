# TP GitLab CI – Exemple d’application Python

Ce projet contient une petite application Python conteneurisée et un workflow **GitHub Actions** permettant de **builder** et **pusher** automatiquement l’image Docker vers le **GitHub Container Registry (GHCR)**.

---

## Lancer l’application

### 1. Récupérer l’image
L’image est automatiquement publiée ici :  
[`ghcr.io/waddenn/tp_gitlab_ci:latest`](https://ghcr.io/waddenn/tp_gitlab_ci)

Télécharge et exécute le conteneur :
```bash
docker run -d \
  --name tp_gitlab_ci \
  -p 5000:5000 \
  ghcr.io/waddenn/tp_gitlab_ci:latest
```
<img width="332" height="87" alt="screenshot-2025-10-16_15-33-12" src="https://github.com/user-attachments/assets/ca158390-6766-431b-a1e2-e9a2a359fb02" />

