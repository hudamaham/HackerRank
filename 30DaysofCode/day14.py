

    # Add your code here
    def computeDifference(self):
        l=list()
        for e in self.__elements:
            for k in self.__elements:
                l.append(abs(e-k))
        
        self.maximumDifference=max(l)              

