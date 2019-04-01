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

add_executable(rand_uniform RandomSamples/Uniform.cpp)
target_link_libraries(rand_uniform -lstdc++fs)

add_executable(rand_beta RandomSamples/Beta.cpp)
target_link_libraries(rand_beta -lstdc++fs)

add_executable(rand_gamma RandomSamples/Gamma.cpp)
target_link_libraries(rand_gamma -lstdc++fs)

add_executable(rand_cauchy RandomSamples/Cauchy.cpp)
target_link_libraries(rand_cauchy -lstdc++fs)