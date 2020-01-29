echo '****************************'
echo '* Create Openssl Congigure *'
echo '****************************'

rm /opt/pki/configs/openssl_sign.cnf # clean dir for rerun

cat <<'EOF' > /opt/pki/configs/openssl_sign.cnf
[ ca ]
default_ca              = CA_default

[ CA_default ]
dir                     = ./
certs                   = $dir/certs
crl_dir                 = $dir/crl
database                = $dir/index.txt
new_certs_dir           = $dir/newcerts
serial                  = $dir/serial
crlnumber               = $dir/crlnumber
crl                     = $dir/crl.pem
RANDFILE                = $dir/.rand

name_opt                = ca_default
cert_opt                = ca_default

default_days            = 365
default_crl_days        = 30
default_bits            = 2048
default_md              = sha256
preserve                = no
policy                  = policy_match

[ policy_match ]
countryName             = match
stateOrProvinceName     = match
organizationName        = match
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[ v3_ca ]
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid:always,issuer
basicConstraints        = CA:true
keyUsage                = cRLSign,keyCertSign

[ v3_server ]
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid,issuer
basicConstraints        = CA:FALSE
keyUsage                = nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage        = serverAuth
subjectAltName          = @alt_names

[alt_names]
DNS.1                   = domain.com
DNS.2                   = sub.domain.com
IP.1                    = 192.168.100.80
IP.2                    = 192.168.100.241

[ v3_client ]
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid,issuer
basicConstraints        = CA:FALSE
keyUsage                = nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage        = clientAuth
EOF
