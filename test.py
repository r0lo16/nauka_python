import random

class Program:
    print("Witaj w programie")
    wylosuj = []
    def losowanie(self):
        
        
        for i in range(10):
            i = random.randint(0,100)
            self.wylosuj.append(int(i))

        print(f"Towje liczby:{self.wylosuj}")

    def otworz(self):
        dane_losowanie = self.wylosuj
        with open('plik.txt', 'w') as plik:
            plik.write(str(dane_losowanie))

    def pobieranie(self):
     
         with open('plik.txt', 'r') as f:
            for line in f:
                line = line.strip('[\n]')  # usuń białe znaki i otwarcie nawiasu klamrowego na początku linii
                numbers = line.strip().split(',')  # usuń białe znaki i rozdziel string na listę stringów, używając przecinka jako separatora
                self.int_numbers = [int(num) for num in numbers]  # utwórz listę liczb całkowitych, używając list comprehension i funkcji int()
                print(self.int_numbers)  # wydrukuj listę liczb całkowitych 

                # for num in numbers:
                #     if int(num) % 2 == 0:  # sprawdź, czy liczba jest podzielna przez 2
                #         print(num)
    def srednia(self):
        pary = []
        for num in self.int_numbers:
            if int(num) % 2 == 0:
                pary.append(int(num))
        print(pary)        
        parzyste = sum(pary)/len(pary)
        print(parzyste)
      
                        
                    
p1=Program()
p1.losowanie()
p1.otworz()
p1.pobieranie()
p1.srednia()



