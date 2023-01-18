## Selenium from scratch

### Hur man börjar koda:
1. Installera pycharm.
2. Skapa nytt projekt (välj virtual env)
3. Kör "pip install selenium" i terminalen för mappen.  
(Terminalen hittas längst ner i pycharm)  

Syfte: Ha ett IDE att använda för att koda  


### Testa Selenium
Filer hittas under 1_selenium_setup  
1. Kör 1_test_google.py
2. Funkar ej chrome? Kör "pip install webdriver-manager"
3. Kör 2_test_google.py

Syfte: Verifiera att Selenium starta chrome och fungerar.  


### Förbättra projektet (Kan skippas)
1. Generera en requirements fil
   1. Klicka "Tools"
   2. Klicka "Sync Python Requirements"
   3. Klicka "Ok"

Syfte: Få in vilken version av Selenium som används, och möjlighet att lägga in flera pip.

### Importera pytest
Filer hittas under 2_pytest_stuff  
1. Kör pip install pytest i terminalen
2. Kör testet inuti 1_pytest.py
3. Kör testet inuti 2_pytest_fixtures.py

Syfte:  
Testat att köra tester i IDE direkt.   
Fått upptäcka fixtures, något som omvänds för att sätta upp testerna

