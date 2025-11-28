# Question
class Question():
    def __init__(self, text, choices, answer):  # Soru nesnesi oluşturulurken çalışır (constructor)
        self.text = text  # Sorunun kendisi (metin)
        self.choices = choices  # Cevap şıkları listesi
        self.answer = answer  # Doğru cevap
    def checkanswer(self, answer):  # Verilen cevabın doğru olup olmadığını kontrol eder
        return self.answer == answer  # Doğruysa True, yanlışsa False döner
  
# Quiz
class Quiz:
    def __init__(self,questions):  # Quiz nesnesi oluşturulurken çalışır
        self.questions = questions  # Tüm soruların listesi
        self.score = 0  # Başlangıç puanı 0
        self.questionsIndex  = 0  # Hangi sorudayız? (ilk soru = 0)
    def getQuestion(self):  # Şu anki soruyu getirir
        return self.questions[self.questionsIndex]  # Index numarasına göre soruyu döndürür
    
    def displayQuestion(self):  # Soruyu ekrana yazdırır ve cevap alır
        question = self.getQuestion()  # Şu anki soruyu al
        print (f'soru {self.questionsIndex + 1}: {question.text}')  # Soru numarası ve metni yazdır (+1 çünkü index 0'dan başlar)
        for q in question.choices:  # Her şıkkı döngüyle yazdır
            print('-' + q)  # Şık başına - işareti koyarak yazdır

        answer = input('cevap: ')  # Kullanıcıdan cevap al
        self.guess(answer)  # Cevabı kontrol et
        self.loadQuestion()  # Bir sonraki soruya geç
 
    def guess(self, answer):  # Kullanıcının verdiği cevabı değerlendirir
        question = self.getQuestion()  # Şu anki soruyu al
        if question.checkanswer(answer):  # Eğer cevap doğruysa
            self.score += 1  # Puanı 1 artır
        self.questionsIndex += 1  # Soru index'ini 1 artır (bir sonraki soruya geç)


    def loadQuestion(self):  # Sıradaki soruyu yükler veya quiz'i bitirir
        if len(self.questions) == self.questionsIndex:  # Eğer tüm sorular bittiyse
            self.showscore()  # Skoru göster
        else:  # Hala sorular varsa
            self.displayProgress()  # İlerlemeyi göster (kaçıncı soru)
            self.displayQuestion()  # Soruyu göster

    def showscore(self):  # Quiz bittiğinde skoru gösterir
        print('score: ', self.score)  # Toplam puanı yazdır
    

    def displayProgress(self):  # Kaçıncı soruda olduğumuzu gösterir
        totalQuestion = len(self.questions)  # Toplam soru sayısı
        questionNumber = self.questionsIndex + 1  # Şu anki soru numarası (index 0'dan başladığı için +1)
        if questionNumber > totalQuestion:  # Eğer soru numarası toplam sorudan fazlaysa
            print('quiz bitti')  # Quiz bittiğini yaz
        else:  # Değilse
            print(f'question {questionNumber} of {totalQuestion}'.center(100,'*' ))  # "question 1 of 5" şeklinde ortada yıldızlarla göster
            
q1 = Question('en iyi programlama dili hangisidir', ['c#', 'python', 'javascript', 'java'],'python')  # 1. soruyu oluştur
q2 = Question('en popüler programlama dili hangisidir', ['python', 'javascript', 'c#','java'],'python')  # 2. soruyu oluştur
q3 = Question('en cok kazandiran programlama dili hangisidir', ['c#', 'javascript', 'java','python',],'python')  # 3. soruyu oluştur
q4 = Question('en cok sevvilen programlama dili hangisidir', ['c#', 'javascript', 'java','python',],'python')  # 4. soruyu oluştur
q5 = Question('en kolay programlama dili hangisidir', ['c#', 'javascript', 'java','python',],'python')  # 5. soruyu oluştur
question = [q1,q2,q3,q4,q5]  # Tüm soruları bir liste içine koy
quiz = Quiz(question)  # Quiz nesnesini oluştur (5 sorulu)
quiz.loadQuestion()  # Quiz'i başlat (ilk soruyu göster)