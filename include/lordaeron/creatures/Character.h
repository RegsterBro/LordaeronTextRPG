#pragma once

#include <string>

using namespace std;

class Character {
private:
    int distanceTravelled;

    int gold;

    string name;
    int level;
    int exp;
    int expNext;

    int strength;
    int agility;
    int intelligence;

    int hp;
    int hpMax;
    int stamina;
    int staminaMax;
    int damageMin;
    int damageMax;
    int defence;
    int accuracy;

    int statPoints;

public:
    Character();
    Character(string name,
              int distanceTravelled,
              int gold,
              int level,
              int exp,
              int strength, int agility, int intelligence,
              int hp, int stamina,
              int statPoints);
    virtual ~Character();
    string getAsString() const;

    void initialize(string name);
    string printStats() const;

    int levelUp();
    void updateStats();
    void useStatPoint(int statpoint);

	inline const int& getLevel() const { return this->level; }
	inline const int& getStatPoints() const { return this->statPoints; }
	inline const int& getHP() const { return this->hp; }
	inline const int& getStamina() const { return this->stamina; }
	inline const int& getDamage()const { return rand() % this->damageMax + this->damageMin; }
    inline const int& getDefence() const { return this->defence; }
	inline const int& getAccuracy() const { return this->accuracy; }
	inline const int& getGold() const { return this->gold; }

    inline void travel() { this->distanceTravelled++; this->stamina--; }
    inline void gainExp(const int exp) { this->exp += exp; }
    inline void gainGold(const int gold) { this->gold += gold; }
    inline void payGold(const int gold) { this->gold -= gold; }
    inline void takeDamage(const int damage) { this->hp -= damage; }

    void heal();
    void rest();
    void upgrade();
};