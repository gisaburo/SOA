echo '*************************************'
echo '* Create Root Certificate Authority *'
echo '*************************************'

rm -fr /opt/pki/RootCA/* # clean dir for rerun

cd /opt/pki/RootCA
mkdir newcerts
echo "01" > serial
echo "00" > crlnumber
touch index.txt

openssl genrsa \
  -out RootCA_key.pem \
  -aes256 -passout pass:rootcaprivkeypass 2048
if [ $? -eq 0 ]; then echo '== genrsa success =='; else echo '== genrsa unsuccess ==';exit 1; fi

openssl req \
  -new \
  -out RootCA_csr.pem \
  -key RootCA_key.pem \
  -passin pass:rootcaprivkeypass \
  -subj "/C=JP/ST=Tokyo/O=Private inc./CN=Private Root CA"
if [ $? -eq 0 ]; then echo '== req success =='; else echo '== req unsuccess ==';exit 1; fi

openssl ca \
  -config ../configs/openssl_sign.cnf \
  -out RootCA_crt.pem \
  -in RootCA_csr.pem \
  -selfsign \
  -keyfile RootCA_key.pem \
  -passin pass:rootcaprivkeypass \
  -batch \
  -extensions v3_ca
if [ $? -eq 0 ]; then echo '== ca success =='; else echo '== ca unsuccess ==';exit 1; fi

openssl x509 \
  -in RootCA_crt.pem \
  -out RootCA_crt.pem
if [ $? -eq 0 ]; then echo '== x509 success =='; else echo '== x509 unsuccess ==';exit 1; fi
