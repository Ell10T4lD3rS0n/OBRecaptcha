# OBRecaptcha - Dev with :heart:

<p align="center">
  <img src="https://i.imgur.com/2ZVQP1y.png" width="350" title="logo">
</p>

## :clipboard: Sommaire :

- [:information_source: | Description](#description)
- [:fr: | Tutoriel](#tutoriel)
- [:speech_balloon: | Me contacter](#contact)


<div id='description'/> 

## :information_source: | Description :
Script Python qui permet de savoir si le recaptcha v3 d'un site est bypassable et si bypassable il génère un txt avec du loliscript idéal pour Openbullet v1

<div id='tutoriel'/> 

## :fr: | Tutoriel :
1. Installation les modules prérequis :
```
pip install -r requirements.txt
```

2. Exécutation du script Python :
```
py OBRecaptcha.py
```

3. Insérez le lien anchor :
```
Entre l'URL anchor ► https://www.google.com/recaptcha/api2/anchor?ar=1&k=xxxxxx&co=xxxxxx&hl=fr&v=xxxxxx&size=invisible&cb=xxxxxx
```

4. Puis insérer les données des varibles suivantes : le CHR, le VH et le BG (vous les trouverez dans la partie client de la requête reload)
```
CHR [xx,xx,xx] : [xx,xx,xx]                 # Le CHR est repérable car il a des crochets et contient des nombres à l'intérieur
VH : xxxxxxxx                               # Le VH se trouve après une étoile (*) et il est composé entierement de chiffres et parfois par un tiret (-) devant
BG !x* : !xxxxxxxxxxxxxxxxxxx*              # Le BG commence par un point exclamation (!) et s'arrête jusqu'à une étoile (* )
```

5. Si le reCAPTCHA n'est pas bypassable il vous retournera "Bypass Recaptcha Impossible" si bypassable il vous retournera "Bypass Recaptcha Possible"

6. Pour finir un .txt se créera depuis l'emplacement où vous avez exécuté le script se nommant "loliscript.txt" contenant le loliscript pour Openbullet 1

7. ENJOY :tada:

<div id='contact'/> 

## :speech_balloon: | Me contacter :

<a href="https://t.me/Ell10T_4lD3rS0n">
<img src="https://i.imgur.com/R8MjNmT.png"  alt="Telegram" width="100" height="100"/>
</a>
<a href="https://twitter.com/Ell10T_4lD3rS0n">
<img src="https://i.imgur.com/zIKc8id.png"  alt="Twitter" width="100" height="100"/>
</a>
