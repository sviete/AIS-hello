# ais_hello


Jest to minimalna implementacja integracji czujnika / licznika.

### Instalacja w Asystencie domowym

1. Utworzenie folderu z integracją

```
mkdir -p  ~/AIS/custom_components
```

2. Sklonowanie do niego kodów z repozytorium:

```
cd ~/AIS/custom_components
git clone https://github.com/araczkowski/ais_hello.git
```

3. Dodanie integracji do konfiguracji
na końcu pliku ```~/AIS/configuration.yaml``` dodajemy taką konfigurację

```
# ~/AIS/configuration.yaml
sensor:
  platform: ais_hello

```

4. restart usługi ais

```
pm2 restart ais

```
------------------------------------------------------
Więcej informacji na forum Asystenta domowego:

Cześć 1:
https://ai-speaker.discourse.group/t/wlasna-integracja-1-struktura-katalogow/917

Cześć 2:
https://ai-speaker.discourse.group/t/wlasna-integracja-2-przenosimy-kody-do-github/930

Cześć 3:
https://ai-speaker.discourse.group/t/wlasna-integracja-3-platforma-integracji/946

Cześć 4:
https://ai-speaker.discourse.group/t/wlasna-integracja-4-konfiguracja-integracji/975

Cześć 5:
https://ai-speaker.discourse.group/t/wlasna-integracja-5-logowanie-logi/1027

Cześć 6:
https://ai-speaker.discourse.group/t/wlasna-integracja-6-wymagania-zaleznosci/1028

Cześć 7:
