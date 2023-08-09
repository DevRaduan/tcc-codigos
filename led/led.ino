const int led1=4;
const int led2=5;
int value=0;

void setup() 
   { 
      Serial.begin(9600); 
      pinMode(led1, OUTPUT);
      digitalWrite (led1, LOW);
      Serial.println("Connection established...");
   }
 
void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
     
     if (value == '1')
        digitalWrite (led1, HIGH);
     
     else if (value == '0')
        digitalWrite (led1, LOW);

        if (value == '2')
        digitalWrite (led2, HIGH);
     
     else if (value == '3')
        digitalWrite (led2, LOW);
   }
