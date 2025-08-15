import json
import os

data= "TrackerOfHabits1.json"
def LOHRead():
    with open(data,"r", encoding="utf-8") as f:
        listofhabits=json.load(f)
        return listofhabits
def intinputvalidator(a):
    while True:
        try:
            b=int(a)
            return b   
        except ValueError:
            a=input("Вводите только номер привычки:")
            continue 
def LOHWrite(habit):
    with open(data,"w",encoding="utf-8") as f:
        json.dump(habit,f,ensure_ascii=False)
        return (print("Информация в сохранении успешно обновлена"))
# def retry():думал сделать отдельный ретрай на основе цикла но оставил просто через while
      
if not os.path.exists(data):
    with open(data,"w",encoding="utf-8") as f:
        json.dump({},f,ensure_ascii=False)

print("Добро пожаловать в трекер привычек!")
while True:
    print()
    print("Введите цифры чтоб выбрать функцию \n1.добавить привычку \n2.удалить привычку \n3.посмотреть список привычек \n4.выйти")
    while True:
        try:
            a=int(input("Введите номер функции:"))
            if a>4 or a<1:
                print("Вводите только номер функции")
                continue
            break
        except ValueError:
            print ("Вводите только номер функции")
    if a==1:
        b=input("1.Добавить привычку \nНазовите привычку:")
        listofhabit=LOHRead()
        if listofhabit:
            l=max(map(int,listofhabit.keys()))+1
            listofhabit[str(l)]=b.capitalize()
            
            with open(data,"w", encoding="utf-8") as f:
                json.dump(listofhabit, f, ensure_ascii=False)
                print(f'Привычка {listofhabit[str(l)]} успешно добавлена.')
        else:
            l=1
            listofhabit[str(l)]=b.capitalize()
            
            with open(data,"w", encoding="utf-8") as f:
                json.dump(listofhabit, f, ensure_ascii=False)
                print(f'Привычка {listofhabit[str(l)]} успешно добавлена.')
    elif a==2:
        print("2.Удалить привычку\n")
        listofhabits=LOHRead()
        if listofhabits:
            print("Все привычки:\n","\n".join(f"{k}.{v}" for k,v in listofhabits.items()),sep="")
            c=input("\nВведите номер привычки которую удалить:")
            c=intinputvalidator(c)
            try:
                print(listofhabits[str(c)],"будет удалено")
                del listofhabits[str(c)]
                keys=sorted(listofhabits.keys(),key=int)
                for k in keys:
                    if c<int(k):
                        listofhabits[int(k)-1]=listofhabits.pop(str(k))
                LOHWrite(listofhabits)
                
            except KeyError:
                print("Привычки под таким номером не существует")
        else:
            print('У вас нет записанных привычек.')
         
    elif a==3:
        with open(data,"r",encoding="utf-8") as f:
            b=json.load(f)
        if b:
            print("Список привычек:")
            print("\n".join(f"{k}.{v}" for k,v in b.items()))
        else:
            print('У вас нет записанных привычек.')
            
    elif a==4:
        print("Выход...")
        break
# в 8/14/2025 придумать что-то чтобы когда удалял одну привычку, все превычки с ключем выше автоматом падали вниз на 1 ключ
# еще надо доделать нормально вторую кнопкну   


