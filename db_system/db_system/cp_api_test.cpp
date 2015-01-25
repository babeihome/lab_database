#include <Python.h>

#define ManualBreak getchar();return 0;

void printDict(PyObject* obj)
{
	if (!PyDict_Check(obj))
		return;

	PyObject *k, *v, *keys, *values;
	keys = PyDict_Keys(obj);
	values = PyDict_Values(obj);

	for (int i = 0; i < PyList_GET_SIZE(keys); i++)
	{
		k = PyList_GET_ITEM(keys, i);
		v = PyList_GET_ITEM(values, i);
		char *c_name = PyString_AsString(k);
		char *v_name = PyString_AsString(v);
		printf("%s:\t %s\n", c_name, v_name);
	}
}

void printList(PyObject* pList){
	if (!PyList_Check(pList))
		return;

	PyObject *k;
	for (int i = 0; i < PyList_GET_SIZE(pList); i++){
		k = PyList_GET_ITEM(pList, i);
		char *c_name = PyString_AsString(k);
		printf("%s\n", c_name);
	}
}


int main(){
	//Interupter of Python initialize first
	Py_Initialize();

	if (!Py_IsInitialized()){
		printf("Initialized fail");
		return -1;
	}
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('../python_API')");
	//Load python module
	//PyObject * pModule = PyImport_ImportModule("config");
	PyObject *pModule = PyImport_ImportModule("raw_data_parse");
	PyObject *pFunc = PyObject_GetAttrString(pModule, "import_data");
	PyObject *pArgv = NULL;
	PyEval_CallObject(pFunc, pArgv);
	getchar();
}