import re
import wave
import pyaudio


class TextToSpeech:
    """
    Преобразование текста в звуки на английском языке
    """

    def __init__(self, words_pronunciation_dictionary: str = "cmudict-0.7b.txt"):
        """
        Инициализация класса
        :param words_pronunciation_dictionary:  словарь произношений слов
        """
        self.lines = {}
        self.load_words(words_pronunciation_dictionary)

    def load_words(self, words_pronunciation_dictionary: str):
        """
        Загрузка слов из файла словаря
        :param words_pronunciation_dictionary: словарь произношений слов
        :return: строки со словами из файла(найденные через регулярное выражение)
        """
        with open(words_pronunciation_dictionary, "r") as file:
            for line in file:
                if not line.startswith(";;;"):
                    key, value = line.split("  ", 2)
                    self.lines[key] = re.findall(r"[A-Z]+", value)

    def get_pronunciation(self, str_input):
        """
        Получение произношения введённого пользователем слова или фразы на английском языке
        :param str_input: введённое слово или фраза
        """
        pronunciation_list = []
        for word in re.findall(r"[\w']+", str_input.upper()):
            if word in self.lines:
                pronunciation_list += self.lines[word]
        print(pronunciation_list)

        if len(pronunciation_list)>0:
            self.generate_wav_data(pronunciation_list)

    def generate_wav_data(self, pronunciation_list):
        """
        Генерация аудио-файла из звуков, требуемых для произношения слова
        :param pronunciation_list: список звуков, которые должны быть произнесены
        """
        with wave.open("generated.wav", "wb") as wav_out:
            for pronunciation in pronunciation_list:
                with wave.open("sounds/" + pronunciation + ".wav", "rb") as wav_in:
                    if not wav_out.getnframes():
                        wav_out.setparams(wav_in.getparams())
                    wav_out.writeframes(wav_in.readframes(wav_in.getnframes()))
        self.play_audio_file("generated.wav")

    def play_audio_file(self, file_name):
        """
        Проигрывание сгенерированного аудио-файла
        :param file_name: название сгенерированного файла
        """
        try:
            wave_audio_file = wave.open(file_name, "rb")
            data = wave_audio_file.readframes(wave_audio_file.getnframes())

            audio = pyaudio.PyAudio()
            stream = audio.open(format=audio.get_format_from_width(wave_audio_file.getsampwidth()),
                                channels=wave_audio_file.getnchannels(),
                                rate=wave_audio_file.getframerate(),
                                output=True)

            if len(data) > 0:
                stream.write(data)

            stream.stop_stream()
            stream.close()
            audio.terminate()
            return
        except:
            pass


if __name__ == "__main__":
    tts = TextToSpeech()
    while True:
        tts.get_pronunciation(input("Enter a word or phrase: "))
