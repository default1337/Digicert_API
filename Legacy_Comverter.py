#Import the requests module
import requests 

#Get Certificate Order ID
Cert_Order_Id = input("Enter Cert ID: ")

#Digicert Cert Central API Endpoint for looking up Legacy Order IDs returning new Digicert Cert Central Order IDs
Legacy_Endpoint = f"https://www.digicert.com/services/v2/oem-migration/{Cert_Order_Id}/order-id"

#Headers to send to the Digicert CertCentral API Endpoint
payload = ""
headers = {
    'X-DC-DEVKEY': "",
    'Content-Type': "application/json"
}

#Use the requests module to get the new Digitrust Cert Central order ID using the legacy Geotrust order ID. We also strip the text from the output of Legacy_Geotrust_Order_ID Variable to be used later on
Legacy_Geotrust_Order_Id = requests.request("GET", Legacy_Endpoint, data=payload, headers=headers)
New_Digicert_Order_Id = Legacy_Geotrust_Order_Id.text.strip('{"id":}')
print("Your new Digicert order ID is: " + New_Digicert_Order_Id)


#Use the requests module to print the certificate using the new Digicert Cert Central order ID using the .cer format.  Note Other formats are avliable
#This is the Digicert endpoint. Used to download data using a Digicert Cert Central Order ID in the cer formant.. Other formats can be used if needed.
Digicert_Endpoint = f"https://www.digicert.com/services/v2/certificate/download/order/{New_Digicert_Order_Id}/format/cer"

#Use the requests module to print the certificate using the new Digicert Cert Central order ID using the .cer format.  Note Other formats are avliable
print("Downlading new certificate in CER format")
Download_New_Cert = requests.request("GET", Digicert_Endpoint, data=payload, headers=headers)
print("")
print(Download_New_Cert.text)
