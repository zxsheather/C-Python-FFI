cmake_minimum_required(VERSION 3.10)

project(CPythonFFI)

set(CMAKE_CXX_STANDARD 17)

add_library(cpython_ffi SHARED IMPORTED)

if(CMAKE_SYSTEM_PROCESSOR MATCHES "x86_64")
  set_target_properties(cpython_ffi PROPERTIES IMPORTED_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}/lib/liblib_x86.so")
else()
  set_target_properties(cpython_ffi PROPERTIES IMPORTED_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}/lib/liblib.so")
endif()

add_executable(code main.cpp)

target_link_libraries(code PRIVATE cpython_ffi)