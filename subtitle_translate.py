print("""
******************************************************
Englisch-Türkisch Untertitel Translate Programm
******************************************************
Deutsch:
Programm Beschreibung:

Von Coursera heruntergeladene Untertitel, beispielsweise lautet die englische Sprache 'subtittle-en.vtt'.

Wenn Sie für mehr als eine Datei übersetzen möchten, nummerieren Sie den Anfang Ihres Dateinamens wie '1_subtitle-en.vtt' ...

Programmzusammenfassung:

1-Sie geben das Verzeichnis ein, in dem sich Ihre Untertitel befinden ...
2-Hier nimmt alle -en.vtt die Namen Ihrer Dateien und setzt sie auf die Liste ...
3-Die Erweiterung für jede Datei muss .txt sein, um Google Translation hochladen zu können ...
Die Google-Erweiterung erkennt die .vtt-Datei hier nicht. Sie übersetzt die Dateierweiterung
4-Gehen Sie zur Google Übersetzungs-Website, laden Sie unsere Datei der Reihe nach hoch und
führen Sie die erforderlichen Aktionen aus...
5-Was auch immer der alte Dateiname ist, er ändert den Namen nicht auf die gleiche Weise,
er überschreibt unsere übersetzte Datei ...
********************************************************
""")
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print('Willkommen zum Untertitelübersetzungsprogramm...\n')
time.sleep(2)
path=input("Geben Sie den Pfad ein, in dem sich Ihre Untertitel befinden:")

os.chdir(path)

list=[]         
for root, dirs, files  in os.walk(path):
    for i in files:
        if i.endswith("-en.vtt"):
            list.append(i)
        else:
            continue

for file in list:
    
    dateiname=file.replace('.vtt','.txt')
    os.rename(file,dateiname)
    

    path2=path+f"\{dateiname}"
    
    
    
            
      
    browser = webdriver.Firefox()

    browser.get("https://translate.google.com/?hl=de#view=home&op=translate&sl=auto&tl=tr")

    time.sleep(1)

    button=browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div")
    button.click()

    durchsuchen=browser.find_element_by_xpath("//*[@id='tlid-file-input']")
    durchsuchen.send_keys(path2)

    time.sleep(2)

    übersetzen=browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div/form/div[2]/div[2]/input')
    übersetzen.click()

    time.sleep(1)

    texts=browser.find_element_by_xpath('/html/body/pre')
        
        
    
    with open(dateiname,"w",encoding="UTF-8") as file:
        file.write(texts.text)
            
    with open(dateiname,"r+",encoding="UTF-8") as file1:
        file1.seek(0)
        file1.write("WEBVTT")
            
    lists=[]
    with open(dateiname,"r+",encoding="UTF-8") as file2:
        for i in file2:
            i1=i.replace("->","-->")
            i2=i1.replace(": ",":")
            lists.append(i2)
    with open(dateiname,"w",encoding="UTF-8") as file3:
        for i in lists:
            file3.write(i)
    path2=path           
    os.rename(dateiname,dateiname.replace('-en.txt','-tr.vtt'))     
print("Ihre Transaktion wurde erfolgreich abgeschlossen...")
print("Programm wird beendet...")


