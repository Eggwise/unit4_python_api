#Unit4 Python API Generator

Dit systeem genereert aan de hand van de Unit 4 Web API documentatie pagina een wrapper library voor python waarmee de Unit 4 Web API te benaderen is.
Dit systeem wordt ontwikkeld om de ontwikkeling van software applicaties waarbij de Unit 4 Web API geintegreerd wordt te vergemakkelijken.



###Hoe werkt het:

De pagina https://api.online.unit4.nl/v182/help/ wordt ingelezen door de page extractor.
Hieruit resulteerd een json bestand die in de extracted map terecht komt.
De library generator leest dit bestand vervolgens in om hiervan python modules te maken.
De uiteindelijke library komt terecht in de “generated” folder.


###Wat werkt er nog niet:
- De methode namen van de python classes worden nog niet volgens een mooi “pythonic” formaat gegenereerd.
- Sommige methodenamen worden nog niet goed gegenereerd, zie administration_data.AccountInfo.py
- Authorizatie van requests
- Return values van requests


***
Warning WIP (Work in progress)

Do not use the library because all method names will be changed in further releases.



http://www.eggwise.com

^

website also WIP.


