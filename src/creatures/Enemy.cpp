#include "../../include/lordaeron/creatures/Enemy.h"

// Конструктор класу Enemy
Enemy::Enemy(int level) {
    this->level = level;
    this->hpMax = rand()% (level * 11) + (level * 4);
    this->hp = this->hpMax;
    this->damageMin = this->level * 2;
    this->damageMax = this->level * 2 + 2;
    this->defence = rand() % level*4 + 1;
    this->accuracy = rand() % level*4 + 1;
}

// Деструктор класу Enemy
Enemy::~Enemy() {

}