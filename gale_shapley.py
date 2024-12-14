from collections import deque

def gale_shapley(men_preferences, women_preferences):
    """
    Реализация алгоритма Гейла-Шепли для задачи построения стабильных бракосочетаний.

    :param men_preferences: Словарь, где ключи — имена мужчин, а значения — списки женщин в порядке предпочтения.
    :param women_preferences: Словарь, где ключи — имена женщин, а значения — словари с ранжированием мужчин.
    :return: Словарь соответствий, где ключи — имена женщин, а значения — имена мужчин.
    """
    # Инициализация всех мужчин как свободных
    free_men = deque(men_preferences.keys())
    
    # Для отслеживания следующей женщины, которую мужчина будет предлагать
    next_proposal = {man: 0 for man in men_preferences}
    
    # Словарь для хранения текущих пар
    engagements = {}
    
    while free_men:
        man = free_men.popleft()
        # Получаем индекс следующей женщины, которую мужчина будет предлагать
        woman_index = next_proposal[man]
        woman = men_preferences[man][woman_index]
        
        print(f"{man} предлагает {woman}")
        
        # Если женщина свободна, связываем их
        if woman not in engagements:
            engagements[woman] = man
            print(f"{woman} принимает предложение от {man}")
        else:
            current_man = engagements[woman]
            # Проверяем, предпочитает ли женщина нового мужчину текущему
            if women_preferences[woman][man] < women_preferences[woman][current_man]:
                engagements[woman] = man
                print(f"{woman} предпочитает {man} вместо {current_man}. {current_man} становится свободным.")
                free_men.append(current_man)
            else:
                print(f"{woman} отклоняет предложение от {man}")
                # Мужчина остаётся свободным и будет предлагать следующую женщину
                free_men.append(man)
        
        # Увеличиваем индекс предложения для мужчины
        next_proposal[man] += 1
    
    return engagements

def prepare_women_preferences(women_pref_list):
    """
    Преобразует предпочтения женщин в словарь рангов для быстрого сравнения.

    :param women_pref_list: Словарь, где ключи — имена женщин, а значения — списки мужчин в порядке предпочтения.
    :return: Словарь, где ключи — имена женщин, а значения — словари с ранжированием мужчин.
    """
    women_preferences = {}
    for woman, prefs in women_pref_list.items():
        women_preferences[woman] = {man: rank for rank, man in enumerate(prefs)}
    return women_preferences

def main():
    # Пример предпочтений
    men_preferences = {
        'Альберт': ['Беатрис', 'Катерина', 'Даниил'],
        'Борис': ['Катерина', 'Даниил', 'Беатрис'],
        'Даниил': ['Катерина', 'Беатрис', 'Альберт']
    }

    women_pref_list = {
        'Беатрис': ['Альберт', 'Борис', 'Даниил'],
        'Катерина': ['Борис', 'Даниил', 'Альберт'],
        'Даниил': ['Даниил', 'Альберт', 'Борис']
    }

    # Подготовка предпочтений женщин
    women_preferences = prepare_women_preferences(women_pref_list)

    # Запуск алгоритма Гейла-Шепли
    stable_matching = gale_shapley(men_preferences, women_preferences)

    print("\nСтабильные соответствия:")
    for woman, man in stable_matching.items():
        print(f"{man} ↔ {woman}")

if __name__ == "__main__":
    main()
