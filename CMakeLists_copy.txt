project(CBSH22)

cmake_minimum_required (VERSION 2.6)

set(CMAKE_CXX_STANDARD 11)
SET(CMAKE_CXX_COMPILER "/usr/bin/g++")

SET (CMAKE_LINKER  "/usr/bin/ld")

SET(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -g -Wall --std=c++0x")

set(OpenCV_DIR "/usr/local/Cellar/opencv/4.0.1/lib/cmake/opencv4")
set(dlib_DIR "/usr/local/Cellar/dlib/19.17/lib/cmake/dlib")


include_directories("inc")
file(GLOB SOURCES "*src/*.cpp")



# Find Boost
find_package( Boost 1.49.0 REQUIRED COMPONENTS program_options system filesystem)
include_directories( ${Boost_INCLUDE_DIRS} )


find_package(OpenCV REQUIRED)
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

find_package(dlib REQUIRED)

file(GLOB srcs *.cpp *.c)
file(GLOB hdrs *.hpp *.h)


add_executable(CBSH22 ${SOURCES} )
target_link_libraries(CBSH22 ${Boost_LIBRARIES})
