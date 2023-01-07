#include <iostream>
using namespace std;
 
//Swap function to swap 2 numbers
void swap(int *num1, int *num2) {
   int temp;
   //Copy the value of num1 to some temp variable
   temp = *num1;
 
   //Copy the value of num2 to num1
   *num1 = *num2;
 
   //Copy the value of num1 stored in temp to num2
   *num2 = temp;
}
 
int main() {
   int num1, num2 = 8345242;
 
   //Inputting 2 numbers from user
//    cout<<"\nEnter the first number : ";
//    cin>>num1;
//    cout<<"\nEnter the Second number : ";
//    cin>>num2;
 
//    //Passing the addresses of num1 and num2
//    swap(&num1, &num2);
 
//    //Printing the swapped values of num1 and num2
//    cout<<"\nFirst number : "<< num1;
//    cout<<"\nSecond number: "<<num2;
 
//    return (0);
    cout << num1;
    return 0;
}