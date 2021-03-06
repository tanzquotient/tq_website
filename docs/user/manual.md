# Anleitung zur TQ-Webseite
## Grundlegendes

Die Bedienung der Website ist grundsätzlich in zwei Bereiche aufgeteilt:

* *Frontend*: Dies ist öffentlich zugänglich und somit für beliebige Nutzer des Internets abrufbar. TQ Kunden und Mitarbeiter im Verein können sich einloggen und sehen je nach dem mehr Informationen, die auf sie zugeschnitten sind. Zum Beispiel sieht ein Tanzschüler seine besuchten Kurse oder ein Tanzlehrer die Kurse, die er gerade unterrichtet. (Noch nicht implementiert)
* *Backend*: Das Backend ist nur für eingeloggte Benutzer sichtbar und nur Mitglieder des Vereins können es sehen. (Es kann genau gesteuert werden wer was sieht). Grobe Anleitung zum verwendeten CMS gibts [hier](https://django-cms.readthedocs.org/en/support-3.0.x/user/reference/page_admin.html). Das Backend ist nicht immer supereinfach zu bediehnen, dafür ist es extrem schnell erweiterbar. Das heisst wenn dir ein Feld fehlt bei irgendeinem Eintrag, zögere nicht diesen Wunsch zu äussern, es ist eine Sache von Minuten (wirklich!) das zu ändern. Am Besten du trägst den Wunsch gleich im [Bug tracking System](https://github.com/gitsimon/tq_website/issues) ein.

## Datenmodell

Bei der Arbeit im Backend, dass heisst bei der Kursverwaltung, dem Eintragen von Events etc. hilft es ungemein, die Struktur der Daten grob zu verstehen. Die Struktur der Daten ist *nicht* zwingend so wie es auf der Webseite dargestellt wird, aber so wie es Sinn macht die Daten zu organisieren, dass man möglich selten Daten kopieren muss.

Nachfolgend werden die einzelnen Modelle(=Tabellen) erläutert, sortiert nach Aufgabenbereich.

### Kursadministration

Für dich als Kursadministrator sind die folgenden Modelle wichtig:

* *Offerings*: Ein Offering beinhaltet alle Kurse, die in einer Zeitspanne angeboten werden, meistens ist eine Zeitspanne ein Quartal eines Semesters. Ein Offering wird immer als ganzes auf der Webseite angezeigt, aber du kannst entscheiden, wann es soweit zusammengestellt ist, dass es auf der Webseite angezeigt werden soll (und die darin enthaltenen Kurse zur Anmeldung offenstehen).
Ein Offering definiert auch die Zeitspanne (des Quartals) und der darin enthaltenen Kurse. Für einzelne Kurse kann die Zeitspanne aber auch überschrieben werden (wenn ein Kurs z.B. früher endet).
* *Courses*: Ein Course ist ein Kurs in einer bestimmten Zeitspanne, für den man sich anmelden kann. Er definiert Zeit, Ort und Typ des Kurses. Der Typ wird jedoch separat verwaltet, weil immer wieder Kurse vom gleichen Typ durchgeführt werden.
* *Course Types*: Ein Course Type ist der Typ eines Kurses. Er enthält die (statischen) Information die sich von einer Durchführung eines Kurses zur nächsten nicht ändern. So enthält er etwa die Tanzstile die unterrichtet werden und eine generelle Beschreibung.
* *Rooms*: Hier verwaltet man die Räume und ihre Beschreibung sowie den Link zur Karte (z.B. Google Maps).
* *Styles*: Hier verwaltet man die Tanzstile, die in der Beschreibung der *Course Types* aufgelistet werden können. Insbesondere können hier auch passende Songs eingetragen werden. Die Songs werden auf der Detailansicht des Kurses angezeigt aber auch auf der [Seite mit der Musikzusammenstellung](//tanzquotient.org/courses/music/) aller Tanzstilen!

Generell ist wichtig zu verstehen, dass Daten an mehreren Orten editiert werden können. Zum Beispiel kann man in *Subscribes* die Anmeldungen verwalten. Mann kann teile davon aber auch sehen, wenn man einen Kurs editiert (nämlich alle Anmeldungen für diesen bestimmten Kurs) oder wenn man einen User editiert (nämlich alle Anmeldungen dieses Users).

### Eventadministration

TODO
