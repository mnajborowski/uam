# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Users/michal.najborowski/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/212.5457.51/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/michal.najborowski/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/212.5457.51/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/zad2.dir/depend.make
# Include the progress variables for this target.
include CMakeFiles/zad2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/zad2.dir/flags.make

CMakeFiles/zad2.dir/main.cpp.o: CMakeFiles/zad2.dir/flags.make
CMakeFiles/zad2.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/zad2.dir/main.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/zad2.dir/main.cpp.o -c /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/main.cpp

CMakeFiles/zad2.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/zad2.dir/main.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/main.cpp > CMakeFiles/zad2.dir/main.cpp.i

CMakeFiles/zad2.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/zad2.dir/main.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/main.cpp -o CMakeFiles/zad2.dir/main.cpp.s

CMakeFiles/zad2.dir/SafeArray.cpp.o: CMakeFiles/zad2.dir/flags.make
CMakeFiles/zad2.dir/SafeArray.cpp.o: ../SafeArray.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/zad2.dir/SafeArray.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/zad2.dir/SafeArray.cpp.o -c /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/SafeArray.cpp

CMakeFiles/zad2.dir/SafeArray.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/zad2.dir/SafeArray.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/SafeArray.cpp > CMakeFiles/zad2.dir/SafeArray.cpp.i

CMakeFiles/zad2.dir/SafeArray.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/zad2.dir/SafeArray.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/SafeArray.cpp -o CMakeFiles/zad2.dir/SafeArray.cpp.s

# Object files for target zad2
zad2_OBJECTS = \
"CMakeFiles/zad2.dir/main.cpp.o" \
"CMakeFiles/zad2.dir/SafeArray.cpp.o"

# External object files for target zad2
zad2_EXTERNAL_OBJECTS =

zad2: CMakeFiles/zad2.dir/main.cpp.o
zad2: CMakeFiles/zad2.dir/SafeArray.cpp.o
zad2: CMakeFiles/zad2.dir/build.make
zad2: CMakeFiles/zad2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable zad2"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/zad2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/zad2.dir/build: zad2
.PHONY : CMakeFiles/zad2.dir/build

CMakeFiles/zad2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/zad2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/zad2.dir/clean

CMakeFiles/zad2.dir/depend:
	cd /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2 /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2 /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/cmake-build-debug /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/cmake-build-debug /Users/michal.najborowski/CLionProjects/bezpieczenstwo-oprogramowania/lab7/zad2/cmake-build-debug/CMakeFiles/zad2.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/zad2.dir/depend
