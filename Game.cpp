#include "Game.h"

// Конструктор класу Game
Game::Game() {
    fileName = "gamefiles/txt/character/save.txt";
}

// Деструктор класу Game
Game::~Game(){

}

// Метод ініціалізації персонажа
void Game::initGame(const string name){
    character.initialize(name);
}

// Метод виведення інформації про персонажа
string Game::printCharacterSheet() {
    return character.printStats();
}

// Метод збереження персонажа
void Game::saveCharacter() {
    ofstream outFile(fileName);

    if(outFile.is_open()){
        outFile << character.getAsString();
    }

    outFile.close();
}

// Метод завантаження персонажа для продовження ігри за нього
void Game::loadCharacter() {
    ifstream inFile(fileName);

    string name = "";
    int distanceTravelled = 0;
    int gold = 0;
    int level = 0;
    int exp = 0;
    int strength = 0;
    int agility = 0;
    int intelligence = 0;
    int hp = 0;
    int stamina = 0;
    int statPoints = 0;

    string line = "";
    stringstream str;

    if (inFile.is_open())
    {
        while (getline(inFile, line))
        {
            str.str(line);
            str >> name;
            str >> distanceTravelled;
            str >> gold;
            str >> level;
            str >> exp;
            str >> strength;
            str >> agility;
            str >> intelligence;
            str >> hp;
            str >> stamina;
            str >> statPoints;

            Character temp(name, distanceTravelled, gold, level,
                           exp, strength, agility, intelligence,
                           hp, stamina, statPoints);

            character = temp;

            str.clear();
        }
    }

    inFile.close();
}

// Метод подорожування
string Game::Travel() {
    character.travel();
    return event.generateEvent(character);
}

// Метод виведення витривалості персонажа
int Game::getCharacterStamina() {
    return character.getStamina();
}

// Метод введення відповіді на загадку
int Game::inputPuzzleAnswer(int answer) {
    return event.inputPuzzleAnswer(answer);
}

// Метод атаки персонажа у битві
int Game::Attack() {
    return event.attack(character);
}

// Метод атаки противника у битві
int Game::Defend() {
    return event.defend(character);
}

// Метод виведення здоров'я персонажа
int Game::getCharacterHp() {
    return character.getHP();
}

// Метод виведення здоров'я противника
int Game::getEnemyHp() {
    return event.getEnemyHP();
}

// Метод підняття рівня персонажа
int Game::levelUpCharacter() {
    if(character.levelUp()==1){
        return character.getLevel();
    }
    return 0;
}

// Метод виведення невикористаних очків атрибутів
int Game::getCharacterStatPoints() {
    return character.getStatPoints();
}

// Метод використання очків атрибутів
void Game::useCharacterStatPoints(int statpoint) {
    character.useStatPoint(statpoint);
}

// Метод отримання досвіду
int Game::gainExp() {
    int exp = character.getLevel() * (rand()%10 + 1);
    character.gainExp(exp);
    return exp;
}

// Метод отримання золота
int Game::gainGold(int amount) {
    int gold;
    if (amount == -1)
        gold = character.getLevel() * (rand() % 10 + 1);
    else
        gold = amount;

    character.gainGold(gold);
    return gold;
}

// Метод для відновлення здоров'я персонажа
void Game::healCharacter() {
    character.heal();
}

// Метод для відновлення витривалості персонажа
void Game::restCharacter() {
    character.rest();
}

// Метод для збільшення очків атрибутів персонажа на 1
void Game::upgradeCharacter() {
    character.upgrade();
}

// Метод отримання золота
int Game::getCharacterGold() {
    return character.getGold();
}