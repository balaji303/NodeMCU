/**
 * @file Read2.ino
 * @author @balaji303 (https://github.com/balaji303)
 * @brief Create a file and doing Write Read operation
 * @version 1
 * @date 31-01-2024
 * 
 * Copyright (c) 2023 @balaji303
 * 
 */
#include <Arduino.h>
#include <LittleFS.h>

const char *filename = "/example";

void setup() 
{
  Serial.begin(115200);

  delay(5000);

  LittleFS.begin();

  if (!LittleFS.exists(filename)) 
  {
    Serial.println("file does not exist, creating...");

    File file = LittleFS.open(filename, "w");

    if (!file) 
    {
      Serial.println("could not open the file for writing");
      LittleFS.end();
      return;
    }

    auto bytesWritten = file.write("hello\n");

    Serial.printf("bytes written: %d\n", bytesWritten);

    if (bytesWritten == 0) 
    {
      Serial.println("could not write to the file");
    }

    file.write("I am example file content\n");

    file.close();
  }

  LittleFS.end();
}

void loop() 
{
  LittleFS.begin();

  File file = LittleFS.open(filename, "r");

  if (!file) 
  {
    // handle the error
      Serial.println("could not open the file for writing");
      LittleFS.end();
      return;
  }

  auto content = file.readString();

  Serial.println(content.c_str());

  file.close();

  LittleFS.end();
  delay(5000);
}