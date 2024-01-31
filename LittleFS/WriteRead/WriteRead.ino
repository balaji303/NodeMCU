#include "LittleFS.h"
 
void setup() 
{
  Serial.begin(115200);
  
  if(!LittleFS.begin())
  {
    Serial.println("An Error has occurred while mounting LittleFS");
    return;
  }
  
  File file = LittleFS.open("/balaji.txt", "r");
  if(!file)
  {
    Serial.println("Failed to open file for reading");
    return;
  }
  
  Serial.println("File Content:");
  while(file.available())
  {
    Serial.write(file.read());
  }
  file.close();
}
 
void loop() 
{
  //Writing a line to the file
  File file = LittleFS.open("/balaji.txt", "a");
  if(!file)
  {
    Serial.println("Failed to open file for writing");
    return;
  }
  
  file.write("Appending this line\r\n");
  
  file.close();

  //Reading the file and printing the content
  File fileread = LittleFS.open("/balaji.txt", "r");
  if(!fileread)
  {
    Serial.println("Failed to open file for reading");
    return;
  }
  
  Serial.println("File Content:");
  while(fileread.available())
  {
    Serial.write(fileread.read());
  }
  fileread.close();

  delay(5000);
}
