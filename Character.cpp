#include "Character.h"

// Конструктор класу Character
Character::Character() {
    distanceTravelled = 0;

    gold = 0;

    name = "NONE";
    level = 0;
    exp = 0;
    expNext = 0;

    strength = 0;
    agility = 0;
    intelligence = 0;

    hp = 0;
    hpMax = 0;
    stamina = 0;
    staminaMax = 0;
    damageMin = 0;
    damageMax = 0;
    defence = 0;
    accuracy = 0;

    statPoints = 0;
}

// Перевантажений конструктор класу Character
Character::Character(string name,
                     int distanceTravelled,
                     int gold,
                     int level,
                     int exp,
                     int strength, int agility, int intelligence,
                     int hp, int stamina,
                     int statPoints) {
    this->distanceTravelled = distanceTravelled;

    this->gold = gold;

    this->name = name;
    this->level = level;
    this->exp = exp;

    this->strength = strength;
    this->agility = agility;
    this->intelligence = intelligence;

    this->hp = hp;
    this->stamina = stamina;

    this->statPoints = statPoints;

    this->updateStats();
}

// Деструктор класу Character
Character::~Character() {

}

// Метод ініціалізації персонажа
void Character::initialize(const string name){
    distanceTravelled = 0;

    gold = 100;

    this->name = name;
    level = 1;
    exp = 0;

    strength = 5;
    agility = 5;
    intelligence = 5;

    updateStats();

    hp = hpMax;
    stamina = staminaMax;

    statPoints = 0;

}

// Метод виведення інформації про персонажа
string Character::printStats() const {
     return "= Інформація про персонажа =\n"
           "= Ім'я: " + name + "\n"
           + "= Рівень: " + to_string(level) + "\n"
           + "= Досвід: " + to_string(exp) + "\n"
           + "= Досвіду до наступного рівня: " + to_string(expNext) + "\n"
           + "= Невикористані очки атрибутів: " + to_string(statPoints) + "\n"
           + "\n"
           + "= Сила: " + to_string(strength) + "\n"
           + "= Спритність: " + to_string(agility) + "\n"
           + "= Інтелект: " + to_string(intelligence) + "\n"
           + "\n"
           + "= Очки здоров'я: " + to_string(hp) + " / " + to_string(hpMax) + "\n"
           + "= Витривалість: " + to_string(stamina) + " / " + to_string(staminaMax) + "\n"
		   + "= Шкода: " + to_string(damageMin) + " - " + to_string(damageMax) + "\n"
		   + "= Броня: " + to_string(defence)+ "\n"
		   + "= Точність: " + to_string(accuracy) + "\n"
		   + "= Пройдена відстань: " + to_string(distanceTravelled) + "\n"
		   + "= Золото: " + to_string(gold) + "\n";
}

// Метод, який повертає інформацію про персонажа як символьний рядок
string Character::getAsString() const {
    return this->name + " "
		+ to_string(distanceTravelled) + " "
		+ to_string(gold) + " "
		+ to_string(level) + " "
		+ to_string(exp) + " "
		+ to_string(strength) + " "
		+ to_string(agility) + " "
		+ to_string(intelligence) + " "
		+ to_string(hp) + " "
		+ to_string(stamina) + " "
		+ to_string(statPoints) + " ";
}

// Метод підняття рівня персонажа
int Character::levelUp() {
    int prevlevel = level;
    while (exp >= expNext) {
        exp -= expNext;
        level++;
        statPoints++;
        updateStats();
    }
    if(prevlevel!=level){
        return 1;
    }
    else return 0;
}

// Метод оновлення характеристик персонажа
void Character::updateStats() {
    expNext = level*50;

    hpMax = 3 * strength;
    staminaMax = 2 * agility;
    damageMin = (strength + agility + intelligence)/3;
    damageMax = (strength + agility + intelligence)/3 + strength/2;
    defence = strength / 2 + intelligence / 2;
    accuracy = intelligence;

    hp = hpMax;
}

// Метод використання очків атрибутів
void Character::useStatPoint(int statpoint) {
    if (statpoint==1){
        strength++;
        statPoints--;
    }
    else if (statpoint==2){
        agility++;
        statPoints--;
    }
    else if (statpoint==3){
        intelligence++;
        statPoints--;
    }

    updateStats();
}

// Метод для відновлення здоров'я персонажа
void Character::heal() {
    hp = hpMax;
    payGold(50);
}

// Метод для відновлення витривалості персонажа
void Character::rest() {
    stamina = staminaMax;
    payGold(20);
}

// Метод для збільшення очків атрибутів персонажа на 1
void Character::upgrade() {
    statPoints+=1;
    payGold(100);
}
