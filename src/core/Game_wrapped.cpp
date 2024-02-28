#include "../../include/lordaeron/core/Game.h"

using namespace std;

extern "C"{
    __declspec(dllexport) Game* createGame(){
        return new Game();
    }

    __declspec(dllexport) void deleteGame(Game* game){
        delete game;
    }

    __declspec(dllexport) void initializeGame(Game* game, const char* name){
        game->initGame(name);
    }

    __declspec(dllexport) char* printCharSheet(Game* game, char* result, size_t resultMaxLength){
        _snprintf_s(result,resultMaxLength,_TRUNCATE,"%s",game->printCharacterSheet().c_str());
        return result;
    }

    __declspec(dllexport) void saveChar(Game* game){
        game->saveCharacter();
    }

    __declspec(dllexport) void loadChar(Game* game){
        game->loadCharacter();
    }

    __declspec(dllexport) char* Travel(Game* game, char* result, size_t resultMaxLength){
        _snprintf_s(result,resultMaxLength,_TRUNCATE,"%s",game->Travel().c_str());
        return result;
    }

    __declspec(dllexport) int getStamina(Game* game){
        return game->getCharacterStamina();
    }

    __declspec(dllexport) int inputPuzzleAnswer(Game* game, int answer){
        return game->inputPuzzleAnswer(answer);
    }

    __declspec(dllexport) int levelUp(Game* game){
        return game->levelUpCharacter();
    }

    __declspec(dllexport) int getStatPoints(Game* game){
        return game->getCharacterStatPoints();
    }

    __declspec(dllexport) void useStatPoints(Game* game, int statpoint){
        game->useCharacterStatPoints(statpoint);
    }

    __declspec(dllexport) int gainExp(Game* game){
        return game->gainExp();
    }

    __declspec(dllexport) int gainGold(Game* game, int amount){
        return game->gainGold(amount);
    }

    __declspec(dllexport) int getCharHP(Game* game){
        return game->getCharacterHp();
    }

    __declspec(dllexport) int getEnemyHP(Game* game){
        return game->getEnemyHp();
    }

    __declspec(dllexport) int Attack(Game* game){
        return game->Attack();
    }

    __declspec(dllexport) int Defend(Game* game){
        return game->Defend();
    }

    __declspec(dllexport) void heal(Game* game){
        game->healCharacter();
    }

    __declspec(dllexport) void rest(Game* game){
        game->restCharacter();
    }

    __declspec(dllexport) void upgrade(Game* game){
        game->upgradeCharacter();
    }

    __declspec(dllexport) int getGold(Game* game){
        return game->getCharacterGold();
    }
}