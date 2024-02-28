#pragma once

#include "Puzzle.h"
#include "../creatures/Character.h"
#include "../creatures/Enemy.h"

#include <stdlib.h>

class Event {
private:
    int puzzleSequenceNumber;
    int answer_quantity;
    Enemy enemy;

public:
    Event();
    virtual ~Event();
        string generateEvent(Character& character);

        string enemyEncounter(Character& character);
        int attack(Character& character);
        int defend(Character& character);
        inline int getEnemyHP() { return this->enemy.getHp(); };

        string puzzleEncounter();
        int inputPuzzleAnswer(int answer);
};


