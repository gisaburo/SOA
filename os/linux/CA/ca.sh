echo '*******************'
echo '* Start Create CA *'
echo '*******************'

./mkdir.sh
./openssl.cnf.sh
./rootca.sh
./interca.sh
./server.sh

echo '*****************'
echo '* End Create CA *'
echo '*****************'
