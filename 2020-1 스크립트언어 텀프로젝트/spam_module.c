#include "Python.h"
#include <math.h>

spam_SmallResultReturn(PyObject *self, PyObject *args) {
	float SeoulAverSaves = 0;
	float index = 0;

	if (!PyArg_ParseTuple(args, "ff",&SeoulAverSaves, &index))
		return NULL;

	float result = floor((SeoulAverSaves / index)*1000)/1000;
	return Py_BuildValue("f", result);

}

spam_BigResultReturn(PyObject *self, PyObject *args) {
	float SeoulAverSaves = 0;
	float index = 0;

	if (!PyArg_ParseTuple(args, "ff", &SeoulAverSaves, &index))
		return NULL;

	float result = floor((SeoulAverSaves / index)+0.5)
	return Py_BuildValue("f", result);

}

static PyMethodDef SpamMethods[] = {//스펨메소드
   {"SetSeoulAverS",spam_SmallResultReturn,METH_VARARGS,"underroundo"},
   {"SetSeoulAverB",spam_BigResultReturn,METH_VARARGS,"underroundx"},
   {NULL, NULL, 0, NULL}    //이 부분 정확하게 모르겠음
};

static struct PyModuleDef spammodule = {//생성할 모듈정보를 담은 구조체
   PyModuleDef_HEAD_INIT,
   "spam",            // 모듈이름 import sm=pam
   "텀프로젝트 c++연동모듈",
   -1,SpamMethods
};

//서울평균 그래프 그리기 위한 수치 측정


PyInit_spam(void)//가장처음실행함!
{
	return PyModule_Create(&spammodule);//모듈 구조체 참고
}
