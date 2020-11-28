ansible-playbook -i inventory .yml --ask-become-pass --tags "setup" --check 
ansible-playbook -i localhost, -c local local.yml --ask-become-pass --tags "setup"
ansible-playbook -i localhost, -c local local.yml --ask-become-pass --tags "guest"
ansible-playbook -i inventory kvm.yml --ask-become-pass --tags "network" --check
ansible-playbook -i inventory kvm.yml --ask-become-pass --tags "storage" --check
ansible-playbook -i inventory kvm.yml --ask-become-pass --tags "guest"