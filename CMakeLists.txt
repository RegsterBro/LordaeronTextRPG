cmake_minimum_required(VERSION 3.25)
project(Coursework)

set(CMAKE_CXX_STANDARD 17)

add_executable(Coursework src/core/Game.cpp
        src/creatures/Character.cpp
        src/creatures/Enemy.cpp
        src/events/Event.cpp
        src/events/Puzzle.cpp
        src/core/Game_wrapped.cpp
        include/lordaeron/core/Game.h
        include/lordaeron/creatures/Character.h
        include/lordaeron/creatures/Enemy.h
        include/lordaeron/events/Event.h
        include/lordaeron/events/Puzzle.h
        src/core/main.cpp)

