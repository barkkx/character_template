from jinja2 import Environment, FileSystemLoader, select_autoescape
import random
import os
import shutil


CLASSES_BASE = {
    "wizard" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : 15,
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3),
        "skills" : [
            "Огненный шар",
            "Ледяная стрела",
            "Электрический разряд",
            "Магический щит",
            "Телепортация",
            "Молния небес",
            "Кислотный туман",
            "Психический удар"
        ]
    },
    "warrior" : {
        "strength" : 15,
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3),
        "skills" : [
            "Мощный удар",
            "Размашистый взмах",
            "Бросок топора",
            "Щитовой удар",
            "Вихрь клинков",
            "Пронзающий удар",
            "Военный клич",
            "Землетрясение"
        ]
    },
 
    "hunter" : {
        "strength" : random.randint(1,3),
        "agility" : 15,
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : random.randint(1,3),
        "skills" : [
            "Меткий выстрел",
            "Зов природы",
            "Кровавая рана",
            "Стальной капкан",
            "Призыв ястреба",
            "Дезориентирующий выстрел",
            "Укус виверны",
            "Маскировка в листве"
        ]
    },
    "assasin" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : 15,
        "temper" : random.randint(1,3),
        "skills" : [
            "Смертельный удар",
            "Незаметное приближение",
            "Ядовитый клинок",
            "Теневой клинок",
            "Внезапное исчезновение",
            "Мгновенный бросок",
            "Глушащий удар",
            "Фантомный шаг"
        ]
    },
    "bard" : {
        "strength" : random.randint(1,3),
        "agility" : random.randint(1,3),
        "intelligence" : random.randint(1,3),
        "luck" : random.randint(1,3),
        "temper" : 15,
        "skills" :  [
            "Стремительный прыжок",
            "Электрический выстрел",
            "Ледяной удар",
            "Стремительный удар",
            "Кислотный взгляд",
            "Тайный побег",
            "Ледяной выстрел",
            "Огненный заряд"
        ]
    }
}

def main():
    folder_name = "characters"

    if os.path.exists(folder_name):
          shutil.rmtree(folder_name)
    os.mkdir(folder_name)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('template.html')
    races = ["Человек", "Эльф", "Гном"]
    classes = ["wizard", "warrior", "hunter", "assasin", "bard"]
    number_cards = int(input('Сколько будет карточек(ответ цифрой): '))
    for i in range(number_cards):
        character_name = input("Введите имя: ").strip()
        character_race = input(f"Введите рассу ({", ".join(races)}): ").strip()
        character_class = input(f"Введите класс ({", ".join(classes)}): ").strip().lower()
        skills = random.sample(CLASSES_BASE[character_class]['skills'], 3)
        rendered_page = template.render(
                    image = f"../images/{character_class}.png",
                    name = character_name,
                    race = character_race,
                    character_class = character_class,
                    strength = CLASSES_BASE[character_class]["strength"],
                    agility = CLASSES_BASE[character_class]["agility"],
                    intelligence = CLASSES_BASE[character_class]["intelligence"],
                    luck = CLASSES_BASE[character_class]["luck"],
                    temper = CLASSES_BASE[character_class]["temper"],
                    first_skill = skills[0],
                    second_skill = skills[1],
                    third_skill = skills[2]
        )

        with open(f'{folder_name}/index_{character_class}_{i+1}.html', 'w', encoding="utf8") as file:
                    file.write(rendered_page)


if __name__ == "__main__":
    main()