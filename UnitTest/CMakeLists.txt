cmake_minimum_required(VERSION 3.15)

find_package(ICU REQUIRED COMPONENTS i18n uc)
include_directories(${ICU_INCLUDE_DIRS})
link_directories(${ICU_LIBRARY_DIRS})

find_package(Eigen3 REQUIRED)
include_directories(${Eigen3_INCLUDE_DIRS})

find_package(gtest REQUIRED)
include_directories(${PROJECT_SOURCE_DIR})
include_directories(/usr/src/googletest/googletest/include)
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/gtestlib)

add_executable(InterpolationTest InterpolationTest.cc ../interpolate.cc ../MMDFileIOUtil.cc ../VMD.cc)
target_link_libraries(InterpolationTest gtest::gtest ${ICU_LIBRARIES})
add_test(NAME InterpolationTest COMMAND InterpolationTest)

add_executable(FpsChangerTest FpsChangerTest.cc ../fpschanger.cc ../interpolate.cc ../MMDFileIOUtil.cc ../VMD.cc)
target_link_libraries(FpsChangerTest gtest::gtest ${ICU_LIBRARIES})
add_test(NAME FpsChangerTest COMMAND FpsChangerTest)

set(CMAKE_CXX_FLAGS "-g -Wall -std=c++11")

