#pragma once

#include <stdlib.h>
#include <string>

using namespace std;

class Enemy {
private:
    int level;
    int hp;
    int hpMax;
    int damageMin;
    int damageMax;
    int defence;
    int accuracy;

public:
    Enemy(int level = 1);
    virtual ~Enemy();

    inline int getDamage()const { return rand() % this->damageMax + this->damageMin; }
    inline int getHp()const { return this->hp; }
    inline int getDefence()const { return this->defence; }
    inline int getAccuracy()const { return this->accuracy; }
    inline void takeDamage(int damage) { this->hp -= damage; }
};


