#pragma once

#include "../events/Event.h"

#include <vector>
#include <sstream>


class Game {
private:
    Character character;
    string fileName;
    Event event;

public:
    Game();
    virtual ~Game();

    void initGame(const string name);
    void saveCharacter();
    void loadCharacter();

    string printCharacterSheet();
    int levelUpCharacter();
    int getCharacterStatPoints();
    void useCharacterStatPoints(int statpoint);

    string Travel();
    int inputPuzzleAnswer(int answer);
    int Attack();
    int Defend();

    int getCharacterHp();
    int getEnemyHp();
    int getCharacterStamina();
    int getCharacterGold();

    int gainExp();
    int gainGold(int amount);

    void healCharacter();
    void restCharacter();
    void upgradeCharacter();
};