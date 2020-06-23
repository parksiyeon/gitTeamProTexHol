#include "Python.h"
//#include "Defines.c"

static PyObject* p;//파이썬 객체를 c 데이터타입으로구현

float SeoulAverSaves;

spam_SeoulAver(PyObject* self, PyObject* args) //args를 받아서
{
    float* seoulF;//인자값 저장할 임시변수

    if (!PyArg_ParseTuple(args, "f", &seoulF)) // args로 받은 인자를 인트형으로 바꿈
        return NULL;

    SeoulAverSaves += *seoulF;//전역 서울에더함

 //Pyarg_ParseTuple() 라는 파이썬 API는 인자의 타입을 검사한 후 C 변수로 바꿀 수 있다.
 //올바르지 않은 인자들이 전달되었을 경우 NULL 반환
}

spam_SeoulResultReturn(PyObject* self, PyObject* args) {
    int index = 0;
    if (!PyArg_ParseTuple(args, "i", &index))
        return NULL;

    float result = (SeoulAverSaves / index);
    return result;

}

static PyMethodDef SpamMethods[] = {//스펨메소드
   {"GetAllValue",spam_SeoulAver,METH_VARARGS,"GetAverSeoul"},
   {"SetSeoulAver",spam_SeoulResultReturn,METH_VARARGS,"ReturnAverResult"},
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

//서울 각 대기오염물질 평균값 구하는 프로세스 생각한것
//1. 티케이인터에서 그래프함수를 호출한다.
//2. 기존에 포문으로 리스트마다 값을 빼와서 더하는 방식 대신 리스트값을 float로 바꾸어 스팸모듈 인자에 바로 넣는다.
//3.전역변수 seoulaversaves에 들어온 인자들을 하나씩 더한다.
//4.티케이인터가 포문을 빠져나오면 numtodivede를 인자로 받아 평균값을 계산하여 반환한다(반환함수는 서울리설ㄾ트리턴~


//인덱스를 포문 안에서 바로 받아오거나/ 다 끝나고 numtodivide 에서 받아와도 됨..
//근데 다끝나고 하는것이 좋을듯(한 계산 끝날때마다 전역변수 초기화해줄 필요 없고 뭔가더열심히 짠거같을듯)하여 일단 그렇게함.