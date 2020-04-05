class AvailabilityZone:
    def __init__(self, region='ap-northeast-1') -> None:
        self.__region = region
 
        if self.__region == 'ap-northeast-1':
            self.__names = ['ap-northeast-1a', 'ap-northeast-1c', 'ap-northeast-1d']
        else:
            self.__names = []
 
    @property
    def names(self) -> list:
        return self.__names
 
    def name(self, az_number) -> str:
        return self.__names[az_number]


print(AvailabilityZone().names)
a = AvailabilityZone()
print(a.name(1))