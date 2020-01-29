echo '**************************************'
echo '* Create Inter Certificate Authority *'
echo '**************************************'

rm -fr /opt/pki/InterCA/* # clean dir for rerun

cd /opt/pki/InterCA
mkdir newcerts
echo "01" > serial
echo "00" > crlnumber
touch index.txt

openssl genrsa \
  -out InterCA_key.pem \
  -aes256 \
  -passout pass:intercaprivkeypass 2048
if [ $? -eq 0 ]; then echo '== genrsa success =='; else echo '== genrsa unsuccess ==';exit 1; fi

openssl req \
  -new \
  -out InterCA_csr.pem \
  -key InterCA_key.pem \
  -passin pass:intercaprivkeypass \
  -subj "/C=JP/ST=Tokyo/O=Private inc./CN=Private Inter CA"
if [ $? -eq 0 ]; then echo '== req success =='; else echo '== req unsuccess ==';exit 1; fi

cd /opt/pki/RootCA
openssl ca \
  -config ../configs/openssl_sign.cnf \
  -out ../InterCA/InterCA_crt.pem \
  -in ../InterCA/InterCA_csr.pem -cert RootCA_crt.pem \
  -keyfile RootCA_key.pem -passin pass:rootcaprivkeypass \
  -batch \
  -extensions v3_ca
if [ $? -eq 0 ]; then echo '== ca success =='; else echo '== ca unsuccess ==';exit 1; fi

cd /opt/pki/InterCA
openssl x509 \
  -in InterCA_crt.pem \
  -out InterCA_crt.pem
if [ $? -eq 0 ]; then echo '== x509 success =='; else echo '== x509 unsuccess ==';exit 1; fi
