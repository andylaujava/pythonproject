class Person():
    def __init__(self,n) -> None:
        super().__init__()
        self.name= n

    #override(覆寫)父類別的method
    def __repe__(self) -> str:
        own = super().__repr__()
        return f"我是person類別建立出來的實體\n{own}"
    
       



