import uuid

class Character():
    def __init__(self):
        pass

    #转换特殊字符
    def ConvertSpecialCharacter(self,input):
        #charReplace = { "--": "－－" ,"'":"''" , "EXEC":"ＥＸＥＣ",  "<":"＜",  ">":"＞"}
        charReplace = {"'":"''"}
        if input=="":
            return ""
        else:
            strReturnValue = input
            for key,value in charReplace.items():
                strReturnValue = strReturnValue.replace(key, value);
            return strReturnValue

    #获取UUID
    def get_uuid(sef):
        return str(uuid.uuid1())

    def get_emplid_zero(sef,input):
        emplid = str(input)
        if len(emplid) < 8:
            emplid='0'+emplid
        return emplid

if __name__=='__main__':
    #print(Character().ConvertSpecialCharacter("It'test EXEC <"))
    #print(Character().get_uuid())
    print(Character().get_emplid_zero('09094080'))