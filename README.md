# NodeMCU
NodeMCU is a low-cost open source IoT platform. It initially included firmware which runs on the ESP8266 Wi-Fi SoC from Espressif Systems, and hardware which was based on the ESP8266 module.

## NodeX

mkdir ~/environment/nodex
cd ~/environment/nodex
aws iot create-thing --thing-name nodex
aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key


arn:aws:iot:us-east-1:010703111265:cert/43cd84c2bd4470fa308a6c62f6f40c94f12a44496bb2fe4e7b9f6200d666019e

aws iot attach-policy --policy-name CarPolicy --target arn:aws:iot:us-east-1:010703111265:cert/43cd84c2bd4470fa308a6c62f6f40c94f12a44496bb2fe4e7b9f6200d666019e

aws iot attach-thing-principal --thing-name nodex --principal arn:aws:iot:us-east-1:010703111265:cert/43cd84c2bd4470fa308a6c62f6f40c94f12a44496bb2fe4e7b9f6200d666019e


## NodeO

mkdir ~/environment/nodeo
cd ~/environment/nodeo
aws iot create-thing --thing-name nodeo
aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key


arn:aws:iot:us-east-1:010703111265:cert/ecf4203431f3b5ce63ac891ce332c35fb77e960eb24f7daefb65d1c6574c4556

aws iot attach-policy --policy-name CarPolicy --target arn:aws:iot:us-east-1:010703111265:cert/ecf4203431f3b5ce63ac891ce332c35fb77e960eb24f7daefb65d1c6574c4556

aws iot attach-thing-principal --thing-name nodeo --principal arn:aws:iot:us-east-1:010703111265:cert/ecf4203431f3b5ce63ac891ce332c35fb77e960eb24f7daefb65d1c6574c4556


 cp ~/environment/car4/exercise-2.3.py ~/environment/nodeo
 cp ~/environment/car4/exercise-2.3.py ~/environment/nodex
 cd ~/environment/nodeo
python exercise-2.3.py



cp ~/environment/nodeo/exercise-2.3.py ~/environment/nodex

http://arduino.esp8266.com/stable/package_esp8266com_index.json

## OpenSSL

openssl x509 -in xx-certificate.pem.crt -out cert.der -outform DER 
openssl rsa -in xx-private.pem.key -out private.der -outform DER
openssl x509 -in AmazonRootCA1.pem -out ca.der -outform DER

87ae5407738c549bdbadc36749dd66f7e0bc0cfa9aab6deb7df6e022cc6b5d2d

openssl x509 -in a39b4a4502c858004dc578e8a52077499c44a6bf025dd56eb0ebc263b04c7fba-certificate.pem.crt -out cert.der -outform DER 
openssl rsa -in a39b4a4502c858004dc578e8a52077499c44a6bf025dd56eb0ebc263b04c7fba-private.pem.key -out private.der -outform DER
openssl x509 -in AmazonRootCA1.pem -out ca.der -outform DER

openssl x509 -in 87ae5407738c549bdbadc36749dd66f7e0bc0cfa9aab6deb7df6e022cc6b5d2d-certificate.pem.crt -out cert.der -outform DER 
openssl rsa -in 87ae5407738c549bdbadc36749dd66f7e0bc0cfa9aab6deb7df6e022cc6b5d2d-private.pem.key -out private.der -outform DER
openssl x509 -in AmazonRootCA1.pem -out ca.der -outform DER

## avx77d4n1rj2z-ats.iot.us-east-1.amazonaws.com
const char* ssid = "DoIT";
const char* password = "123Balaji";

000000000000001
led command = 1

## Quality Of Service
When subscribing to a topic, Quality of Service (QoS) 0 will be chosen by default.
Quality of Service 0 - Message will be delivered at most once
Quality of Service 1 - Message will be delivered at least once