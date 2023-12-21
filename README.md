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