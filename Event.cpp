#include "Event.h"

// Конструктор класу Event
Event::Event() {

}

// Деструктор класу Event
Event::~Event() {

}

// Метод створення події
string Event::generateEvent(Character& character) {
    int cointoss = rand() % 2;

    switch(cointoss){
        case 0:
            return enemyEncounter(character);
        case 1:
            return puzzleEncounter();
        default:
            break;
    }
}

// Метод виведення інформації про битву
string Event::enemyEncounter(Character& character) {
    enemy = Enemy(character.getLevel() + rand()%3);

    string battle_info;
    string enemy_name;

    int cointoss = rand() % 3 + 1;

    if (cointoss == 1) {
        enemy_name = "троль";
    }
    else if (cointoss == 2) {
        enemy_name = "зомбі";
    }
    else if (cointoss==3) {
        enemy_name = "вампір";
    }

    cointoss = rand() % 2 + 1;

    if (cointoss == 1) {
        battle_info = "Ви побачили, що у вас на шляху стоїть " + enemy_name + " !";
    }
    else if (cointoss==2) {
        battle_info = "На вас біжить злий " + enemy_name + "!";
    }

    return battle_info + "\n\nВведіть 'Атакувати' щоб почати битву...";
}

// Метод атаки персонажа у битві
int Event::attack(Character& character) {
    int combatTotal = enemy.getDefence() + character.getAccuracy();
    int enemyTotal = enemy.getDefence() / (double)combatTotal * 100;
    int playerTotal = character.getAccuracy() / (double)combatTotal * 100;
    int combatRollPlayer = rand() % playerTotal + 1;
    int combatRollEnemy = rand() % enemyTotal + 1;

    if (combatRollPlayer > combatRollEnemy) {
        int damage = character.getDamage();
        this->enemy.takeDamage(damage);
        return damage;
    }
    else return 0;
}

// Метод атаки противника у битві
int Event::defend(Character& character) {
    int combatTotal = character.getDefence() + enemy.getAccuracy();
    int enemyTotal = enemy.getAccuracy() / (double)combatTotal * 100;
    int playerTotal = character.getDefence() / (double)combatTotal * 100;
    int combatRollPlayer = rand() % playerTotal + 1;
    int combatRollEnemy = rand() % enemyTotal + 1;

    if (combatRollPlayer < combatRollEnemy) {
        int damage = enemy.getDamage();
        character.takeDamage(damage);
        return damage;
    }
    else return 0;
}

// Метод виведення загадки
string Event::puzzleEncounter() {
    int cointoss = rand() % 5 + 1;
    puzzleSequenceNumber = cointoss;
    answer_quantity = 0;

    if (cointoss == 1){
        Puzzle puzzle("gamefiles/txt/puzzles/1.txt");
        return puzzle.getAsString();
    }
    else if(cointoss == 2){
        Puzzle puzzle("gamefiles/txt/puzzles/2.txt");
        return puzzle.getAsString();
    }
    else if(cointoss == 3){
        Puzzle puzzle("gamefiles/txt/puzzles/3.txt");
        return puzzle.getAsString();
    }
    else if(cointoss == 4){
        Puzzle puzzle("gamefiles/txt/puzzles/3.txt");
        return puzzle.getAsString();
    }
    else if(cointoss == 5){
        Puzzle puzzle("gamefiles/txt/puzzles/3.txt");
        return puzzle.getAsString();
    }
}

// Метод введення відповіді на загадку
int  Event::inputPuzzleAnswer(int answer){
    answer_quantity++;
    if (answer_quantity!=1){
        return -1;
    }
    if (puzzleSequenceNumber==1){
        Puzzle puzzle("gamefiles/txt/puzzles/1.txt");
        if(answer == puzzle.getCorrectAnswer()){
            return 1;
        }
        else return 0;
    }
    else if(puzzleSequenceNumber==2){
        Puzzle puzzle("gamefiles/txt/puzzles/2.txt");
        if(answer == puzzle.getCorrectAnswer()){
            return 1;
        }
        else return 0;
    }
    else if(puzzleSequenceNumber==3){
        Puzzle puzzle("gamefiles/txt/puzzles/3.txt");
        if(answer == puzzle.getCorrectAnswer()){
            return 1;
        }
        else return 0;
    }
    else if(puzzleSequenceNumber==4){
        Puzzle puzzle("gamefiles/txt/puzzles/4.txt");
        if(answer == puzzle.getCorrectAnswer()){
            return 1;
        }
        else return 0;
    }
    else if(puzzleSequenceNumber==5){
        Puzzle puzzle("gamefiles/txt/puzzles/5.txt");
        if(answer == puzzle.getCorrectAnswer()){
            return 1;
        }
        else return 0;
    }
}


