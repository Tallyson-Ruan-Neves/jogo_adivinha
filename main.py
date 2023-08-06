#Tallyson-Ruan-Neves

try:
  import random
  
  num = random.randint(0,100)
  print("_"*4+"Jogo de adivinhaçao"+"_"*4)
  
  ganhou = False 
  while not ganhou:
    num_chute = int(input("Chute um valor entre [0, 100]: "))
    if num == num_chute:
      print(f"Voçe ganhou o numero era {num}!")
      ganhou = True

    elif num > num_chute:
      print("Errrado, mais!")
      
    elif num < num_chute:
      print("Errrado, menos!")

except:
  
  print("Nao foi possivel executar o JOGO!")
