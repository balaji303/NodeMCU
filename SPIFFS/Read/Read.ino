/**
 * @file Read.ino
 * @author @balaji303 (https://github.com/balaji303)
 * @brief Using SPIFFS reads the file
 * @version 1
 * @date 29-01-2024
 * 
 * Copyright (c) 2023 @balaji303
 * 
 */
#include <string.h>
#include "FS.h"


bool    spiffsActive = false;
#define TESTFILE "/balaji.txt"


void setup()
{
  Serial.begin(115200);
  delay(1000);
  
  // Start filing subsystem
  if (SPIFFS.begin()) 
  {
      Serial.println("SPIFFS Active");
      Serial.println();
      spiffsActive = true;
  }
  else
  {
      Serial.println("Unable to activate SPIFFS");
  }
  delay(2000);
}




void loop()
{
  if (spiffsActive)
  {
    if (SPIFFS.exists(TESTFILE))
    {
     File f = SPIFFS.open(TESTFILE, "r");
      // 1. Read and Print the content
     if (!f) 
     {
       Serial.print("Unable To Open '");
       Serial.print(TESTFILE);
       Serial.println("' for Reading");
       Serial.println();
     }
     else
     {
       String s;
       Serial.print("Contents of file '");
       Serial.print(TESTFILE);
       Serial.println("'");
       Serial.println();
       while (f.position()<f.size())
       {
         s=f.readStringUntil('\n');
         s.trim();
         Serial.println(s);
//          Serial.println("*1*");
//          Serial.print(f.position());
//          Serial.println("*2*");
//          Serial.print(f.size());
//          Serial.println("***");
       } 
       f.close();
     }
     Serial.println();
    } 
    else
    {
      Serial.print("Unable To Find ");
      Serial.println(TESTFILE);
      Serial.println();
    }
  }
  
  while (true)
  {
    yield();
  }
}
