Questions = [
    ["1. What country has the highest life expectancy ?", "India", "USA", "Hong Kong", "UK", 3],
    ["2. Which is the biggest continent in the world ?", "America", "Asia", "Africa", "UK", 2],
    ["3. Which is longest river in the world ?", "Ganga", "Amazon", "Nile", "Niger", 3],
    ["4. Which is india's first super computer ?", "Param8000", "Param800", "Param80", "param8", 1],
    ["5. Which bank is called bankers bank of india ?", "BOB", "SBI", "ICICI", "RBI", 4],
    ["6. Which is largest animal in the world ?", "Shark", "Blue whale", "Elephant", "Giraff", 2],
    ["7. Which is largest desert in the world ?", "Sahara", "Gobi", "Kalahari", "Tubei", 1],
    ["8. World war I was ended in which year ?", "1917", "1919", "1920", "1918", 4],
    ["9. World war II was ended in which year ?", "1945", "1940", "1947", "1965", 1],
    ["10. What is the capital of karnataka ?", "Mysore", "Hubli", "Bengaluru", "Belguam", 3],
    ["11. What country has the highest life expectancy ?", "India", "USA", "Hong Kong", "UK", 3],
    ["12. Which is the biggest continent in the world ?", "America", "Asia", "Africa", "UK", 2],
    ["13. Which is longest river in the world ?", "Ganga", "Amazon", "Nile", "Niger", 3],
    ["14. Which is india's first super computer ?", "Param8000", "Param800", "Param80", "param8", 1],
    ["15. Which bank is called bankers bank of india ?", "BOB", "SBI", "ICICI", "RBI", 4],
    ["16. Which is largest animal in the world ?", "Shark", "Blue whale", "Elephant", "Giraff", 2],
    ["17. Which is largest desert in the world ?", "Sahara", "Gobi", "Kalahari", "Tubei", 1],
]

levels = [1000,2000,4000,8000,16000,32000,64000,80000,100000,135000,155000,200000,250000,310000,380000,500000,10000000]
money = 0

for i in range(0, len(Questions)):
    Question = Questions[i]
    print(f"\n\n---Question for Rs.{levels[i]}---")
    print(f"A.{Question[1]}       B.{Question[2]}")
    print(f"C.{Question[3]}       D.{Question[4]}")
    replay = int(input("Enter the answer (1 to 4) or 0 to quit : "))
    if(replay == 0):
        money = levels[i-1]
        break
    if(replay == Question[-1]):
        print(f"Correct Answer, You have won Rs.{levels[i]}")
        if(i == 4):
            money = 16000
        elif(i == 9):
            money = 135000
        elif(i == 14):
            money = 380000
    else:
        print("Wrong Answer...!!")
        break
print(f"You take the money Rs.{money}")