#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

class Puzzle {
private:
    string question;
    vector<string> answers;
    int correctAnswer;

public:
    Puzzle(string fileName);
    virtual ~Puzzle();
    string getAsString();

    inline const int& getCorrectAnswer() { return this->correctAnswer; };
};


