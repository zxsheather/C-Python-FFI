cmake_minimum_required(VERSION 3.10)

project(CPythonFFI)

set(CMAKE_CXX_STANDARD 17)

add_library(cpython_ffi SHARED IMPORTED)

if(APPLE)
  set_target_properties(cpython_ffi PROPERTIES IMPORTED_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}/lib/liblib.so")
else()
  set_target_properties(cpython_ffi PROPERTIES IMPORTED_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}/lib/liblib_x86.so")
endif()

add_executable(code main.cpp)

target_link_libraries(code PRIVATE cpython_ffi)