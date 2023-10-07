run:
	g++ -o main main.cpp Game.cpp Character.cpp Enemy.cpp Event.cpp Puzzle.cpp Game_wrapped.cpp
	g++ -fPIC -shared -o cmake-build-debug/libcoursework.dll main.cpp Game.cpp Character.cpp Enemy.cpp Event.cpp Puzzle.cpp Game_wrapped.cpp