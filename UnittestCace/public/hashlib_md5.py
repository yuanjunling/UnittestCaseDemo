import hashlib
class Md5:
    def Hashlib_md5(self,par):
        parameter_md5 = par
        md5 = hashlib.md5()
        md5.update(parameter_md5.encode("utf-8"))
        parameter = md5.hexdigest()
        return parameter
MD5_ha=Md5()
if __name__=="__main__":
    md51=Md5()


