[Retour à la table des matières](../README.md)

# Introduction à Docker

## Dockerfile

| Commande | Explication |
| - | - |
| FROM | Détermine l'image à partir de laquelle la personnalisation commence FROM alphine:3.14 |
| COPY | Permet de copier un fichier local dans l'image. COPY LICENSE.TXT / |
| ADD | Permet d'ajouter un fichier local dans l'image. Si c'est une archive, celle-ci est automatiquement décompressée. |
| RUN | Exécute une commande dans l'image (installation de packages, droits, users, ...) RUN echo "hello world" |
| CMD | Détermine la commande à exécuter lors du démarrage du conteneur. CMD ["apache2", "-DFOREGROUND"] |
| EXPOSE | Annonce les ports réseaux. EXPOSE 80/tcp |

### Construire l'image

```
docker build -t imagename ./
```

### Executer l'image

```
docker run -d -p 8080:80 --name containerName imagename
```

### Volume

```dockerfile
docker run -d -p 8080:80 -v /opt/html:/usr/share/nginx/html
```

### Le réseau Docker

| Mode | Explication |
| - | - |
| bridge | Mode par défaut |
| host | Possède la même ip que la machine hôte |
| none | Aucune communication réseau, appart interface loopback |

```
--network=host
```

### Exemple

```dockerfile
FROM nginx:1.21.1
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

