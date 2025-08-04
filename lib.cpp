#include <iostream>
#include "lib.h"

extern "C" {
    int add(int a, int b) {
        return a + b;
    }

    void hello() {
        std::cout << "Hello World!" << std::endl;
    }
}