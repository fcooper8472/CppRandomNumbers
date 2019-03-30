cmake_minimum_required (VERSION 3.8)
project (CppRandomNumbers)

# ensure C++17
set (CMAKE_CXX_STANDARD 17)
set (CMAKE_CXX_STANDARD_REQUIRED ON)
set (CMAKE_CXX_EXTENSIONS OFF)

# Set global compiler warnings
if (MSVC)
    add_compile_options(/W4 /WX)
else ()
    add_compile_options (-Wall -Wextra -pedantic)
endif ()

add_executable(rand_normal RandomSamples/Normal.cpp)
target_link_libraries(rand_normal -lstdc++fs)