echo '***************************************'
echo '* Create Server Certificate Authority *'
echo '***************************************'

rm -fr /opt/pki/Server/* # clean dir for rerun

cd /opt/pki/Server
mkdir newcerts
echo "01" > serial
echo "00" > crlnumber
touch index.txt

openssl genrsa \
  -out Server_key.pem \
  -aes256 \
  -passout pass:serverprivkeypass 2048
if [ $? -eq 0 ]; then echo '== genrsa success =='; else echo '== genrsa unsuccess ==';exit 1; fi

openssl req \
  -new \
  -out Server_csr.pem \
  -key Server_key.pem \
  -passin pass:serverprivkeypass \
  -subj "/C=JP/ST=Tokyo/O=Private inc./CN=Private Server CA"
if [ $? -eq 0 ]; then echo '== req success =='; else echo '== req unsuccess ==';exit 1; fi

cd /opt/pki/InterCA
openssl ca \
  -config ../configs/openssl_sign.cnf \
  -out ../Server/Server_crt.pem \
  -in ../Server/Server_csr.pem -cert InterCA_crt.pem \
  -keyfile InterCA_key.pem -passin pass:intercaprivkeypass \
  -batch \
  -extensions v3_server
if [ $? -eq 0 ]; then echo '== ca success =='; else echo '== ca unsuccess ==';exit 1; fi

cd /opt/pki/Server
openssl x509 \
  -in Server_crt.pem \
  -out Server_crt.pem
if [ $? -eq 0 ]; then echo '== x509 success =='; else echo '== x509 unsuccess ==';exit 1; fi
