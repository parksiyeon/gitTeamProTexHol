#include "python.h" 

static PyObject * 

spam_strlen(PyObject *self, PyObject *args) //args를 받아서
{
    const char* str=NULL;
    int len; 

    if (!PyArg_ParseTuple(args, "s", &str)) // "s'-->string 타입으로 바꿈

    len = strlen(str); //바꾼스트링의 길이 받음

    return Py_BuildValue("i", len); //받은 스트링의 길이 밸류를 파이오브젝트 타입으로 변견
}

static PyObject *
spam_division(PyObject *self, PyObject *args)
{
    int quotient=0;
    int dividend,divisor=0; 
           
    if (!PyArg_ParseTuple(args, "ii", &dividend,&divisor)) //인자로 받은 인티저 두개는 인티저로 파싱
          return NULL;
   
    if (divisor){
         quotient = dividend/divisor;
    } else {  // ������ 0�� �� ���� ó���� �մϴ�.
         // ���� ó���� �� ���� �ݵ�� NULL�� ���� ���ݴϴ�. PyErr_SetString�Լ��� �׻� NULL�� �����մϴ�.
         //PyExc_ZeroDivisionError�� 0���� �������� �� �� ���� �����Դϴ�.
         PyErr_SetString(PyExc_ZeroDivisionError, "divisor must not be zero");
         return  NULL;
    }
    
    return Py_BuildValue("i",quotient);//몫을 인티저 파이오브젝트타입으로 정환하여 파이썬으로 전달함
}

static PyMethodDef SpamMethods[] = {//스펨메소드
    {"strlen", spam_strlen, METH_VARARGS,//스트링렝뜨 와 디비전이있다고 기술
    "count a string length."},
    {"division", spam_division, METH_VARARGS,
    "division function \n return quotient, quotient is dividend / divisor"},
    {NULL, NULL, 0, NULL}    //d
};

static struct PyModuleDef spammodule = {//생성할 모듈정보를 담은 구조체
    PyModuleDef_HEAD_INIT,
    "spam",            // 모듈이름 import sm=pam
    "It is test module.",
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)//가장처음실행함!
{
    return PyModule_Create(&spammodule);//모듈 구조체 참고
}

//접누끝나면 비주얼-->새 프로젝트-->데스크탑 마법사-->이름 spam.c(응용프로그램 마법사 비어있는프로그램-->만든소스코드추가-
//이후피피티고대로따라하면될듯