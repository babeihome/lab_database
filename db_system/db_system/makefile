CXX = g++ 
 
TARGET = cp_api_test
 
C_FLAGS += -g -Wall -pthread
 
INC = -I/usr/local/include/python2.7/
LIB = -L/usr/local/lib/ -lpython2.7 -ldl -lutil
 
all: $(TARGET)
 
cp_api_test:  cp_api_test.o
    $(CXX) -o $@ $^  $(LIB) $(C_FLAGS)
 
.cpp.o:
    $(CXX) -c -o $*.o $(INC) $(C_FLAGS) $*.cpp
 
clean:
    -rm -f *.o $(TARGET)