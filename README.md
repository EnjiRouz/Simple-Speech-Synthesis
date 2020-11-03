# Simple Speech Syntesis (Text to Speech)

Это моя первая попытка познакомиться с написанием **простейшего** синтеза речи с нуля.

В качестве словаря произношений для **английского** языка был использован [Carnegie Mellon University Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)

Звуки были записаны самостоятельно с помощью [Audacity](https://www.audacityteam.org/) и могут звучать некорректно (***требуется зависимость от контекста и побольше опыта, но для понимании концепции это уже неплохо***).

Для установки PyAudio можно найти и скачать нужный в зависимости от архитектуры и версии Python whl-файл [здесь](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) в папку с проектом. После чего его можно установить при помощи подобной команды:

`pip install PyAudio-0.2.11-cp38-cp38m-win_amd64.whl`