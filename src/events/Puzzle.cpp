#include "../../include/lordaeron/events/Puzzle.h"

// Конструктор класу Puzzle
Puzzle::Puzzle(string fileName) {
    ifstream inFile(fileName);

    string answer = "";
    int correctAnswer = 0;

    if(inFile.is_open()){
        std::getline(inFile, this->question);

        for(int i = 0; i < 3; i++){
            getline(inFile, answer);
            this->answers.push_back(answer);
        }

        inFile >> correctAnswer;
        this->correctAnswer = correctAnswer;
        inFile.ignore();
    }


    inFile.close();
}

// Деструктор класу Puzzle
Puzzle::~Puzzle() {

}

//Метод виведення загадки як символьного рядка
string Puzzle::getAsString() {

    string story = "";
    string answers;

    int cointoss = rand() % 3;

    if (cointoss==0){
        story = "Ви бачите троля на дорозі.\n"
                "Так як троль виглядає не ворожо, ви підходите до нього.\n"
                "Він вам каже: \"Щоб пройти по цій дорозі, відгадай цю загадку:\n";
    }
    else if (cointoss==1){
        story = "Вас зупинив ельф на вході у ліс.\n"
                "Він вам каже: \"Щоб зайти у мій ліс, відгадай цю загадку:\n";
    }
    else if (cointoss==2){
        story = "Перед вами, на мості, появилася відьма.\n"
                "Вона вам каже: \"Щоб пройти по цьому мосту, відгадай цю загадку:\n";
    }

    for (int i = 0; i < this->answers.size(); i++)
    {
        answers += to_string(i+1) + ": " + this->answers[i] + "\n";
    }

    return story + this->question + "\"\n" + "\n"
           + answers + "\n";
}
