# winget x Upgrade GUI
![GitHub](https://img.shields.io/github/license/Mr-Robot-ops/winget-x)

![image](https://github.com/Mr-Robot-ops/winget-x/assets/55334802/d3594c97-e423-4b86-80a1-1fa808ad492d)

## Beschreibung

Die **winget x Upgrade GUI** ist ein benutzerfreundliches grafisches Tool für Windows, mit dem Sie Windows-Anwendungen mithilfe von Windows Package Manager (winget) aktualisieren können. Das Tool bietet eine einfach zu bedienende Benutzeroberfläche zum Anzeigen und Aktualisieren von verfügbaren Anwendungsaktualisierungen.

## Installation

1. **Voraussetzungen**: Stellen Sie sicher, dass Sie Windows Package Manager (winget) und Python auf Ihrem System installiert haben.

Wichtiger Hinweis: Das Skript funktioniert nur, wenn Sie winget bereits in einer Eingabeaufforderung geöffnet und die "Nutzungsbedingungen" akzeptiert haben!

```
C:\WINDOWS\system32>winget upgrade
Die Quelle "msstore" erfordert, dass Sie die folgenden Vereinbarungen vor der Verwendung anzeigen.
Terms of Transaction: https://aka.ms/microsoft-store-terms-of-transaction
Die Quelle erfordert, dass die geografische Region des aktuellen Computers aus 2 Buchstaben an den Back-End-Dienst gesendet wird, damit er ordnungsgemäß funktioniert (z. B. „US“).

Stimmen Sie allen Nutzungsbedingungen der Quelle zu?
[Y] Ja  [N] Nein:
```

```
winget
```
```
python --version
```
[Offizielle Python Download Seite](https://www.python.org/downloads/windows/)

3. **Herunterladen des Tools**: Laden Sie die neueste Version des Tools von [GitHub Releases](https://github.com/Mr-Robot-ops/winget-x/releases/tag/Upgrade_GUI_2.3) herunter.

4. **Entpacken**: Entpacken Sie das heruntergeladene Archiv an den gewünschten Speicherort auf Ihrem Computer.

5. **Ausführen**: Starten Sie das Script mit Python (`Wintget_x_Upgrade_GUI_Version_x.x.py`), um das Tool zu benutzen.

6. Installieren Sie ggf. die benötigten Module nach.
- Windows+R
- cmd eingeben
- STRG+Shift+Enter um die Eingabeaufforderung als Administrator zu starten. Anschließend ggf. das fehlende Modul installieren.

```
py -m pip install Pillow
```

## Verwendung

1. Starten Sie das Tool, und klicken Sie auf die Schaltfläche "Aktualisierbare Anwendung auflisten" um eine Liste der aktualisierbaren Anwendungen anzuzeigen.

2. Wählen Sie die gewünschten Anwendungen aus der Liste aus. Halten Sie die Umschalttaste (Shift) gedrückt, um mehrere Anwendungen auszuwählen. Wenn Sie die Auswahl einzelner Anwendungen aufheben möchten, halten Sie die STRG-Taste gedrückt und klicken Sie auf die Anwendung, die Sie hinzufügen oder deren Auswahl aufheben möchten.

3. Klicken Sie auf die Schaltfläche "Ausgewählte Anwendungen aktualisieren", um die ausgewählten Anwendungen zu aktualisieren.

4. Die Ergebnisse werden im Tool angezeigt, einschließlich erfolgreicher oder fehlgeschlagener Aktualisierungen.

5. Um die Anwendungen alphabetisch zu sortieren klicken Sie auf die Spalte "Name".

6. Mit der rechten Maustaste können Sie ein Kontextmenu öffnen und zwischen 4 Farben wählen.

![x_gif](https://github.com/Mr-Robot-ops/winget-x/assets/55334802/45560489-e696-4835-bc82-3b8a054a42e5)

## Beitrag

Wenn Sie zu diesem Projekt beitragen möchten, können Sie gerne Pull Requests erstellen oder Fehler melden. Wir begrüßen Ihre Hilfe und Ihr Feedback!

## Lizenz

Dieses Projekt ist unter der [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/) lizenziert.

## Autor

*Mr-Robot-ops* - [GitHub](https://github.com/Mr-Robot-ops)

## Kontakt

Sie können mich über GitHub kontaktieren oder Discord: iluckyduck
