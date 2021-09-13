# workshop-data-science

Intensivkurs Grundlagen und Anwendung von Data-Science und Machine-Learning mit Python

## Systemvoraussetzungen

- Ein vernuenftiges Betriebssystem: Linux, MacOS oder Windows 10
- Python 3.9.6 mit pip (Package Installer for Python)

## Vorausgesetzte Kenntnisse

- Grundlagen der Programmierung
- Grundlagen Mathematik auf Hochschulniveau
- Umgang mit der Kommandozeile

## Installation

Als erstes muss der Python-Interpreter und Paketmanager selbst installiert werden.
Aufgrund der globalen Sichtbarkeit von Abhängigkeiten in Python ist es besser, fuer jedes Projekt eine eigene, virtuelle Python-Umgebung zu erstellen. Dies garantiert reproduzierbares Verhalten.

1. Python direkt ueber den Paketmanager in Linux/MacOS installieren.  
Falls Version 3.9.6 noch nicht verfügbar sein sollte, alternativ das offizielle [Release hier herunterladen](https://www.python.org/downloads/release/python-396/)
2. Pip installieren [Dokumentation](https://pip.pypa.io/en/stable/installation/)
3. Empfohlen: Pipenv installieren [Dokumentation](https://pipenv.pypa.io/en/latest/)

### 1. Empfohlen: Automatisch mit pipenv

Das Ausführen des Befehls

```{Bash}
pipenv sync
```

installiert die von uns bei der Entwicklung verwendete Version der benoetigten Pakete automatisch. Wenn Sie von allen Paketen die neueste Version verwenden wollen, nutzen Sie stattdessen pipenv install.  
Verwendung auf eigene Gefahr!

Zu letzt muessen wir die virtuelle Umgebung aktivieren. Wenn Sie pipenv verwenden, reicht ein einfaches

```{Bash]}
pipenv shell
```

wonach Sie sich in einer neuen, virtuellen shell wiederfinden.  

> **Achtung!** diesen letzten Schritt müssen Sie jedes mal ausführen, bevor Sie den Notebook-Server starten.

### 2. Manuell mit venv + pip

Der Python Interpreter selbst bietet die Möglichkeit, eine virtuelle Python Umgebung zu erstellen. Allerdings muss hierbei schon die richtige Python Version verwendet werden (anders als mit pipenv).

Alle folgenden Befehle sollten im Oberordner des Repository ausgeführt werden (Ebene dieser Readme.md).

Ein neues Virtual Environment im lokalen Ordner erzeugen Sie mit

```{Bash}
python -m venv <./venvname>
```

Als naechstes muss dieses nun aktiviert werden. Dies muss in jeder neuen Shell erneut ausgeführt werden.

```{Bash}
./venvname/Scripts/activate.py
```

Genaueres finden Sie in der [offiziellen Dokumentation zu venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Anschließend kümmern wir uns um die für unseren Workshop benötigten Pakete. Diese sind in der [Requirements-Datei](requirements.txt) direkt fuer pip lesbar aufgelistet.

```{Bash}
pip install -r requirements.txt
```


## Starten der Notebook-Server
Das gesamte Kursmaterial ist in sogennanten (jupyter) "notebooks" erstellt worden. Dies ist ein gemischtes Dateiformat, in welchem Code, Strukturierter Text (Markdown) und Mathematische Formeln nebeneinander dargestellt und ausgefuehrt werden koennen.  
Dieses Format wird mittlerweile weitlaeufig in verschiedenen IDEs unterstuetzt.  

Das ausfuehren von
```
jupyter-lab
```
startet eine Weboberflaeche, die einer IDE aehnelt, jedoch auf o.g. Notebook-Format spezialisiert ist. Notebooks koennen dort in eigenen Tabs geoeffnet werden.  

Alternativ steht auch noch die urspruengliche Standalone-Anwendung zur Verfuegung, welche etwas simpler aufgebaut ist.  
Die wird gestartet mit
```
jupyter-notebook
```
und ist in der Regel ausreichend fuer diesen Workshop.

> **Achtung!** Zum aktuellen Zeitpunkt scheint diese zumindest fuer den ersten Teil des Workshops 00_Introduction_Setup noch notwendig zu sein, da dort ein spezielles interaktives Slide-Format verwendet wird, welches scheinbar in jupyter-lab noch nicht unterstuetzt wird.
