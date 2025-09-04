#include <iostream>
#include <stack>


using namespace std;

stack <int> bateria;



int main() {
    

 bateria.push(55);
 bateria.push(1);
 bateria.push(100);
 bateria.push(99);
 bateria.push(999);
 bateria.push(333);
 bateria.push(12);

while (bateria.size()>0){
    cout << bateria.top() << endl;
    bateria.pop();
}

    
    
}