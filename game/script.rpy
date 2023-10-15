init python:
    renpy.music.register_channel("bgs", "sfx", loop = True)

#Смерть персонажей
define sasha_die = False
define yura_die = False
define you_die = False
    
#Персонажи, их имена и цвета диалога
define v = Character('Влада', color="#ff7801ff", image="girl")
define s = Character('Саша', color="#19dcff", image="girl2")
define y = Character('Юра', color="#05e705", image="boy")

#Переменая для удобной позиции
init:
    $ left2 = Position(xalign=0.3)
    $ right2 = Position(xalign=0.7)


#Игра начинается здесь
label start:
    scene bg lab
    with fade

    show boy shock

    y "О нет, моя младшая сестра пропала"

    show girl sad at right2
    with moveinright

    v "О нет, это плохо!"

    show girl2 sad at left2
    with moveinleft

    s "Нельзя терять ни минуты и найти её!"

    menu:
        "Мне страшно, стоит ли делать это?"

        "Дождаться ответа полиции":
            jump stay_to_wait_for_the_police_response

        "Пойти искать младшую сестру":
            jump go_search


    return
#Решают дождаться полиции
label stay_to_wait_for_the_police_response:

    y "Мы не сможем, это опасно."

    v "Ладно, мы дождёмся ответа от полиции"

    return
#Решаются искать
label go_search:
    
    s "Нет, мы не можем оставить всё так! {w} Мы идём её искать!"

    v "Ладно, попробуем найти её."

    jump park

    return
#Действие в парке
label park:
    scene bg forest

    show boy shock
    show girl sad at right2
    show girl2 sad at left2

    v "Вот это нас занесло"

    s "Лучше держаться от туда подальше!"

    y "..."

    s "Аккуратнее!"

    menu:
        "Стоит послушаться Сашу?"

        "Прислушаться к Саше":
            "Саша жива"

        "Проигнорировать Сашу":
            "Саша умерла"
            $ sasha_die = True
        
    jump building

    return
#Действие в здании
label building:
    scene bg corridor

    if sasha_die:
        show boy shock
        show girl sad at right2
        v "Боже мой, как такое могло случиться..."
        y "Дыши, если будем держаться вместе то сможем выйти от сюда"
    else:
        show boy shock
        show girl sad at right2
        show girl2 sad at left2

        v "Саша, ты дура!"
        s "Да ладно, я же выжила"
        y "Сейчас нам главное держаться вместе"

    menu:
        "Стоит послушаться Юру?"

        "Прислушаться к Юра":
            "Юра жив"

        "Проигнорировать Юру":
            "Юра умер"
            $ yura_die = True


    jump storage

    return
#Действие в кладовке
label storage:
    scene bg room3 lamp

    show boy shock
    show girl sad at right2
    show girl2 sad at left2

    if sasha_die:
        if yura_die: 
            v "О нет, я осталась совершенно одна"
        else: 
            v "Как хорошо что ты выжил!"
            y "Ага, это хорошо"
    else:
        if yura_die: 
            v "О нет, я мы потеряли Юру..."
            y "Это ужасно!"
        else: 
            v "Как хорошо что мы выжили!"
            y "Ага, это хорошо"
            s "Фуууух."

    menu:
        "Стоит послушаться себя?"

        "Прислушаться к себе":
            "Ты жива"

        "Проигнорировать себя":
            "Ты умерла"
            $ you_die = True

    return
# Концовка где все живы
# Концовка где умерла только Саша
# КОонцовка где умер только Юра
# Концовка где умерла только Влада
# Концовка где умерли все

 