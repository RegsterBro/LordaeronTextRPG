cmake_minimum_required(VERSION 3.25)
project(Coursework)

set(CMAKE_CXX_STANDARD 17)

add_executable(Coursework main.cpp Game.cpp Character.cpp Enemy.cpp
        Event.cpp Puzzle.cpp Game_wrapped.cpp
        Game.h Character.h Enemy.h Event.h Puzzle.h)

