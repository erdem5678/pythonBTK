# Question
class Question():
    def __init__(self, text, choices, answer):  # Soru nesnesi oluşturulurken çalışır (constructor)
        self.text = text  # Sorunun kendisi (metin)
        self.choices = choices  # Cevap şıkları listesi
        self.answer = answer  # Doğru cevap


# Verilen cevabın doğru olup olmadığını kontrol eder
    def checkanswer(self, answer):
        return self.answer == answer  # Doğruysa True, yanlışsa False döner
  
# Quiz
class Quiz:
    def __init__(self,questions):  # Quiz nesnesi oluşturulurken çalışır
        self.questions = questions  # Tüm soruların listesi
        self.score = 0  # Başlangıç puanı 0
        self.questionsIndex  = 0  # Hangi sorudayız? (ilk soru = 0)



 # Şu anki soruyu getirir
    def getQuestion(self):  
        return self.questions[self.questionsIndex]  # Index numarasına göre soruyu döndürür
    


# Soruyu ekrana yazdırır ve cevap alır 
    def displayQuestion(self):  # Soruyu ekrana yazdırır ve cevap alır
        question = self.getQuestion()  # Şu anki soruyu al
        print (f'soru {self.questionsIndex + 1}: {question.text}')  # Soru numarası ve metni yazdır (+1 çünkü index 0'dan başlar)
        for q in question.choices:  # Her şıkkı döngüyle yazdır
            print('-' + q)  # Şık başına - işareti koyarak yazdır

        answer = input('cevap: ')  # Kullanıcıdan cevap al
        self.guess(answer)  # Cevabı kontrol et
        self.loadQuestion()  # Bir sonraki soruya geç


# Kullanıcının verdiği cevabı değerlendirir
    def guess(self, answer):
        question = self.getQuestion()  # Şu anki soruyu al
        if question.checkanswer(answer):  # Eğer cevap doğruysa
            self.score += 1  # Puanı 1 artır
        self.questionsIndex += 1  # Soru index'ini 1 artır (bir sonraki soruya geç)


 # Sıradaki soruyu yükler veya quiz'i bitirir
    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:  # Eğer tüm sorular bittiyse
            self.showscore()  # Skoru göster
        else:  # Hala sorular varsa
            self.displayProgress()  # İlerlemeyi göster (kaçıncı soru)
            self.displayQuestion()  # Soruyu göster


 # Quiz bittiğinde skoru gösterir
    def showscore(self): 
        print('score: ', self.score)  # Toplam puanı yazdır
    

# Kaçıncı soruda olduğumuzu gösterir
    def displayProgress(self):
        totalQuestion = len(self.questions)  # Toplam soru sayısı
        questionNumber = self.questionsIndex + 1  # Şu anki soru numarası (index 0'dan başladığı için +1)
        if questionNumber > totalQuestion:  # Eğer soru numarası toplam sorudan fazlaysa
            print('quiz bitti')  # Quiz bittiğini yaz
        else:  # Değilse
            print(f'question {questionNumber} of {totalQuestion}'.center(100,'*' ))  # "question 1 of 5" şeklinde ortada yıldızlarla göster

            
# Ekrana çıktı verme - Nesnelerin özelliklerini ve metodlarını test etme
# Output to the screen - Testing the properties and methods of objects
q1 = Question('en iyi programlama dili hangisidir', ['c#', 'python', 'javascript', 'java'],'python') 
q2 = Question('en popüler programlama dili hangisidir', ['python', 'javascript', 'c#','java'],'python') 
q3 = Question('en cok kazandiran programlama dili hangisidir', ['c#', 'javascript', 'java','python',],'python') 
q4 = Question('en cok sevvilen programlama dili hangisidir', ['c#', 'javascript', 'java','python',],'python')  
q5 = Question('en kolay programlama dili hangisidir', ['c#', 'javascript', 'java','python',],'python')  

question = [q1,q2,q3,q4,q5]  # Tüm soruları bir liste içine koy
quiz = Quiz(question)  # Quiz nesnesini oluştur (5 sorulu)
quiz.loadQuestion()  # Quiz'i başlat (ilk soruyu göster)