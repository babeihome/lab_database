#include <Python.h>

int maina(int argc, char *argv[]){
	/*
	Storing variables and control flags declaration for C/C++
	*/
	char *path = "./PedestalPar";


	/*
	Interface level for type transferring, function declaration
	*/
	Py_Initialize();

	if (!Py_IsInitialized()){
		return -1;
	}

	

}
