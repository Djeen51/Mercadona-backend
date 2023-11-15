# Mercadona-backend
la partie backend de studi mercadona

pour déployer le site, bien penser à taper la commande : 
python manage.py collectstatic 

le déploiement est fait via fly.io

pour lancer les tests unitaires lancer la commande : 
pytest

les résultats des tests sont disponnibles dans report.html

pour connaitre le % de couverture des tests, lancer la commande : 
pytest --cov=base

les résultas peuvent être récupéré sur htmlcov/index.html 

côté frontend, la commande "npm run build" pour créer le fichier static qui sera utilisé pour le site
Attention, pour relier la partie backend et frontend, bien vérifier les les paths pour les fichiers statics : 

exemple : 
dans mon environnement local, le path est agencé ainsi: 

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'frontend/dist/static'
]

MEDIA_ROOT = '/data'



