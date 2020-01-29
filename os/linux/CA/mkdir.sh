echo '**********************'
echo '* Create Openssl Dir *'
echo '**********************'

rm -fr /opt/pki # clean dir for rerun

mkdir -p /opt/pki
mkdir /opt/pki/configs
mkdir /opt/pki/crl
mkdir /opt/pki/RootCA
mkdir /opt/pki/InterCA
mkdir /opt/pki/Server
mkdir /opt/pki/Client
