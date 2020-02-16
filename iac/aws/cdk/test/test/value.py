import yaml
#from abc import ABCMeta, abstractmethod
#class variable(metaclass=ABCMeta):
class variable:
#    @abstractmethod
    def __init__(self, *args, **kwargs):
        file=args[0]
        with open(file) as input:
            self.yml = yaml.load(input, Loader=yaml.FullLoader)

        if 'VPC' in self.yml:
            for i in range(len(self.yml['VPC'])):
                self.default =  {}
                self.default =  {
                                    'cidr_block': '10.0.0.0/16',
                                    'enable_dns_hostnames': True,
                                    'enable_dns_support': True,
                                    'instance_tenancy': 'default'
                }

                self.default.update(self.yml['VPC'][i])
                self.yml['VPC'][i].update(self.default)