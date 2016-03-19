# Comment éviter les infections sur un ordinateur Windows.

L'infection la plus répandue de nos jours est le publiciel (adware).
C'est un logiciel qui infecte votre ordinateur dans le but d'insérer de la
publicité dans votre ordinateur, souvent dans votre navigateur, via de
l'obstruction ("pop-ups", redirection vers d'autres sites, etc.) et le
changement de votre page d'accueil par une autre.

Il y a aussi des logiciels qui tentent de vous faire peur avec des messages
alarmistes. Il peuvent vous demander des informations personnelles ou vous
demander d'effectuer une action qui pourrait compromettre votre ordinateur.

Les symptomes d'un ordinateur malade sont les suivants:

* Le(s) navigateur web est truffé de "pop-ups" et de publicité, la page par défaut
du navigateur a changé sans notre consentement.

* Des logiciels malveillants affichent des messages inquiétants, disant que
l'ordinateur est vulnérable (souvent en anglais), ou qu'un virus se trouve
sur votre ordinateur (ironique, car le logiciel vous disant ça est le virus).
Les messages erreurs peuvent varier, et le virus est souvent fait pour avoir
l'air menaçant ou ressembler à l'interface de Windows.

**En général, Microsoft et Windows ne devraient jamais vous demandez votre
numéro de carte de crédit. À moins d'un achat en ligne, il n'y a pas de raison
d'utiliser votre carte de crédit.**

**Lorsqu'on remarque que sont ordinateur est infecté, éviter d'entrer de
l'information confidentielle!**

(En passant, si vous recevez un coup de téléphone de Microsoft à la maison,
c'est une arnaque. Microsoft n'a aucune raison de vous appeler chez vous!)

## Navigation
* Prévention
    * [Installation de logiciels](#installation-de-logiciels)
    * [Bloqueur de publicité](#bloqueur-de-publicit-)
* [Nettoyage après sinistre](#nettoyage-apr-s-sinistre)
    * [Anti-virus](#anti-virus)
    * [Nettoyeur de publiciels](#nettoyer-de-publiciels)
* [À long terme](#--long-terme)

## Prévention
### Installation de logiciels
L'installation de logiciel est la porte d'entrée des publiciels. L'installation
de logiciels requiert les droits d'administrateur de votre ordinateur. C'est
donc l'occasion rêvée d'installer des publiciels à votre insu.

La grande majorité des installateurs de logiciels offrent l'option de ne pas
installer les publiciels. Le problème est que l'option n'est pas cochée par
défaut, et les gens appuient sur suivant sans se donner la peine de vérifier.

Plusieurs logiciels réputés installent des publiciels, comme Skype, Flash et
Java. Il faut faire très attention lorsqu'on télécharge un installateur du web.
Les fichiers terminant en ".exe" ou ".msi" doivent être gérés avec beaucoup
de précaution!
### Bloqueur de publicité
Les bloqueurs de publicité permettent de faire disparaître les publicitées
lorsqu'on navigue le web. Supprimer les publicités des pages web, vous permet
non seulement d'avoir la paix, mais aussi de charger les pages web plus
rapidement. Les bloqueurs bloquent aussi les éléments potentiellement
dangereux, comme les sites frauduleux et malveillants.

Voici les meilleurs bloqueurs de publicité pour chaque navigateur.

* [Firefox](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)
* [Chrome](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
* [Internet Explorer](https://adblockplus.org/en/internet-explorer)
    * Désactiver l'affichage des publicitées ditent "acceptable" dans les options.

## Nettoyage après sinistre
Lorsque votre ordinateur est déjà infecté, la prévention ne peut pas enlever
les virus existants. Cette section discute de comment de débarasser des virus
et des publiciels.

**Il est très important de faire une sauvegarde des données importantes de
l'ordinateur sur un média externe. Les étapes de nettoyage peuvent ne pas
fonctionner, et dans de rare cas endommager votre système d'exploitation.**

### Anti-virus
Microsoft à créé un anti-virus gratuit, appelé "Microsoft Security Essentials"
sur Windows 7 et "Windows Defender" sur Windows 8, 8.1 et 10. L'anti-virus
qui est capable d'éliminer beaucoup de problèmes. L'anti-virus est inclut
dans Windows 8, 8.1 et 10, mais doit être installé dans Windows Vista et Windows 7.
[Télécharger ici](http://windows.microsoft.com/fr-CA/windows/security-essentials-download).

Une fois installé, il faut faire un scan **complet** de l'ordinateur. Le scan
peut prendre plusieurs heures. Une fois le scan terminé, si l'anti-virus a
détecté des virus, il faut lui dire de les enlever.

Il est possible que cette méthode n'arrive pas à enlever tous les virus sur
votre ordinateur. Windows Defender arrive à enlever quelques publiciels,
mais n'est pas parfait. Il y a un outil qui s'attaque aux publiciels
discuté dans la prochaine section.

### Nettoyeur de publiciels
L'outil s'apelle [AdwCleaner](https://toolslib.net/forum/viewthread/183-fr-documentation-adwcleaner/).
Il est très simple à utiliser.

**Enregistrer les documents sur lequels vous travaillez avant d'utiliser l'outil
car il redémarrera votre ordinateur.**

1. Télécharger l'outils à partir du lien plus haut.
2. Lancer l'outil.
3. Dans le menu "Option", décocher les options qui sont cochées.
4. Appuyer sur "Scanner".
5. Appuyer sur "Nettoyer" lorsque le scan est terminé.
6. Votre ordinateur devrait être redémarré.

## À long terme
Si vous avez des difficultées récurrentes, vous pouvez essayer de réinstaller
votre système d'exploitation à neuf. Une fois reéinstallé, il faut faire de la
prévention rigoureuse pour empêcher une autre infection.

Windows est un système d'exploitation très vulnérable. Le mode de distribution
d'applications est ce qui cause tous ces problèmes. Télécharger un fichier
exécutable de l'internet est extrêmement dangereux. Les téléphones mobiles,
par exemple, disposent d'un "App Store", qui est un espace controllé et
centralisé pour la distribution de logiciels. Ils peuvent donc guarantir que
les logiciels téléchargés sont authentiques et sans virus.

Il n'y a, malheureusement, pas beaucoup d'alternatives à Windows. Mac est
plus dispendieux et parfois non-compatible avec certains logiciels.

Linux est une famille de systèmes d'exploitation libres. C'est à dire que le
code source est accessible à tous, et qu'il n'est pas nécessaire de débourser
de l'argent pour l'obtenir. Linux est divisé en plusieurs distributions. Les
distributions Ubuntu et Linux Mint, par exemple, s'adressent à des usagers
novices. Ubuntu et Mint possèdent tous deux des "App Stores", qui gèrent
la distribution de logiciels de façon sécuritaire. On ne télécharge jamais
de fichier exécutable de l'internet avec Linux.

Tout ce qui est Web fonctionne sur Linux (hotmail, Office 365). Toutefois,
les applications Windows n'existent pas toujours sur Linux (e.g Office). Il
existe presque toujours des alternatives aux applications Windows. Par exemple,
Libre Office offre les mêmes fonctionalitées que Office.

1. [Ubuntu](http://www.ubuntu.com/)
2. [Linux Mint](https://www.linuxmint.com/)
